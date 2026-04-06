// ILA Agent Screen Builder — Figma Plugin
// Ermöglicht KI-Agenten das Erstellen von Figma-Screens via JSON-Input.
// Git-Identity: Cheko <cheko@ila-agent.local>

// --- Typen ---

interface ComponentSpec {
  name: string;
  x: number;
  y: number;
  label?: string;
}

interface ScreenSpec {
  screen_name: string;
  page: string;
  size: "desktop" | "mobile";
  components: ComponentSpec[];
}

interface PluginMessage {
  type: "build-screen" | "cancel";
  json?: string;
}

interface ResultMessage {
  type: "result";
  success: boolean;
  message: string;
  errors?: string[];
}

// --- Konstanten ---

const FRAME_SIZES: Record<string, { width: number; height: number }> = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};

// --- Hilfsfunktionen ---

/**
 * Sucht eine Komponente per Name in allen lokalen und eingebetteten Libraries.
 * Gibt den ComponentNode zurück oder null wenn nicht gefunden.
 */
async function findComponentByName(name: string): Promise<ComponentNode | null> {
  // 1. Lokale Komponenten (im aktuellen Dokument)
  const localComponents = figma.root.findAll(
    (node) => node.type === "COMPONENT" && node.name === name
  ) as ComponentNode[];

  if (localComponents.length > 0) {
    return localComponents[0];
  }

  // 2. Über importierte Component-Sets suchen (Varianten)
  const componentSets = figma.root.findAll(
    (node) => node.type === "COMPONENT_SET" && node.name === name
  ) as ComponentSetNode[];

  if (componentSets.length > 0) {
    const firstSet = componentSets[0];
    const children = firstSet.children.filter(
      (c) => c.type === "COMPONENT"
    ) as ComponentNode[];
    if (children.length > 0) {
      return children[0];
    }
  }

  // 3. Team Library / Remote Components via importComponentByKeyAsync
  // (Nur möglich wenn Key bekannt — hier Name-basierte Suche als Fallback)
  // Figma API erlaubt keinen direkten Name-Lookup in Team-Libraries ohne Key.
  // Hinweis wird im Fehler zurückgegeben.
  return null;
}

/**
 * Findet die Zielseite oder erstellt sie neu.
 */
function getOrCreatePage(pageName: string): PageNode {
  const existing = figma.root.children.find(
    (page) => page.name === pageName
  ) as PageNode | undefined;

  if (existing) {
    return existing;
  }

  const newPage = figma.createPage();
  newPage.name = pageName;
  return newPage;
}

/**
 * Setzt Text in einem TextNode — sucht rekursiv im Frame.
 */
async function applyLabel(node: SceneNode, label: string): Promise<void> {
  if (node.type === "TEXT") {
    await figma.loadFontAsync(node.fontName as FontName);
    node.characters = label;
    return;
  }

  if ("children" in node) {
    const textNodes = (node as ChildrenMixin).children.filter(
      (c) => c.type === "TEXT"
    ) as TextNode[];

    if (textNodes.length > 0) {
      const target = textNodes[0];
      await figma.loadFontAsync(target.fontName as FontName);
      target.characters = label;
    }
  }
}

/**
 * Hauptlogik: Baut einen Screen aus einer ScreenSpec.
 */
async function buildScreen(spec: ScreenSpec): Promise<ResultMessage> {
  const errors: string[] = [];
  const sizeKey = spec.size in FRAME_SIZES ? spec.size : "desktop";
  const { width, height } = FRAME_SIZES[sizeKey];

  // Seite aktivieren
  const targetPage = getOrCreatePage(spec.page);
  await figma.setCurrentPageAsync(targetPage);

  // Frame anlegen
  const frame = figma.createFrame();
  frame.name = spec.screen_name;
  frame.resize(width, height);
  frame.x = 0;
  frame.y = 0;

  // Hintergrundfarbe (Standard: Weiß)
  frame.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];

  // Komponenten einfügen
  for (const compSpec of spec.components) {
    const component = await findComponentByName(compSpec.name);

    if (!component) {
      errors.push(
        `Komponente nicht gefunden: "${compSpec.name}" — bitte sicherstellen, dass die Library eingebunden ist.`
      );
      continue;
    }

    try {
      const instance = component.createInstance();
      instance.x = compSpec.x;
      instance.y = compSpec.y;
      frame.appendChild(instance);

      // Label setzen falls vorhanden
      if (compSpec.label) {
        await applyLabel(instance, compSpec.label);
      }
    } catch (err) {
      errors.push(
        `Fehler beim Einfügen von "${compSpec.name}": ${(err as Error).message}`
      );
    }
  }

  // Viewport auf den neuen Frame ausrichten
  figma.viewport.scrollAndZoomIntoView([frame]);

  const success = errors.length === 0;
  const message = success
    ? `Screen "${spec.screen_name}" erfolgreich erstellt auf Seite "${spec.page}" (${sizeKey}: ${width}×${height}px).`
    : `Screen "${spec.screen_name}" erstellt — ${errors.length} Fehler aufgetreten.`;

  return { type: "result", success, message, errors };
}

// --- Plugin Entry Point ---

figma.showUI(__html__, { width: 480, height: 560, title: "ILA Screen Builder" });

figma.ui.onmessage = async (msg: PluginMessage) => {
  if (msg.type === "cancel") {
    figma.closePlugin();
    return;
  }

  if (msg.type === "build-screen" && msg.json) {
    let spec: ScreenSpec;

    try {
      spec = JSON.parse(msg.json) as ScreenSpec;
    } catch (parseErr) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message: `Ungültiges JSON: ${(parseErr as Error).message}`,
        errors: [],
      } as ResultMessage);
      return;
    }

    // Pflichtfelder prüfen
    if (!spec.screen_name || !spec.page || !spec.components) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message: "Pflichtfelder fehlen: screen_name, page und components sind erforderlich.",
        errors: [],
      } as ResultMessage);
      return;
    }

    try {
      const result = await buildScreen(spec);
      figma.ui.postMessage(result);
    } catch (err) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message: `Unerwarteter Fehler: ${(err as Error).message}`,
        errors: [],
      } as ResultMessage);
    }
  }
};

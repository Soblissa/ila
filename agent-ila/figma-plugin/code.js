// ILA Agent Screen Builder — Figma Plugin (compiled JS)
// Kompiliert aus code.ts — bei Änderungen code.ts bearbeiten und neu kompilieren.
// Git-Identity: Cheko <cheko@ila-agent.local>

"use strict";

// --- Konstanten ---
const FRAME_SIZES = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};

// --- Hilfsfunktionen ---

/**
 * Sucht eine Komponente per Name in allen lokalen und eingebetteten Libraries.
 */
async function findComponentByName(name) {
  // 1. Lokale Komponenten (im aktuellen Dokument)
  const localComponents = figma.root.findAll(
    (node) => node.type === "COMPONENT" && node.name === name
  );

  if (localComponents.length > 0) {
    return localComponents[0];
  }

  // 2. Über importierte Component-Sets suchen (Varianten)
  const componentSets = figma.root.findAll(
    (node) => node.type === "COMPONENT_SET" && node.name === name
  );

  if (componentSets.length > 0) {
    const firstSet = componentSets[0];
    const children = firstSet.children.filter((c) => c.type === "COMPONENT");
    if (children.length > 0) {
      return children[0];
    }
  }

  // 3. Kein Match gefunden
  return null;
}

/**
 * Findet die Zielseite oder erstellt sie neu.
 */
function getOrCreatePage(pageName) {
  const existing = figma.root.children.find((page) => page.name === pageName);
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
async function applyLabel(node, label) {
  if (node.type === "TEXT") {
    await figma.loadFontAsync(node.fontName);
    node.characters = label;
    return;
  }

  if ("children" in node) {
    const textNodes = node.children.filter((c) => c.type === "TEXT");
    if (textNodes.length > 0) {
      const target = textNodes[0];
      await figma.loadFontAsync(target.fontName);
      target.characters = label;
    }
  }
}

/**
 * Hauptlogik: Baut einen Screen aus einer ScreenSpec.
 */
async function buildScreen(spec) {
  const errors = [];
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
        `Fehler beim Einfügen von "${compSpec.name}": ${err.message}`
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

figma.ui.onmessage = async (msg) => {
  if (msg.type === "cancel") {
    figma.closePlugin();
    return;
  }

  if (msg.type === "build-screen" && msg.json) {
    let spec;

    try {
      spec = JSON.parse(msg.json);
    } catch (parseErr) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message: `Ungültiges JSON: ${parseErr.message}`,
        errors: [],
      });
      return;
    }

    // Pflichtfelder prüfen
    if (!spec.screen_name || !spec.page || !spec.components) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message:
          "Pflichtfelder fehlen: screen_name, page und components sind erforderlich.",
        errors: [],
      });
      return;
    }

    try {
      const result = await buildScreen(spec);
      figma.ui.postMessage(result);
    } catch (err) {
      figma.ui.postMessage({
        type: "result",
        success: false,
        message: `Unerwarteter Fehler: ${err.message}`,
        errors: [],
      });
    }
  }
};

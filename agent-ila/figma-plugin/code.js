// ILA Agent Screen Builder — Figma Plugin
// Version 2.0 — mit Komponenten-Index, kein loadAllPagesAsync
"use strict";

const FRAME_SIZES = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};

// Komponenten-Index — wird vom Plugin geladen
let COMPONENT_INDEX = null;

async function loadComponentIndex() {
  if (COMPONENT_INDEX) return COMPONENT_INDEX;
  // Index ist in den Plugin-Daten eingebettet
  COMPONENT_INDEX = {"Navigation Bar Main": {"nodeId": "5:43556", "originalName": "Navigation Bar Main 🆕", "width": 64, "height": 1018, "foundIn": "iFoe-L/Foerderplan/Initial"}, "Navigation Bar Content": {"nodeId": "5:43558", "originalName": "Navigation Bar Content", "width": 1216, "height": 64, "foundIn": "iFoe-L/Foerderplan/Initial"}, "Header Page Support": {"nodeId": "1:4192", "originalName": "Header Page Support", "width": 1104, "height": 136, "foundIn": "iFoe-L/Foerderakte"}, "Title": {"nodeId": "155:17016", "originalName": "Title", "width": 954, "height": 40, "foundIn": "ila-L/Foerderungen"}, "Button Floating": {"nodeId": "155:17029", "originalName": "Button Floating", "width": 234, "height": 56, "foundIn": "ila-L/Foerderungen"}, "Icon": {"nodeId": "I155:17029;4096:948", "originalName": "Icon", "width": 24, "height": 24, "foundIn": "ila-L/Foerderungen"}, "_Top-Level Navigation Item": {"nodeId": "I4:58300;7902:11879", "originalName": "_Top-Level Navigation Item", "width": 48, "height": 48, "foundIn": "iFoe-L/Foerderziel-in-Planung"}, "FAQ": {"nodeId": "I4:58300;7902:11881", "originalName": "FAQ", "width": 48, "height": 48, "foundIn": "iFoe-L/Foerderziel-in-Planung"}, "Favorites": {"nodeId": "I4:58300;7902:11883", "originalName": "Favorites", "width": 48, "height": 48, "foundIn": "iFoe-L/Foerderziel-in-Planung"}, "Open/Close": {"nodeId": "I4:58300;7903:12117", "originalName": "Open/Close", "width": 48, "height": 48, "foundIn": "iFoe-L/Foerderziel-in-Planung"}};;
  return COMPONENT_INDEX;
}

async function findComponentByName(name) {
  const normalize = (s) => {
    let r = '';
    for (let i = 0; i < s.length; i++) {
      if (s.charCodeAt(i) < 128) r += s[i];
    }
    return r.replace(/\s+/g, ' ').trim();
  };
  
  const norm = normalize(name);
  const index = await loadComponentIndex();
  
  // 1. Exakter Match im Index
  if (index[name]) {
    const entry = index[name];
    const node = await figma.getNodeByIdAsync(entry.nodeId);
    if (node) return node;
  }
  
  // 2. Normalisierter Match im Index
  if (index[norm]) {
    const entry = index[norm];
    const node = await figma.getNodeByIdAsync(entry.nodeId);
    if (node) return node;
  }
  
  // 3. Partial Match im Index
  for (const [key, entry] of Object.entries(index)) {
    if (normalize(key).includes(norm) || norm.includes(normalize(key))) {
      const node = await figma.getNodeByIdAsync(entry.nodeId);
      if (node) return node;
    }
  }
  
  return null;
}

function getOrCreatePage(pageName) {
  const existing = figma.root.children.find((page) => page.name === pageName);
  if (existing) return existing;
  const newPage = figma.createPage();
  newPage.name = pageName;
  return newPage;
}

async function applyLabel(instance, label) {
  const textNodes = [];
  function findText(node) {
    if (node.type === "TEXT") textNodes.push(node);
    if ("children" in node) node.children.forEach(findText);
  }
  findText(instance);
  if (textNodes.length > 0) {
    try {
      await figma.loadFontAsync(textNodes[0].fontName);
      textNodes[0].characters = label;
    } catch(e) {}
  }
}

async function buildScreen(spec) {
  const errors = [];
  let width, height;
  if (spec.width && spec.height) {
    width = spec.width;
    height = spec.height;
  } else {
    const sizeKey = spec.size in FRAME_SIZES ? spec.size : "desktop";
    width = FRAME_SIZES[sizeKey].width;
    height = FRAME_SIZES[sizeKey].height;
  }

  // Zielseite laden
  figma.ui.postMessage({ type: "status", message: "Bereite Seite vor..." });
  const targetPage = figma.root.children.find(p => p.name === spec.page);
  if (targetPage) {
    await targetPage.loadAsync();
    await figma.setCurrentPageAsync(targetPage);
  } else {
    const newPage = figma.createPage();
    newPage.name = spec.page;
    await figma.setCurrentPageAsync(newPage);
  }

  // Frame anlegen
  const frame = figma.createFrame();
  frame.name = spec.screen_name;
  frame.resize(width, height);
  frame.x = 0;
  frame.y = 0;
  frame.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];

  figma.ui.postMessage({ type: "status", message: "Füge Komponenten ein..." });

  for (const compSpec of spec.components) {
    // Node-ID direkt wenn angegeben
    let component = null;
    if (compSpec.nodeId) {
      try {
        const node = await figma.getNodeByIdAsync(compSpec.nodeId);
        if (node) component = node;
      } catch(e) {}
    }
    if (!component) component = await findComponentByName(compSpec.name);

    if (!component) {
      errors.push(`Komponente nicht gefunden: "${compSpec.name}"`);
      continue;
    }

    try {
      // Alle möglichen Fonts laden
      const fontFamilies = [
        "Noto Sans Display", "Noto Sans Display Condensed", 
        "Noto Sans", "Inter", "Roboto", "Arial", "Helvetica",
        "SF Pro Display", "SF Pro Text"
      ];
      const fontStyles = [
        "Thin", "Thin Italic", "ExtraLight", "ExtraLight Italic",
        "Light", "Light Italic", "Regular", "Italic",
        "Medium", "Medium Italic", "SemiBold", "SemiBold Italic",
        "Bold", "Bold Italic", "ExtraBold", "ExtraBold Italic",
        "Black", "Black Italic"
      ];
      for (const family of fontFamilies) {
        for (const style of fontStyles) {
          try { await figma.loadFontAsync({ family, style }); } catch(e) {}
        }
      }

      let instance;
      if (component.type === "COMPONENT") {
        instance = component.createInstance();
      } else {
        instance = component.clone();
      }
      instance.x = compSpec.x;
      instance.y = compSpec.y;
      frame.appendChild(instance);

      if (compSpec.label) {
        await applyLabel(instance, compSpec.label);
      }
    } catch (err) {
      errors.push(`Fehler bei "${compSpec.name}": ${err.message}`);
    }
  }

  figma.viewport.scrollAndZoomIntoView([frame]);

  const success = errors.length === 0;
  const message = success
    ? `Screen "${spec.screen_name}" erstellt (${width}×${height}px).`
    : `Screen "${spec.screen_name}" erstellt — ${errors.length} Fehler.`;

  return { type: "result", success, message, errors };
}

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
      figma.ui.postMessage({ type: "result", success: false, message: `Ungültiges JSON: ${parseErr.message}`, errors: [] });
      return;
    }

    if (!spec.screen_name || !spec.page || !spec.components) {
      figma.ui.postMessage({ type: "result", success: false, message: "Pflichtfelder fehlen: screen_name, page, components", errors: [] });
      return;
    }

    try {
      const result = await buildScreen(spec);
      figma.ui.postMessage(result);
    } catch (err) {
      figma.ui.postMessage({ type: "result", success: false, message: `Fehler: ${err.message}`, errors: [err.message] });
    }
  }
};

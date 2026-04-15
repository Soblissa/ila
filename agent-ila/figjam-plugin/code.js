// ILA Flow Builder — FigJam Plugin
"use strict";

figma.showUI(__html__, { width: 400, height: 500 });

// Farben
const COLORS = {
  blue:       { r: 0.094, g: 0.627, b: 0.984 },
  darkBlue:   { r: 0.118, g: 0.290, b: 0.490 },
  green:      { r: 0.188, g: 0.690, b: 0.314 },
  orange:     { r: 0.965, g: 0.620, b: 0.157 },
  red:        { r: 0.918, g: 0.220, b: 0.220 },
  gray:       { r: 0.600, g: 0.600, b: 0.600 },
  lightGray:  { r: 0.941, g: 0.941, b: 0.941 },
  white:      { r: 1.000, g: 1.000, b: 1.000 },
  purple:     { r: 0.576, g: 0.314, b: 0.796 },
};

const SHAPE_COLORS = {
  ROUNDED_RECTANGLE: { r: 0.094, g: 0.627, b: 0.984 },
  DIAMOND:           { r: 0.965, g: 0.620, b: 0.157 },
  ELLIPSE:           { r: 0.188, g: 0.690, b: 0.314 },
  PARALLELOGRAM:     { r: 0.576, g: 0.314, b: 0.796 },
  TRIANGLE_UP:       { r: 0.918, g: 0.220, b: 0.220 },
};

async function buildFlow(spec) {
  figma.ui.postMessage({ type: 'progress', message: 'Starte...' });

  const nodes = {};      // id → FigJam-Node
  const errors = [];
  let created = 0;

  // 1. Nodes erstellen
  for (const node of (spec.nodes || [])) {
    try {
      figma.ui.postMessage({ type: 'progress', message: `Erstelle: ${node.label}` });

      let shape;

      if (node.type === 'STICKY') {
        shape = figma.createSticky();
        shape.text.characters = node.label || '';
        shape.x = node.x || 0;
        shape.y = node.y || 0;
        if (node.color && COLORS[node.color]) {
          shape.fills = [{ type: 'SOLID', color: COLORS[node.color] }];
        }

      } else if (node.type === 'TEXT') {
        shape = figma.createText();
        for (const s of ['Regular','Medium','SemiBold','Bold']) { try { await figma.loadFontAsync({ family: 'Inter', style: s }); } catch(e) {} }
        shape.characters = node.label || '';
        shape.fontSize = node.fontSize || 14;
        shape.x = node.x || 0;
        shape.y = node.y || 0;

      } else {
        // Standard: ShapeWithText
        shape = figma.createShapeWithText();
        shape.shapeType = node.type || 'ROUNDED_RECTANGLE';

        // Größe
        shape.resize(node.width || 200, node.height || 60);
        shape.x = node.x || 0;
        shape.y = node.y || 0;

        // Text
        for (const s of ['Regular','Medium','SemiBold','Bold']) { try { await figma.loadFontAsync({ family: 'Inter', style: s }); } catch(e) {} }
        shape.text.characters = node.label || '';
        shape.text.fontSize = node.fontSize || 13;

        // Farbe
        const fillColor = node.fillColor
          ? COLORS[node.fillColor]
          : (SHAPE_COLORS[node.type] || COLORS.blue);
        shape.fills = [{ type: 'SOLID', color: fillColor }];

        // Textfarbe
        const textColor = node.textColor
          ? COLORS[node.textColor]
          : COLORS.white;
        shape.text.fills = [{ type: 'SOLID', color: textColor }];
      }

      shape.name = node.id || node.label || 'Node';
      nodes[node.id] = shape;
      created++;

    } catch(e) {
      errors.push(`Node "${node.label}": ${e.message}`);
    }
  }

  // 2. Connectors erstellen
  for (const conn of (spec.connectors || [])) {
    try {
      const fromNode = nodes[conn.from];
      const toNode   = nodes[conn.to];

      if (!fromNode) { errors.push(`Connector: Node "${conn.from}" nicht gefunden`); continue; }
      if (!toNode)   { errors.push(`Connector: Node "${conn.to}" nicht gefunden`); continue; }

      const connector = figma.createConnector();
      connector.connectorStart = { endpointNodeId: fromNode.id, magnet: 'AUTO' };
      connector.connectorEnd   = { endpointNodeId: toNode.id,   magnet: 'AUTO' };

      if (conn.label) {
        connector.connectorStartStrokeCap = 'NONE';
        connector.connectorEndStrokeCap   = 'ARROW_LINES';
        // Label als Text neben Connector (FigJam unterstützt kein direktes Label auf Connector)
      }

      if (conn.color && COLORS[conn.color]) {
        connector.strokes = [{ type: 'SOLID', color: COLORS[conn.color] }];
      }

      connector.strokeWeight = conn.strokeWeight || 2;
      created++;

    } catch(e) {
      errors.push(`Connector ${conn.from}→${conn.to}: ${e.message}`);
    }
  }

  // 3. Viewport anpassen
  if (Object.values(nodes).length > 0) {
    figma.viewport.scrollAndZoomIntoView(Object.values(nodes));
  }

  const msg = `${created} Elemente erstellt.${errors.length > 0 ? ' Fehler: ' + errors.join('; ') : ''}`;
  figma.ui.postMessage({ type: 'done', message: msg });
}

figma.ui.onmessage = async (msg) => {
  if (msg.type === 'build') {
    try {
      await buildFlow(msg.spec);
    } catch(e) {
      figma.ui.postMessage({ type: 'error', message: e.message });
    }
  }
};

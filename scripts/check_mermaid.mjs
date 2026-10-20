// Optional syntax check. Dependencies stay in the ignored documentation-tool cache.
import { readFile, readdir } from "node:fs/promises";
const { JSDOM } = await import("../.cache/docs-tools/node_modules/jsdom/lib/api.js");
const dom = new JSDOM("<!doctype html><html><body></body></html>");
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.Element = dom.window.Element;
globalThis.HTMLElement = dom.window.HTMLElement;
globalThis.SVGElement = dom.window.SVGElement;
const { default: mermaid } = await import("../.cache/docs-tools/node_modules/mermaid/dist/mermaid.core.mjs");
mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
const pattern = /(?:\x60{3}|~{3})mermaid\s*\r?\n([\s\S]*?)(?:\x60{3}|~{3})/g;
const sourceFolder = new URL("../docs/wiki/", import.meta.url);
let checked = 0;
for (const name of (await readdir(sourceFolder)).filter(name => name.endsWith(".md")).sort()) {
  const source = (await readFile(new URL(name, sourceFolder), "utf8")).replace(/\r\n/g, "\n");
  const exported = (await readFile(new URL("../dist/wiki/" + name, import.meta.url), "utf8")).replace(/\r\n/g, "\n");
  const blocks = [...source.matchAll(pattern)].map(match => match[1]);
  const exportedBlocks = [...exported.matchAll(pattern)].map(match => match[1]);
  if (JSON.stringify(blocks) !== JSON.stringify(exportedBlocks)) {
    throw new Error("Wiki export changed Mermaid diagrams in " + name);
  }
  for (let i = 0; i < blocks.length; i++) {
    const result = await mermaid.parse(blocks[i]);
    if (!result) throw new Error("Mermaid parser did not accept " + name + " diagram " + (i + 1));
    checked++;
    console.log("PASS " + name + " diagram " + (i + 1) + ": " + result.diagramType);
  }
}
if (!checked) throw new Error("No Mermaid diagrams found.");
console.log("PASS: " + checked + " diagrams parse, and Wiki export preserves their source.");
console.log("This checks syntax only; published GitHub rendering still requires a visual review.");
dom.window.close();

// Optional syntax check. Dependencies stay in the ignored documentation-tool cache.
import { readFile } from "node:fs/promises";
const { JSDOM } = await import("../.cache/docs-tools/node_modules/jsdom/lib/api.js");
const dom = new JSDOM("<!doctype html><html><body></body></html>");
globalThis.window = dom.window;
globalThis.document = dom.window.document;
globalThis.Element = dom.window.Element;
globalThis.HTMLElement = dom.window.HTMLElement;
globalThis.SVGElement = dom.window.SVGElement;
const { default: mermaid } = await import("../.cache/docs-tools/node_modules/mermaid/dist/mermaid.core.mjs");
mermaid.initialize({ startOnLoad: false, securityLevel: "strict" });
const source = (await readFile(new URL("../docs/wiki/11-Critical-User-Flows.md", import.meta.url), "utf8")).replace(/\r\n/g, "\n");
const exported = (await readFile(new URL("../dist/wiki/11-Critical-User-Flows.md", import.meta.url), "utf8")).replace(/\r\n/g, "\n");
const pattern = /(?:\x60{3}|~{3})mermaid\s*\r?\n([\s\S]*?)(?:\x60{3}|~{3})/g;
const blocks = [...source.matchAll(pattern)].map(match => match[1]);
const exportedBlocks = [...exported.matchAll(pattern)].map(match => match[1]);
if (blocks.length !== 2 || JSON.stringify(blocks) !== JSON.stringify(exportedBlocks)) {
  throw new Error("Expected exactly two unchanged Mermaid diagrams in source and Wiki export.");
}
for (let i = 0; i < blocks.length; i++) {
  const result = await mermaid.parse(blocks[i]);
  if (!result) throw new Error("Mermaid parser did not accept flow " + (i + 1));
  console.log("PASS FL-0" + (i + 1) + ": " + result.diagramType);
}
console.log("PASS: both flows parse, and Wiki export preserves the diagram source.");
console.log("This checks syntax only; published GitHub rendering still requires a visual review.");
dom.window.close();

import { existsSync } from "node:fs";
import { describe, expect, it } from "bun:test";

const greenfieldRoot = new URL("../../../../experiments/skills/ui-greenfield/", import.meta.url);
const designToCodeRoot = new URL("../../../../experiments/skills/ui-design-to-code/", import.meta.url);
const redesignRoot = new URL("../../../../experiments/skills/ui-redesign/", import.meta.url);
const greenfieldPath = new URL("SKILL.md", greenfieldRoot);
const designToCodePath = new URL("SKILL.md", designToCodeRoot);
const redesignPath = new URL("SKILL.md", redesignRoot);

describe("specialized UI skill contracts", () => {
  it("keeps ui-greenfield focused on new UI from scratch", async () => {
    // given
    const text = await Bun.file(greenfieldPath).text();

    // when
    const hasGreenfieldInputs = text.includes("product context") && text.includes("target audience");

    // then
    expect(hasGreenfieldInputs).toBe(true);
    expect(text).toContain("ambition lane");
    expect(text).toContain("lightweight implementation notes");
    expect(text).toContain("Select exactly one Layer A");
    expect(text).toContain("Select exactly one Layer B");
    expect(text).toContain("Mobile/tablet/desktop QA completed");
    expect(text).toContain("Accessibility checks completed");
    expect(text).toContain("Browser screenshot evidence recorded");
  });

  it("keeps ui-design-to-code focused on concrete references", async () => {
    // given
    const text = await Bun.file(designToCodePath).text();

    // when
    const treatsReferenceAsContract = text.includes("implementation contract");

    // then
    expect(treatsReferenceAsContract).toBe(true);
    expect(text).toContain("Figma");
    expect(text).toContain("source-site captures");
    expect(text).toContain("Create or update `DESIGN.md` only when");
    expect(text).toContain("No screenshot-as-background shortcut");
    expect(text).toContain("Component extensibility checked");
    expect(text).toContain("Actual browser captures exist");
  });

  it("keeps ui-redesign focused on designer-led existing UI redesign", async () => {
    // given
    const text = await Bun.file(redesignPath).text();

    // when
    const hasDesignerPerspective = text.includes("designer's perspective");

    // then
    expect(hasDesignerPerspective).toBe(true);
    expect(text).toContain("Do not perform unrelated redesign");
    expect(text).toContain("Redesign goal identified");
    expect(text).toContain("Changed breakpoints checked");
    expect(text).toContain("Changed states checked");
    expect(text).toContain("Browser evidence recorded");
    expect(text).toContain("Before/after evidence recorded when useful");
  });

  it("requires all specialized skills to use authoritative design sources", async () => {
    // given
    const greenfield = await Bun.file(greenfieldPath).text();
    const designToCode = await Bun.file(designToCodePath).text();
    const redesign = await Bun.file(redesignPath).text();

    // when
    const combinedText = [greenfield, designToCode, redesign].join("\n");

    // then
    expect(combinedText).toContain("Figma design system");
    expect(combinedText).toContain("repo tokens");
    expect(combinedText).toContain("Existing `DESIGN.md`");
    expect(combinedText).toContain("lightweight implementation notes");
  });

  it("keeps experimental skills self-contained", async () => {
    // given
    const greenfield = await Bun.file(greenfieldPath).text();
    const designToCode = await Bun.file(designToCodePath).text();
    const redesign = await Bun.file(redesignPath).text();

    // when
    const combinedText = [greenfield, designToCode, redesign].join("\n");

    // then
    expect(combinedText).not.toContain("core/skills/frontend");
    expect(combinedText).not.toContain("frontend/references");
    expect(combinedText).not.toContain("frontend/scripts");
    expect(combinedText).toContain("Evidence must record");
  });

  it("includes references scripts and templates in each experimental skill", async () => {
    // given
    const expectedPaths = [
      new URL("references/design/_INDEX.md", greenfieldRoot),
      new URL("references/ui-ux-db/palettes.csv", greenfieldRoot),
      new URL("scripts/search-uiux-db.mjs", greenfieldRoot),
      new URL("scripts/capture-browser.mjs", greenfieldRoot),
      new URL("templates/DESIGN.md", greenfieldRoot),
      new URL("package.json", greenfieldRoot),
      new URL("references/design/image-to-code-skill.md", designToCodeRoot),
      new URL("references/visual-qa/reference-fidelity.md", designToCodeRoot),
      new URL("scripts/capture-browser.mjs", designToCodeRoot),
      new URL("scripts/visual-diff.mjs", designToCodeRoot),
      new URL("templates/DESIGN.md", designToCodeRoot),
      new URL("package.json", designToCodeRoot),
      new URL("references/design-ops/critique.md", redesignRoot),
      new URL("references/perfection/performance-audit.md", redesignRoot),
      new URL("references/visual-qa/browser-capture.md", redesignRoot),
      new URL("scripts/capture-browser.mjs", redesignRoot),
      new URL("templates/DESIGN.md", redesignRoot),
      new URL("package.json", redesignRoot),
    ];

    // when
    const missingPaths = expectedPaths.filter((path) => !existsSync(path));

    // then
    expect(missingPaths).toEqual([]);
  });
});

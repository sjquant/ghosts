import { describe, expect, it } from "bun:test";

const greenfieldPath = new URL("../../ui-greenfield/SKILL.md", import.meta.url);
const designToCodePath = new URL("../../ui-design-to-code/SKILL.md", import.meta.url);
const improvePath = new URL("../../ui-improve/SKILL.md", import.meta.url);

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

  it("keeps ui-improve focused on existing UI changes", async () => {
    // given
    const text = await Bun.file(improvePath).text();

    // when
    const hasExistingSourceRule = text.includes("First identify the existing source");

    // then
    expect(hasExistingSourceRule).toBe(true);
    expect(text).toContain("Do not perform unrelated redesign");
    expect(text).toContain("Improvement goal identified");
    expect(text).toContain("Changed breakpoints checked");
    expect(text).toContain("Changed states checked");
    expect(text).toContain("Browser evidence recorded");
    expect(text).toContain("Before/after evidence recorded when useful");
  });

  it("requires all specialized skills to use authoritative design sources", async () => {
    // given
    const greenfield = await Bun.file(greenfieldPath).text();
    const designToCode = await Bun.file(designToCodePath).text();
    const improve = await Bun.file(improvePath).text();

    // when
    const combinedText = [greenfield, designToCode, improve].join("\n");

    // then
    expect(combinedText).toContain("Figma design system");
    expect(combinedText).toContain("repo tokens");
    expect(combinedText).toContain("Existing `DESIGN.md`");
    expect(combinedText).toContain("lightweight implementation notes");
  });
});

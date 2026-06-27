import { describe, expect, it } from "bun:test";

const skillPath = new URL("../SKILL.md", import.meta.url);

describe("frontend skill contract", () => {
  it("routes concrete visual references to ui-design-to-code", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasDesignToCodeRoute = text.includes("ui-design-to-code");

    // then
    expect(hasDesignToCodeRoute).toBe(true);
    expect(text).toContain("Concrete visual reference");
    expect(text).toContain("Figma");
    expect(text).toContain("designer spec");
    expect(text).toContain("ui-design-to-code");
  });

  it("routes new UI work to ui-greenfield", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasGreenfieldRoute = text.includes("ui-greenfield");

    // then
    expect(hasGreenfieldRoute).toBe(true);
    expect(text).toContain("New UI with no concrete visual reference");
    expect(text).toContain("ui-greenfield");
  });

  it("routes existing UI changes to ui-improve", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasImproveRoute = text.includes("ui-improve");

    // then
    expect(hasImproveRoute).toBe(true);
    expect(text).toContain("Existing UI change");
    expect(text).toContain("ui-improve");
  });

  it("does not make DESIGN.md mandatory for all workflows", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const treatsDesignMdAsOptionalSource = text.includes("one possible design contract");

    // then
    expect(treatsDesignMdAsOptionalSource).toBe(true);
    expect(text).toContain("Figma design system");
    expect(text).toContain("Existing repo tokens");
    expect(text).toContain("lightweight implementation notes");
    expect(text).not.toContain("Requires DESIGN.md before UI code");
    expect(text).not.toContain("DESIGN.md exists before new components");
  });
});

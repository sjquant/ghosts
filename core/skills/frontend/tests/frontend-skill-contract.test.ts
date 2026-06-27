import { describe, expect, it } from "bun:test";

const skillPath = new URL("../SKILL.md", import.meta.url);

describe("frontend skill contract", () => {
  it("requires concrete visual references to become a visual contract", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasContractLanguage = text.includes("Concrete visual reference");

    // then
    expect(hasContractLanguage).toBe(true);
    expect(text).toContain("Concrete visual reference");
    expect(text).toContain("reference-fidelity");
    expect(text).toContain("DESIGN.md");
    expect(text).toContain("visual contract");
  });

  it("requires greenfield work to load references before UI code", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasGreenfieldRoute = text.includes("Greenfield");

    // then
    expect(hasGreenfieldRoute).toBe(true);
    expect(text).toContain("Greenfield");
    expect(text).toContain("_INDEX.md");
    expect(text).toContain("Layer A");
    expect(text).toContain("Layer B");
  });

  it("defines flatness as a failure", async () => {
    // given
    const text = await Bun.file(skillPath).text();

    // when
    const hasFlatnessGate = text.includes("Correct-but-flat is a failure");

    // then
    expect(hasFlatnessGate).toBe(true);
    expect(text).toContain("Correct-but-flat is a failure");
    expect(text).toContain("flatten");
  });
});

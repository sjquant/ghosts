import { describe, expect, it } from "bun:test";

const refPath = new URL("../references/visual-qa/reference-fidelity.md", import.meta.url);
const qaPath = new URL("../references/visual-qa/README.md", import.meta.url);
const browserCapturePath = new URL("../references/visual-qa/browser-capture.md", import.meta.url);

describe("visual QA contract", () => {
  it("checks both visual match and implementation quality", async () => {
    // given
    const text = await Bun.file(refPath).text();

    // when
    const hasVisualQualityGate = text.includes("Flatness/material quality");

    // then
    expect(hasVisualQualityGate).toBe(true);
    expect(text).toContain("Pixel/layout fidelity");
    expect(text).toContain("Component extensibility");
    expect(text).toContain("No screenshot-as-background shortcut");
    expect(text).toContain("Flatness/material quality");
  });

  it("captures responsive and state coverage", async () => {
    // given
    const text = await Bun.file(qaPath).text();

    // when
    const hasResponsiveCoverage = text.includes("375px mobile") && text.includes("1280px desktop");

    // then
    expect(hasResponsiveCoverage).toBe(true);
    expect(text).toContain("375px mobile");
    expect(text).toContain("768px tablet");
    expect(text).toContain("1280px desktop");
    expect(text).toContain("hover");
    expect(text).toContain("error");
  });

  it("uses tmp for browser evidence paths", async () => {
    // given
    const text = await Bun.file(browserCapturePath).text();

    // when
    const usesTmpEvidence = text.includes("/tmp/frontend-evidence");

    // then
    expect(usesTmpEvidence).toBe(true);
    expect(text).not.toContain(".evidence");
  });
});

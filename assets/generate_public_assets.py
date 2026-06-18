from pathlib import Path
import html
import math

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT

COLORS = {
    "bg": "#F8FAFC",
    "panel": "#FFFFFF",
    "panel2": "#F1F5F9",
    "text": "#0F172A",
    "muted": "#64748B",
    "line": "#CBD5E1",
    "line2": "#E2E8F0",
    "blue": "#2563EB",
    "blue2": "#DBEAFE",
    "cyan": "#0891B2",
    "cyan2": "#CFFAFE",
    "violet": "#7C3AED",
    "violet2": "#EDE9FE",
    "green": "#059669",
    "green2": "#D1FAE5",
    "amber": "#D97706",
    "amber2": "#FEF3C7",
    "red": "#DC2626",
    "red2": "#FEE2E2",
    "slate": "#475569",
    "slate2": "#E2E8F0",
}


def esc(value: str) -> str:
    return html.escape(str(value), quote=True)


def wrap_text(text: str, max_chars: int = 28) -> list[str]:
    lines: list[str] = []
    for paragraph in str(text).split("\n"):
        words = paragraph.split()
        line = ""
        for word in words:
            if len(line) + len(word) + 1 <= max_chars:
                line = (line + " " + word).strip()
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


class SVG:
    def __init__(self, title: str, subtitle: str | None = None, w: int = 1200, h: int = 720):
        self.w = w
        self.h = h
        self.parts: list[str] = []
        self.defs = [
            """<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
  <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#0F172A" flood-opacity="0.10"/>
</filter>""",
            """<marker id="arrow" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
  <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748B"/>
</marker>""",
        ]
        self.parts.append(f'<rect width="{w}" height="{h}" fill="{COLORS["bg"]}"/>')
        self.parts.append('<g opacity="0.38">')
        for x in range(60, w, 60):
            self.parts.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="#E2E8F0" stroke-width="1"/>')
        for y in range(60, h, 60):
            self.parts.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="#E2E8F0" stroke-width="1"/>')
        self.parts.append("</g>")
        self.title(title, subtitle)

    def title(self, title: str, subtitle: str | None = None) -> None:
        self.text(56, 58, title, 32, weight=760, color=COLORS["text"])
        if subtitle:
            self.text(56, 89, subtitle, 15, color=COLORS["muted"])
        self.parts.append(
            f'<line x1="56" y1="114" x2="{self.w - 56}" y2="114" stroke="{COLORS["line2"]}" stroke-width="1.5"/>'
        )

    def text(
        self,
        x: float,
        y: float,
        text: str,
        size: int = 16,
        weight: int = 400,
        color: str | None = None,
        anchor: str = "start",
        opacity: float | None = None,
        extra: str = "",
    ) -> None:
        color = color or COLORS["text"]
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="Inter, Segoe UI, Arial, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}"{op} {extra}>{esc(text)}</text>'
        )

    def multiline(
        self,
        x: float,
        y: float,
        text: str,
        size: int = 16,
        line_h: int = 22,
        weight: int = 400,
        color: str | None = None,
        anchor: str = "start",
        max_chars: int = 32,
    ) -> None:
        for i, line in enumerate(wrap_text(text, max_chars)):
            self.text(x, y + i * line_h, line, size, weight, color, anchor)

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        rx: float = 18,
        fill: str | None = None,
        stroke: str | None = None,
        sw: float = 1.5,
        filter_id: str | None = None,
        opacity: float | None = None,
    ) -> None:
        fill = fill or COLORS["panel"]
        stroke = stroke or COLORS["line"]
        fil = f' filter="url(#{filter_id})"' if filter_id else ""
        op = f' opacity="{opacity}"' if opacity is not None else ""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{fil}{op}/>'
        )

    def pill(self, x: float, y: float, w: float, h: float, label: str, color: str, fill: str | None = None) -> None:
        fill = fill or f"{color}22"
        self.rect(x, y, w, h, rx=h / 2, fill=fill, stroke=color, sw=1.2)
        self.text(x + w / 2, y + h / 2 + 5, label, 13, 650, color, anchor="middle")

    def card(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        title: str,
        subtitle: str | None = None,
        accent: str = COLORS["blue"],
        fill: str = COLORS["panel"],
    ) -> None:
        self.rect(x, y, w, h, rx=22, fill=fill, stroke=COLORS["line"], sw=1.2, filter_id="shadow")
        self.parts.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{accent}"/>')
        self.text(x + 28, y + 38, title, 20, 740, accent)
        if subtitle:
            self.multiline(x + 28, y + 65, subtitle, 13, 18, 400, COLORS["muted"], max_chars=42)

    def arrow(self, x1: float, y1: float, x2: float, y2: float, color: str = COLORS["muted"], sw: float = 2.0, dash: bool = False) -> None:
        dash_str = ' stroke-dasharray="8 8"' if dash else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
            f'stroke="{color}" stroke-width="{sw}" marker-end="url(#arrow)"{dash_str}/>'
        )

    def circle(self, cx: float, cy: float, r: float, fill: str, stroke: str | None = None, sw: float = 1.2) -> None:
        stroke = stroke or fill
        self.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img">
<title>{esc(path.stem.replace("_", " ").title())}</title>
<defs>
{chr(10).join(self.defs)}
</defs>
{chr(10).join(self.parts)}
</svg>
"""
        path.write_text(content, encoding="utf-8")


def diagram_project_boundary() -> None:
    s = SVG("Sonata project boundary", "Public dossier framing: what the project claims, and what it explicitly does not claim")
    s.card(70, 160, 495, 450, "Sonata IS", "laboratory evidence, reproducible artifacts, and public-safe technical summaries", COLORS["blue"])
    for i, text in enumerate([
        "Research platform for custom AI systems",
        "Tensor / autograd / runtime stack",
        "CPU, assembly and CUDA backend path",
        "Training and inference experiments",
        "INT8 quantization validation",
        "Symbolic-control bridge experiments",
        "Closed-source core with public evidence",
    ]):
        y = 305 + i * 41
        s.circle(105, y - 5, 5, COLORS["blue"])
        s.multiline(125, y, text, 16, 21, 500, COLORS["text"], max_chars=44)
    s.card(635, 160, 495, 450, "Sonata IS NOT", "boundaries stay visible so the portfolio reads as evidence, not hype", COLORS["red"])
    for i, text in enumerate([
        "Not a finished commercial product",
        "Not a general-purpose AGI system",
        "Not a deployed security product",
        "Not open-source core code",
        "Not guaranteed beyond the tested lab context",
        "Not a claim of production maturity",
    ]):
        y = 310 + i * 45
        s.circle(670, y - 5, 5, COLORS["red"])
        s.multiline(690, y, text, 16, 21, 500, COLORS["text"], max_chars=42)
    s.save(OUTPUT / "diagrams/project_boundary.svg")


def diagram_public_private() -> None:
    s = SVG("Disclosure boundary", "Separate public proof materials from private implementation recipes")
    s.card(70, 170, 455, 400, "Private core", "kept internal to avoid leaking exact implementation paths", COLORS["red"])
    for i, text in enumerate(["source code and internal branches", "exact architectural recipes", "raw checkpoints and logs", "failure history and roadmap", "unsafe operational details"]):
        y = 295 + i * 50
        s.rect(108, y - 22, 24, 24, rx=7, fill=COLORS["red2"], stroke=COLORS["red"])
        s.text(150, y, text, 16, 520, COLORS["text"])
    s.card(675, 170, 455, 400, "Public dossier", "portable, portfolio-safe evidence and explanation layer", COLORS["green"])
    for i, text in enumerate(["architecture summaries", "benchmark plots and limits", "claim/evidence matrices", "validation reports", "screenshots and demos"]):
        y = 295 + i * 50
        s.rect(713, y - 22, 24, 24, rx=7, fill=COLORS["green2"], stroke=COLORS["green"])
        s.text(755, y, text, 16, 520, COLORS["text"])
    s.arrow(535, 366, 665, 366, sw=2.5)
    s.text(600, 335, "curated extract", 14, 650, COLORS["muted"], anchor="middle")
    s.save(OUTPUT / "diagrams/public_private_boundary.svg")


def diagram_layered_architecture() -> None:
    s = SVG("Layered architecture", "A readable stack diagram: high-level public view without implementation leakage")
    layers = [
        ("Training & inference experiments", "Visible research behavior and benchmark outputs", COLORS["violet"], COLORS["violet2"]),
        ("Symbolic control bridge", "Logos-style constraints and validation loop", COLORS["blue"], COLORS["blue2"]),
        ("Model and checkpoint system", "state, serialization, reproducibility boundaries", COLORS["green"], COLORS["green2"]),
        ("Tensor / autograd engine", "gradient flow and computation graph layer", COLORS["amber"], COLORS["amber2"]),
        ("HAL and backend dispatch", "CPU / ASM / CUDA selection boundary", COLORS["cyan"], COLORS["cyan2"]),
        ("Runtime foundation", "memory, scheduling, pools and safety fuses", COLORS["slate"], COLORS["slate2"]),
    ]
    x, w = 245, 710
    y0, h, gap = 150, 70, 18
    for i, (name, desc, accent, fill) in enumerate(layers):
        y = y0 + i * (h + gap)
        s.rect(x, y, w, h, rx=20, fill=fill, stroke=accent, sw=1.8)
        s.text(x + 28, y + 30, name, 20, 750, accent)
        s.text(x + 28, y + 53, desc, 14, 400, COLORS["muted"])
        if i < len(layers) - 1:
            s.arrow(x + w / 2, y + h + 3, x + w / 2, y + h + gap - 4, sw=1.5)
    brackets = [(175, 315), (350, 500), (535, 645)]
    layer_names = ["public layer", "engine layer", "system layer"]
    for (by1, by2), name in zip(brackets, layer_names):
        s.parts.append(f'<path d="M180 {by1} L180 {by2}" stroke="{COLORS["line"]}" stroke-width="3" stroke-linecap="round"/>')
        s.text(120, (by1 + by2) / 2 + 5, name, 14, 700, COLORS["muted"])
    s.save(OUTPUT / "diagrams/layered_architecture.svg")


def diagram_backend_ladder() -> None:
    s = SVG("Backend dispatch chain", "Fallback ladder for heterogeneous execution, presented as capability tiers")
    tiers = [
        ("01", "GPU / CUDA", "cuBLAS and custom-kernel route", COLORS["green"], COLORS["green2"]),
        ("02", "Multithreaded CPU", "Pascal thread pool route", COLORS["blue"], COLORS["blue2"]),
        ("03", "Assembly kernels", "x86-64 SIMD optimized route", COLORS["amber"], COLORS["amber2"]),
        ("04", "Pascal reference", "portable fallback and correctness anchor", COLORS["red"], COLORS["red2"]),
    ]
    x, y = 200, 165
    for i, (num, title, desc, accent, fill) in enumerate(tiers):
        yy = y + i * 118
        s.rect(x, yy, 800, 84, rx=24, fill=COLORS["panel"], stroke=COLORS["line"], filter_id="shadow")
        s.circle(x + 54, yy + 42, 27, fill, accent, 1.5)
        s.text(x + 54, yy + 48, num, 17, 800, accent, anchor="middle")
        s.text(x + 105, yy + 35, title, 22, 780, accent)
        s.text(x + 105, yy + 62, desc, 15, 400, COLORS["muted"])
        if i < len(tiers) - 1:
            s.arrow(x + 400, yy + 88, x + 400, yy + 112, sw=1.6)
    s.pill(455, 642, 290, 42, "highest viable backend wins", COLORS["slate"], COLORS["slate2"])
    s.save(OUTPUT / "diagrams/backend_ladder.svg")


def diagram_logos_control_loop() -> None:
    s = SVG("Neural / symbolic control loop", "Keep the loop legible: signals move, constraints return")
    s.card(85, 175, 420, 350, "Neural stack", "training and inference path", COLORS["blue"])
    for i, text in enumerate(["forward pass", "loss computation", "backward pass", "weight update"]):
        s.pill(140, 285 + i * 54, 235, 34, text, COLORS["blue"], COLORS["blue2"])
    s.card(695, 175, 420, 350, "Logos bridge", "symbolic validation and constraint layer", COLORS["green"])
    for i, text in enumerate(["contradiction checks", "axiom-guided penalties", "guarded evolution", "constraint validation"]):
        s.pill(750, 285 + i * 54, 250, 34, text, COLORS["green"], COLORS["green2"])
    s.arrow(518, 320, 680, 320, COLORS["muted"], 2.4)
    s.arrow(680, 430, 518, 430, COLORS["muted"], 2.4)
    s.text(600, 298, "outputs / traces", 14, 650, COLORS["muted"], anchor="middle")
    s.text(600, 468, "penalties / constraints", 14, 650, COLORS["muted"], anchor="middle")
    s.circle(600, 375, 45, COLORS["panel"], COLORS["line"], 1.5)
    s.text(600, 368, "review", 16, 700, COLORS["text"], anchor="middle")
    s.text(600, 390, "gate", 14, 500, COLORS["muted"], anchor="middle")
    s.save(OUTPUT / "diagrams/logos_control_loop.svg")


def diagram_hardware_constraint() -> None:
    s = SVG("Hardware constraint context", "Make limitations look intentional and honest, not like excuses")
    cards = [
        ("GPU", "RTX 2070 Super mobile\n8 GB VRAM hard limit", COLORS["red"], COLORS["red2"]),
        ("VRAM", "batch size and cache ceiling\nshape the benchmark envelope", COLORS["amber"], COLORS["amber2"]),
        ("Thermals", "laptop cooling constrains\nsustained compute windows", COLORS["amber"], COLORS["amber2"]),
        ("CPU", "i7-10750H\n6 cores / 12 threads", COLORS["blue"], COLORS["blue2"]),
        ("RAM", "32 GB\nsufficient for lab workflow", COLORS["green"], COLORS["green2"]),
    ]
    x0, y, w, gap = 70, 190, 204, 22
    for i, (title, desc, accent, fill) in enumerate(cards):
        x = x0 + i * (w + gap)
        s.rect(x, y, w, 315, rx=24, fill=COLORS["panel"], stroke=COLORS["line"], filter_id="shadow")
        s.circle(x + w / 2, y + 72, 50, fill, accent, 1.6)
        s.text(x + w / 2, y + 81, title, 22, 800, accent, anchor="middle")
        s.multiline(x + w / 2, y + 165, desc, 15, 22, 500, COLORS["text"], anchor="middle", max_chars=23)
    s.text(600, 575, "Context is part of the evidence: public claims should be scoped to the actual machine.", 17, 500, COLORS["muted"], anchor="middle")
    s.save(OUTPUT / "diagrams/hardware_constraint_panel.svg")


def diagram_autograd_mamba_flow() -> None:
    s = SVG("Autograd + Mamba training flow", "Forward path, loss, and backward signal in one clean horizontal trace")
    nodes = [
        ("Input tokens", 120, COLORS["slate"], COLORS["slate2"]),
        ("Embedding", 300, COLORS["blue"], COLORS["blue2"]),
        ("Mamba SSM layer", 500, COLORS["violet"], COLORS["violet2"]),
        ("Output projection", 720, COLORS["amber"], COLORS["amber2"]),
        ("Cross-entropy loss", 930, COLORS["red"], COLORS["red2"]),
    ]
    y, w, h = 330, 150, 82
    for i, (label, x, accent, fill) in enumerate(nodes):
        s.rect(x, y, w, h, rx=22, fill=fill, stroke=accent, sw=1.8)
        s.multiline(x + w / 2, y + 38, label, 16, 20, 720, COLORS["text"], anchor="middle", max_chars=16)
        if i < len(nodes) - 1:
            s.arrow(x + w + 12, y + h / 2, nodes[i + 1][1] - 14, y + h / 2, sw=2.1)
    s.parts.append(f'<path d="M 970 455 C 800 590, 430 590, 310 455" fill="none" stroke="{COLORS["green"]}" stroke-width="2.4" stroke-dasharray="10 8" marker-end="url(#arrow)"/>')
    s.text(640, 612, "gradient signal returns through the computation graph", 15, 650, COLORS["green"], anchor="middle")
    s.pill(475, 200, 250, 42, "public-safe training trace", COLORS["violet"], COLORS["violet2"])
    s.save(OUTPUT / "diagrams/autograd_mamba_flow.svg")


def diagram_benchmark_timeline() -> None:
    s = SVG("Benchmark correction timeline", "Show the story: baseline → anomaly → diagnosis → stable result")
    events = [
        (130, "task-87", "~2000 tok/s", COLORS["slate"]),
        (340, "Phase 20 pre-fix", "~7676 tok/s anomaly", COLORS["red"]),
        (560, "Leak found", "VRAM overflow diagnosis", COLORS["amber"]),
        (780, "Safety fuse", "guarded execution", COLORS["amber"]),
        (1010, "Phase 20 post-fix", "~5659 tok/s stable", COLORS["green"]),
    ]
    y = 360
    s.parts.append(f'<line x1="130" y1="{y}" x2="1010" y2="{y}" stroke="{COLORS["line"]}" stroke-width="8" stroke-linecap="round"/>')
    for x, title, desc, color in events:
        s.circle(x, y, 24, COLORS["panel"], color, 4)
        s.circle(x, y, 11, color, color, 1)
        s.text(x, y - 68, title, 18, 760, color, anchor="middle")
        s.multiline(x, y + 58, desc, 14, 18, 450, COLORS["muted"], anchor="middle", max_chars=20)
    s.pill(458, 555, 285, 42, "correction is part of credibility", COLORS["blue"], COLORS["blue2"])
    s.save(OUTPUT / "diagrams/benchmark_timeline.svg")


def bar_chart(
    title: str,
    subtitle: str,
    filename: str,
    labels: list[str],
    values: list[float],
    colors: list[str],
    unit: str = "",
    note: str | None = None,
    y_max: float | None = None,
    log: bool = False,
) -> None:
    s = SVG(title, subtitle)
    left, bottom, top, chart_w, chart_h = 130, 590, 160, 900, 390
    if log:
        y_min = 0.000001 if max(values) < 0.01 else 1
        y_max = y_max or max(values) * 1.4
        ticks = [0.000001, 0.00001, 0.0001, 0.001] if y_min < 0.01 else [1, 10, 100, 1000, 3000]
        def yscale(v: float) -> float:
            return bottom - ((math.log10(max(v, y_min)) - math.log10(y_min)) / (math.log10(y_max) - math.log10(y_min)) * chart_h)
        for tick in ticks:
            if tick > y_max * 1.001 or tick < y_min:
                continue
            yy = yscale(tick)
            s.parts.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{left + chart_w}" y2="{yy:.1f}" stroke="{COLORS["line2"]}" stroke-width="1"/>')
            s.text(left - 18, yy + 5, f"{tick:g}{unit}", 12, 500, COLORS["muted"], anchor="end")
    else:
        y_max = y_max or max(values) * 1.18
        def yscale(v: float) -> float:
            return bottom - (v / y_max * chart_h)
        for k in range(1, 5):
            yy = bottom - k * chart_h / 5
            s.parts.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{left + chart_w}" y2="{yy:.1f}" stroke="{COLORS["line2"]}" stroke-width="1"/>')
            val = y_max * k / 5
            label = f"{val:.0f}{unit}" if val >= 10 else f"{val:g}{unit}"
            s.text(left - 18, yy + 5, label, 12, 500, COLORS["muted"], anchor="end")

    s.parts.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{COLORS["line"]}" stroke-width="2"/>')
    s.parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left + chart_w}" y2="{bottom}" stroke="{COLORS["line"]}" stroke-width="2"/>')

    n = len(values)
    bar_w = min(105, chart_w / (n * 1.8))
    for i, (label, value, color) in enumerate(zip(labels, values, colors)):
        x = left + (i + 0.65) * chart_w / n - bar_w / 2
        y = yscale(value)
        h = bottom - y
        s.rect(x, y, bar_w, h, rx=12, fill=color, stroke=color, sw=0)
        s.text(x + bar_w / 2, y - 12, f"{value:g}{unit}", 14, 760, COLORS["text"], anchor="middle")
        s.multiline(x + bar_w / 2, bottom + 34, label, 13, 16, 520, COLORS["muted"], anchor="middle", max_chars=15)

    if note:
        s.rect(720, 120, 345, 86, rx=18, fill=COLORS["panel"], stroke=COLORS["line"], filter_id="shadow")
        s.multiline(742, 155, note, 14, 19, 500, COLORS["muted"], max_chars=40)

    s.save(OUTPUT / "plots" / filename)


def plot_throughput_comparison() -> None:
    bar_chart(
        "Throughput comparison",
        "Sustained result, peak micro-benchmark, and historical reference",
        "throughput_comparison.svg",
        ["Sustained\nBatch 8", "Peak micro\nBatch 320", "Phase 20\npost-fix"],
        [6802, 18172, 5659],
        [COLORS["green"], COLORS["violet"], COLORS["amber"]],
        " tok/s",
        "TinyStories BPE · 2-layer Mamba LM · RTX 2070 Super 8 GB",
        y_max=23000,
    )


def plot_h2d_traffic_reduction() -> None:
    bar_chart(
        "H2D traffic reduction",
        "Host-to-device traffic, log-scaled for readable comparison",
        "h2d_traffic_reduction.svg",
        ["Baseline\ntask-87", "Phase 20\npost-fix", "TinyStories\nsustained", "TinyStories\npeak"],
        [2048, 16, 5.2, 407.9],
        [COLORS["red"], COLORS["green"], COLORS["blue"], COLORS["violet"]],
        " MB",
        "The plot emphasizes order-of-magnitude behavior, not decorative drama.",
        y_max=3000,
        log=True,
    )


def plot_vram_usage() -> None:
    bar_chart(
        "VRAM usage envelope",
        "Sustained training leaves headroom; peak benchmark consumes the cache envelope",
        "vram_usage.svg",
        ["Sustained\nweights", "Sustained\nactive+pool", "Sustained\nfree", "Peak\nactive+pool", "Peak\nfree"],
        [0.05, 1.15, 6.8, 7.45, 0.5],
        [COLORS["green"], COLORS["blue"], COLORS["slate"], COLORS["amber"], COLORS["red"]],
        " GB",
        "Public framing: 8 GB is a hard experimental constraint.",
        y_max=8.8,
    )


def plot_int8_validation() -> None:
    bar_chart(
        "INT8 validation",
        "Measured numerical error is plotted against declared tolerances",
        "int8_validation.svg",
        ["MatMul", "GPU dispatch", "GPU/CPU parity", "Serialization", "Stress"],
        [0.000013, 0.000035, 0.000495, 0.000002, 0.000220],
        [COLORS["blue"], COLORS["blue"], COLORS["amber"], COLORS["green"], COLORS["violet"]],
        "",
        "Use source tables nearby; keep the chart as a visual summary.",
        y_max=0.001,
        log=True,
    )


def plot_stability_throughput() -> None:
    s = SVG("Training stability and throughput", "Separate historical correction from current benchmark result")
    labels = ["task-87\nbaseline", "Phase 20\npre-fix", "Phase 20\npost-fix", "AMP v2", "Sustained\ncurrent", "Peak\nmicro"]
    values = [2000, 7676, 5659, 5753, 6802, 18172]
    colors = [COLORS["slate"], COLORS["red"], COLORS["green"], COLORS["green"], COLORS["blue"], COLORS["violet"]]
    left, bottom, cw, ch, y_max = 120, 590, 940, 370, 21000
    for k in range(0, 6):
        yy = bottom - k * ch / 5
        s.parts.append(f'<line x1="{left}" y1="{yy:.1f}" x2="{left + cw}" y2="{yy:.1f}" stroke="{COLORS["line2"]}" stroke-width="1"/>')
        if k > 0:
            s.text(left - 20, yy + 5, f"{int(y_max * k / 5 / 1000)}k", 12, 500, COLORS["muted"], anchor="end")
    s.parts.append(f'<line x1="{left}" y1="{bottom}" x2="{left + cw}" y2="{bottom}" stroke="{COLORS["line"]}" stroke-width="2"/>')
    for i, (label, value, color) in enumerate(zip(labels, values, colors)):
        bw, x = 88, left + 45 + i * 150
        h = value / y_max * ch
        y = bottom - h
        s.rect(x, y, bw, h, rx=12, fill=color, stroke=color, sw=0)
        s.text(x + bw / 2, y - 10, f"{value}", 13, 760, COLORS["text"], anchor="middle")
        s.multiline(x + bw / 2, bottom + 34, label, 13, 16, 520, COLORS["muted"], anchor="middle", max_chars=12)
    s.parts.append(f'<line x1="{left + 620}" y1="170" x2="{left + 620}" y2="640" stroke="{COLORS["line"]}" stroke-width="1.5" stroke-dasharray="8 8"/>')
    s.text(left + 300, 160, "historical correction", 14, 700, COLORS["muted"], anchor="middle")
    s.text(left + 770, 160, "current result", 14, 700, COLORS["muted"], anchor="middle")
    s.save(OUTPUT / "plots/stability_throughput.svg")


def main() -> None:
    diagram_project_boundary()
    diagram_public_private()
    diagram_layered_architecture()
    diagram_backend_ladder()
    diagram_logos_control_loop()
    diagram_hardware_constraint()
    diagram_autograd_mamba_flow()
    diagram_benchmark_timeline()
    plot_throughput_comparison()
    plot_h2d_traffic_reduction()
    plot_vram_usage()
    plot_int8_validation()
    plot_stability_throughput()


if __name__ == "__main__":
    main()

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT

OUTPUT = "/Users/usman.sindhu/Dynatrace-pmm-os-main/docs/dynatrace-vs-datadog-differentiators.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1*inch,
    rightMargin=1*inch,
    topMargin=1*inch,
    bottomMargin=1*inch,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "Title",
    fontSize=18,
    fontName="Helvetica-Bold",
    textColor=colors.HexColor("#1a1a2e"),
    spaceAfter=4,
)
subtitle_style = ParagraphStyle(
    "Subtitle",
    fontSize=11,
    fontName="Helvetica",
    textColor=colors.HexColor("#555555"),
    spaceAfter=20,
)
number_style = ParagraphStyle(
    "Number",
    fontSize=28,
    fontName="Helvetica-Bold",
    textColor=colors.HexColor("#0066cc"),
    spaceAfter=0,
    leading=32,
)
heading_style = ParagraphStyle(
    "Heading",
    fontSize=13,
    fontName="Helvetica-Bold",
    textColor=colors.HexColor("#1a1a2e"),
    spaceAfter=6,
    leading=18,
)
body_style = ParagraphStyle(
    "Body",
    fontSize=10,
    fontName="Helvetica",
    textColor=colors.HexColor("#333333"),
    spaceAfter=6,
    leading=15,
)
source_style = ParagraphStyle(
    "Source",
    fontSize=8,
    fontName="Helvetica-Oblique",
    textColor=colors.HexColor("#888888"),
    spaceAfter=0,
    leading=12,
)
caveat_style = ParagraphStyle(
    "Caveat",
    fontSize=9,
    fontName="Helvetica-Oblique",
    textColor=colors.HexColor("#cc6600"),
    spaceAfter=0,
    leading=13,
)
footer_style = ParagraphStyle(
    "Footer",
    fontSize=8,
    fontName="Helvetica",
    textColor=colors.HexColor("#aaaaaa"),
    spaceAfter=0,
)

differentiators = [
    {
        "n": "1",
        "heading": "Seven layers, not just the agent trace",
        "body": (
            "Dynatrace traces from the GPU and vector store up through the orchestration "
            "chain, the agent, and all the way to business impact — in one view. Datadog's "
            "story centers on the agent trace and tool decisions. If a bad response traces "
            "back to a retrieval failure or a cost spike on the infra side, Datadog puts "
            "that in a different place. Dynatrace puts it on the same problem card."
        ),
        "source": "corpus/product-truth.md, verified 2026-09-15 · corpus/competitors/datadog.md, verified 2026-08-28",
    },
    {
        "n": "2",
        "heading": "Your production traffic is your eval dataset",
        "body": (
            "dt-evals samples live GenAI spans, runs a judge LLM of your choice across "
            "15 built-in evaluators, and writes scores back to the same trace — no separate "
            "eval pipeline. You can gate deploys on quality regression the same way you gate "
            "on latency. Datadog has offline experimentation and dataset versioning, but it's "
            "a separate workflow from production monitoring."
        ),
        "source": "corpus/product-truth.md, verified 2026-09-15",
        "caveat": "Honest gap: Datadog is ahead on the pre-production developer loop today (golden datasets, human annotation, offline experiments). dt-evals closes the production side.",
    },
    {
        "n": "3",
        "heading": "Causal root cause, not correlation",
        "body": (
            "Davis AI uses deterministic, causal analysis — topology context from Smartscape "
            "— to tell you why something broke, not just that it did. When an AI app degrades, "
            "it reasons across the full dependency graph to pinpoint the cause. Datadog surfaces "
            "outliers and patterns; it does not claim causal, deterministic root cause."
        ),
        "source": "corpus/product-truth.md, verified 2026-09-15 · corpus/competitors/datadog.md, verified 2026-08-28",
    },
]

story = []

story.append(Paragraph("Dynatrace vs. Datadog", title_style))
story.append(Paragraph("Three differentiators for AI engineers · September 2026", subtitle_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0066cc"), spaceAfter=24))

for d in differentiators:
    story.append(Paragraph(d["n"], number_style))
    story.append(Paragraph(d["heading"], heading_style))
    story.append(Paragraph(d["body"], body_style))
    if d.get("caveat"):
        story.append(Spacer(1, 4))
        story.append(Paragraph("Honest gap: " + d["caveat"].replace("Honest gap: ", ""), caveat_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Source: " + d["source"], source_style))
    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#dddddd"), spaceAfter=20))

story.append(Spacer(1, 8))
story.append(Paragraph(
    "All claims grounded in corpus/ only. Audience: AI engineers / developers. "
    "Grounding verified 2026-09-15.",
    footer_style,
))

doc.build(story)
print(f"PDF written to {OUTPUT}")

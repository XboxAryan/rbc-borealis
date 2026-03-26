"""Generate proposal DOCX matching the RBC Borealis sample PDF style."""

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "proposal-v1.docx")

# Colors from the sample PDF
NAVY_BLUE = RGBColor(0x00, 0x31, 0x68)  # RBC Borealis brand navy
DARK_TEXT = RGBColor(0x1A, 0x1A, 0x2E)  # Near-black for title
HEADING_GRAY = RGBColor(0x44, 0x44, 0x44)  # Section headings
BODY_COLOR = RGBColor(0x33, 0x33, 0x33)  # Body text
LINK_BLUE = RGBColor(0x05, 0x63, 0xC1)  # Hyperlink blue
FOOTER_GRAY = RGBColor(0x88, 0x88, 0x88)  # Footer text


def set_character_spacing(run, spacing_pts):
    """Set character spacing (letter-spacing) on a run in half-points."""
    rPr = run._r.get_or_add_rPr()
    spacing = OxmlElement("w:spacing")
    spacing.set(qn("w:val"), str(int(spacing_pts * 20)))  # twips
    rPr.append(spacing)


def add_header_footer(doc):
    """Add RBC BOREALIS header and page-numbered footer to every page."""
    for section in doc.sections:
        # --- Header ---
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        hp.paragraph_format.space_after = Pt(4)
        run = hp.add_run("RBC BOREALIS")
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = "Calibri"
        run.font.color.rgb = NAVY_BLUE
        set_character_spacing(run, 2)

        # --- Footer ---
        footer = section.footer
        footer.is_linked_to_previous = False

        # Use a table for left-aligned text + right-aligned page number
        ftbl = footer.add_table(1, 2, width=Inches(6.5))
        ftbl.autofit = True
        # Remove table borders
        tbl = ftbl._tbl
        tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
        borders = OxmlElement("w:tblBorders")
        for border_name in ("top", "left", "bottom", "right", "insideH", "insideV"):
            border = OxmlElement(f"w:{border_name}")
            border.set(qn("w:val"), "none")
            border.set(qn("w:sz"), "0")
            border.set(qn("w:space"), "0")
            border.set(qn("w:color"), "auto")
            borders.append(border)
        tblPr.append(borders)

        # Left cell: "RBC Borealis"
        left_cell = ftbl.cell(0, 0)
        left_p = left_cell.paragraphs[0]
        left_p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        left_run = left_p.add_run("RBC Borealis")
        left_run.font.size = Pt(8)
        left_run.font.name = "Calibri"
        left_run.font.color.rgb = FOOTER_GRAY

        # Right cell: page number
        right_cell = ftbl.cell(0, 1)
        right_p = right_cell.paragraphs[0]
        right_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        fld_char_begin = OxmlElement("w:fldChar")
        fld_char_begin.set(qn("w:fldCharType"), "begin")
        instr_text = OxmlElement("w:instrText")
        instr_text.set(qn("xml:space"), "preserve")
        instr_text.text = " PAGE "
        fld_char_end = OxmlElement("w:fldChar")
        fld_char_end.set(qn("w:fldCharType"), "end")

        run_pg = right_p.add_run()
        run_pg.font.size = Pt(8)
        run_pg.font.name = "Calibri"
        run_pg.font.color.rgb = FOOTER_GRAY
        run_pg._r.append(fld_char_begin)
        run_pg2 = right_p.add_run()
        run_pg2.font.size = Pt(8)
        run_pg2.font.name = "Calibri"
        run_pg2.font.color.rgb = FOOTER_GRAY
        run_pg2._r.append(instr_text)
        run_pg3 = right_p.add_run()
        run_pg3.font.size = Pt(8)
        run_pg3.font.name = "Calibri"
        run_pg3.font.color.rgb = FOOTER_GRAY
        run_pg3._r.append(fld_char_end)


def add_hyperlink(paragraph, url, text):
    """Add a clickable hyperlink to a paragraph."""
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    for tag, attr, val in [
        ("w:color", "w:val", "0563C1"),
        ("w:u", "w:val", "single"),
    ]:
        el = OxmlElement(tag)
        el.set(qn(attr), val)
        rPr.append(el)
    rFonts = OxmlElement("w:rFonts")
    rFonts.set(qn("w:ascii"), "Calibri")
    rFonts.set(qn("w:hAnsi"), "Calibri")
    rPr.append(rFonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "22")
    rPr.append(sz)
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_section_heading(doc, text):
    """Add a section heading matching the sample PDF: light weight, gray, ~16pt."""
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.space_before = Pt(18)
    fmt.space_after = Pt(8)
    fmt.line_spacing = 1.3
    run = p.add_run(text)
    run.bold = False
    run.font.size = Pt(16)
    run.font.name = "Calibri Light"
    run.font.color.rgb = HEADING_GRAY


def add_body(doc, text):
    """Add a body paragraph matching the sample PDF style."""
    p = doc.add_paragraph(text)
    fmt = p.paragraph_format
    fmt.line_spacing = 1.3
    fmt.space_after = Pt(8)
    for run in p.runs:
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.color.rgb = BODY_COLOR
    return p


def add_body_with_bold(doc, segments):
    """Add paragraph with mixed bold/normal text. segments = [(text, bold), ...]"""
    p = doc.add_paragraph()
    fmt = p.paragraph_format
    fmt.line_spacing = 1.3
    fmt.space_after = Pt(8)
    for text, bold in segments:
        run = p.add_run(text)
        run.bold = bold
        run.font.name = "Calibri"
        run.font.size = Pt(11)
        run.font.color.rgb = BODY_COLOR
    return p


def build_document():
    doc = Document()

    # Set default style
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = BODY_COLOR
    style.paragraph_format.line_spacing = 1.3

    # Margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Header and footer
    add_header_footer(doc)

    # ═══════════════════════════════════════════════
    # TITLE (large, light weight, left-aligned — matching sample PDF)
    # ═══════════════════════════════════════════════
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    fmt = title.paragraph_format
    fmt.space_before = Pt(12)
    fmt.space_after = Pt(24)
    fmt.line_spacing = 1.1

    run = title.add_run(
        "Project Proposal \u2013 Societal\nImpact Modeling for AI Data\nCenter Siting in Canada"
    )
    run.bold = False
    run.font.size = Pt(28)
    run.font.name = "Calibri Light"
    run.font.color.rgb = DARK_TEXT

    # ═══════════════════════════════════════════════
    # SECTION 1: The Problem
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "What is the problem?")

    add_body(
        doc,
        "AI data centers are expanding rapidly across Canada. The country currently hosts "
        "10.3 GW of data center capacity, with an additional 9 GW in the development "
        "pipeline \u2014 nearly doubling the installed base within the next few years. These "
        "facilities consume enormous amounts of electricity and water, and their environmental "
        "impact varies dramatically depending on where they are built.",
    )

    add_body(
        doc,
        "A 100 MW data center in Alberta produces approximately 430,000 tonnes of CO\u2082 "
        "per year under standard grid-average accounting, while the same facility in Quebec "
        "produces roughly 1,500 tonnes \u2014 a 286-fold difference. But this comparison "
        "understates the real complexity. Research in the Journal of Industrial Ecology "
        "(Dandres et al. 2016) shows that the marginal electricity actually serving new "
        "data center loads in Canada is dominated by natural gas and coal, with a GHG "
        "intensity of 0.85\u20131.01 kg CO\u2082-eq/kWh \u2014 roughly 5x higher than the "
        "Canadian average. Worse, 60\u201370% of this marginal electricity comes from reduced "
        "exports to the United States, triggering compensating fossil fuel generation south "
        "of the border. Even siting in \u201cclean\u201d provinces has significant carbon "
        "consequences that standard accounting misses entirely.",
    )

    add_body(
        doc,
        "Yet no publicly available tool exists to help policymakers evaluate these "
        "tradeoffs \u2014 including the hidden marginal and cross-border effects \u2014 before "
        "a siting decision is made. This gap is becoming urgent. In December 2025, Ontario "
        "passed Bill 40, the first Canadian law requiring ministerial approval for data "
        "center grid connections \u2014 a signal that governments are actively seeking "
        "analytical frameworks for these decisions. Meanwhile, data center siting choices "
        "lock in 20 to 30 years of environmental consequences. The decisions being made "
        "today will shape Canada\u2019s carbon and water footprint for decades.",
    )

    add_body(
        doc,
        "We propose building the first open-source Societal Impact Score for AI data center "
        "siting in Canada: a composite metric that evaluates carbon emissions, water "
        "consumption, grid stress, and cooling efficiency for any proposed location, with "
        "uncertainty quantification to support honest, evidence-based decision-making.",
    )

    # ═══════════════════════════════════════════════
    # SECTION 2: Why it matters
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "Why does this matter to our team?")

    add_body(
        doc,
        "As computer science students, we use AI tools every day \u2014 ChatGPT, GitHub "
        "Copilot, cloud computing platforms. These tools depend on massive data center "
        "infrastructure, but the environmental cost of that infrastructure is rarely visible "
        "to the people who use it. We want to make that cost visible and measurable.",
    )

    add_body(
        doc,
        "Our team has a shared interest in sustainability and climate technology. We believe "
        "that machine learning should not only be applied to commercial problems but also to "
        "the environmental challenges that AI itself creates. Canada is uniquely positioned "
        "for this work because its federated electricity system produces a 200-fold variation "
        "in carbon intensity across provinces \u2014 meaning that where a data center is built "
        "matters far more than how efficiently it operates.",
    )

    add_body(
        doc,
        "With 9 GW of new capacity in the pipeline and siting decisions being made in our "
        "own communities, this is not an abstract policy question. It is happening now, and "
        "we want to contribute a tool that helps communities and policymakers make informed "
        "choices.",
    )

    # ═══════════════════════════════════════════════
    # SECTION 3: Why ML
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "Why can machine learning help?")

    add_body(
        doc,
        "The environmental impact of a data center depends on complex, nonlinear "
        "interactions between grid conditions, climate, water availability, and facility "
        "design. Machine learning is well suited to capturing these relationships.",
    )

    add_body(doc, "Our approach involves four sub-models, each addressing a distinct prediction task:")

    add_body_with_bold(
        doc,
        [
            ("1. Grid stress prediction: ", True),
            (
                "A classification model trained on hourly electricity demand and reserve "
                "margin data to estimate whether adding a data center\u2019s load would push "
                "a provincial grid toward reliability limits.",
                False,
            ),
        ],
    )
    add_body_with_bold(
        doc,
        [
            ("2. Carbon intensity forecasting: ", True),
            (
                "A time-series model forecasting both average and marginal carbon intensity "
                "of electricity at a given location. Marginal intensity \u2014 the carbon cost "
                "of the next unit of generation dispatched \u2014 is typically 2\u20135x higher "
                "than the grid average in mixed-source provinces (Dandres et al. 2016), and "
                "is the methodologically appropriate metric for evaluating new loads.",
                False,
            ),
        ],
    )
    add_body_with_bold(
        doc,
        [
            ("3. Cooling efficiency regression: ", True),
            (
                "A regression model predicting Power Usage Effectiveness (PUE) \u2014 the "
                "energy overhead from cooling \u2014 based on local climate variables such as "
                "temperature and humidity.",
                False,
            ),
        ],
    )
    add_body_with_bold(
        doc,
        [
            ("4. Water intensity estimation: ", True),
            (
                "A physics-based model estimating water consumption from cooling systems, "
                "weighted by local water stress indices.",
                False,
            ),
        ],
    )

    add_body(
        doc,
        "These four outputs are combined into a single Societal Impact Score using "
        "configurable weights. Monte Carlo simulation propagates uncertainty from each "
        "sub-model through the composite score, producing confidence intervals rather than "
        "misleading point estimates.",
    )

    # ═══════════════════════════════════════════════
    # SECTION 4: Datasets
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "What data do we plan to use?")

    add_body(doc, "We have identified three primary open datasets:")

    # Dataset 1
    p1 = add_body_with_bold(
        doc,
        [
            (
                "1. Environment and Climate Change Canada (ECCC) \u2014 Provincial "
                "Emission Factors\n",
                True,
            ),
            (
                "Official government emission intensities (gCO\u2082e/kWh) for every Canadian "
                "province and territory. These serve as the ground truth for our carbon "
                "intensity model.\n(",
                False,
            ),
        ],
    )
    add_hyperlink(
        p1,
        "https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html",
        "canada.ca/emission-factors",
    )
    p1.add_run(")").font.size = Pt(11)

    # Dataset 2
    p2 = add_body_with_bold(
        doc,
        [
            (
                "2. Independent Electricity System Operator (IESO) \u2014 Ontario Hourly "
                "Generation Data\n",
                True,
            ),
            (
                "Hourly generation by fuel type (nuclear, hydro, gas, wind, solar), system "
                "demand, and market pricing. Available as CSV downloads and via the "
                "open-source gridstatus Python library.\n(",
                False,
            ),
        ],
    )
    add_hyperlink(p2, "https://www.ieso.ca/power-data/data-directory", "ieso.ca/power-data")
    p2.add_run(")").font.size = Pt(11)

    # Dataset 3
    p3 = add_body_with_bold(
        doc,
        [
            (
                "3. World Resources Institute (WRI) \u2014 Aqueduct 4.0 Water Risk Atlas\n",
                True,
            ),
            (
                "Sub-basin water stress indices covering all of Canada, including baseline "
                "water stress, seasonal variability, and drought risk. Licensed under "
                "Creative Commons Attribution 4.0.\n(",
                False,
            ),
        ],
    )
    add_hyperlink(
        p3,
        "https://www.wri.org/applications/aqueduct/water-risk-atlas/",
        "wri.org/aqueduct",
    )
    p3.add_run(")").font.size = Pt(11)

    add_body(
        doc,
        "We also draw on the methodological findings of Dandres et al. (2016), published "
        "in the Journal of Industrial Ecology, which established that marginal generation "
        "in Canada is 85\u2013100% fossil-fueled and identified cross-border electricity trade "
        "as a critical factor in consequential carbon accounting for new large loads.",
    )

    # ═══════════════════════════════════════════════
    # SECTION 5: Coursework
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "Does this project relate to coursework?")

    add_body(
        doc,
        "This project is purely extracurricular. It does not fulfill any coursework "
        "requirement. It is driven by our shared interest in applying machine learning to "
        "sustainability challenges.",
    )

    # ═══════════════════════════════════════════════
    # SECTION 6: Willingness to pivot
    # ═══════════════════════════════════════════════
    add_section_heading(doc, "Willingness to pivot")

    add_body(
        doc,
        "Our team is fully open to pivoting to an alternative community project if selected "
        "and our mentor recommends a different direction. We are here to learn and to "
        "contribute, and we trust the mentorship process.",
    )

    doc.save(OUTPUT_PATH)
    print(f"Saved: {OUTPUT_PATH}")

    # Word count
    total_words = sum(len(p.text.split()) for p in doc.paragraphs if p.text.strip())
    print(f"Approximate word count: {total_words}")


if __name__ == "__main__":
    build_document()

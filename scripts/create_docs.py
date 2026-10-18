import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def create_docx():
    doc = docx.Document()

    # Page margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Palette
    c_dark = RGBColor(0x1B, 0x10, 0x30)
    c_card = RGBColor(0x2A, 0x1A, 0x4A)
    c_orange = RGBColor(0xFF, 0x8A, 0x3D)
    c_lilac = RGBColor(0xB7, 0x9C, 0xFF)
    c_text = RGBColor(0x33, 0x33, 0x33)
    c_muted = RGBColor(0x66, 0x66, 0x66)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = c_text

    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(4)
    run_title = p_title.add_run("GitHub Profile README Documentation")
    run_title.font.name = 'Arial'
    run_title.font.size = Pt(26)
    run_title.font.bold = True
    run_title.font.color.rgb = c_dark

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(20)
    run_sub = p_sub.add_run("Pixel-Perfect Gamified Architecture for @HARIPRASATH2611")
    run_sub.font.name = 'Arial'
    run_sub.font.size = Pt(14)
    run_sub.font.color.rgb = c_orange

    # Divider line
    p_div = doc.add_paragraph()
    p_div.paragraph_format.space_after = Pt(20)
    run_div = p_div.add_run("―" * 55)
    run_div.font.color.rgb = c_lilac

    # 1. Project Overview
    h1 = doc.add_heading(level=1)
    r1 = h1.add_run("1. Project Overview & Architecture")
    r1.font.name = 'Arial'
    r1.font.color.rgb = c_dark

    doc.add_paragraph(
        "This repository contains the GitHub profile README for @HARIPRASATH2611, built as a "
        "bespoke, gamified UI matching modern dark-mode gaming aesthetics. Due to GitHub's markdown security limits "
        "(which strip <style>, <script>, custom fonts, and external CSS), the entire visual interface is implemented "
        "as a unified, self-contained SVG asset with embedded typography, base64 imagery, and living vector animations."
    )

    doc.add_paragraph(
        "By packaging the profile into assets/profile-animated.svg, the design guarantees exact 24–28px card spacing "
        "without unwanted markdown paragraph margins (<p> spacing artifacts) and delivers smooth 60fps animations across all browsers."
    )

    # Repository Structure Table
    p_tbl_lbl = doc.add_paragraph()
    r_tbl_lbl = p_tbl_lbl.add_run("Repository Structure:")
    r_tbl_lbl.font.bold = True

    table = doc.add_table(rows=6, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ["Path", "Type", "Description"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        set_cell_background(cell, "2A1A4A")
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(h)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xF6, 0xF1, 0xFF)

    files_data = [
        ("/README.md", "Markdown", "Root profile document rendered on GitHub profile page"),
        ("/assets/profile-animated.svg", "SVG", "Unified animated profile banner with embedded fonts and SMIL animations"),
        ("/assets/profile.png", "Image", "Original, untouched profile photo"),
        ("/build_full_svg.py", "Python", "Master build script that generates the unified profile SVG"),
        ("/.github/workflows/snake.yml", "YAML", "GitHub Actions scheduled workflow for contribution grid animation")
    ]

    for row_idx, row in enumerate(files_data, start=1):
        bg = "F7F4FD" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            run = p.add_run(text)
            if col_idx == 0:
                run.font.name = 'Consolas'
                run.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    # 2. Design System
    h2 = doc.add_heading(level=1)
    r2 = h2.add_run("2. Design System & Design Tokens")
    r2.font.name = 'Arial'
    r2.font.color.rgb = c_dark

    doc.add_paragraph("The visual design adheres strictly to a curated dark gamified color palette:")

    palette_table = doc.add_table(rows=6, cols=3)
    palette_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    p_headers = ["Token Name", "Hex Code", "Usage in UI"]
    for i, h in enumerate(p_headers):
        cell = palette_table.cell(0, i)
        set_cell_background(cell, "2A1A4A")
        p = cell.paragraphs[0]
        run = p.add_run(h)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xF6, 0xF1, 0xFF)

    palette_data = [
        ("Background", "#1B1030", "Deep eggplant canvas background & chip fills"),
        ("Card Surface", "#2A1A4A", "Card container surface background"),
        ("Accent Orange", "#FF8A3D", "Hero photo card bottom banner, active nodes, status dot, snake head"),
        ("Accent Lilac", "#B79CFF", "Main Quest badge, footer card background, labels"),
        ("Text Primary", "#F6F1FF", "Headings, titles, chip text, contrast text")
    ]

    for row_idx, row in enumerate(palette_data, start=1):
        bg = "F7F4FD" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row):
            cell = palette_table.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            run = p.add_run(text)
            if col_idx == 1:
                run.font.name = 'Consolas'
                run.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    # Contribution Heatmap Tokens
    p_heat = doc.add_paragraph()
    r_heat = p_heat.add_run("Contribution Heatmap Levels:")
    r_heat.font.bold = True

    heat_items = [
        ("Level 0 (#34225A):", " Empty days / background grid nodes"),
        ("Level 1 (#6E4FB5):", " 1–3 contributions per day (muted violet)"),
        ("Level 2 (#B79CFF):", " 4–6 contributions per day (bright lilac)"),
        ("Level 3 (#FFB27A):", " 7–9 contributions per day (warm peach)"),
        ("Level 4 (#FF8A3D):", " 10+ contributions per day (vibrant orange)")
    ]
    for prefix, body in heat_items:
        p = doc.add_paragraph(style='List Bullet')
        r_p = p.add_run(prefix)
        r_p.font.bold = True
        p.add_run(body)

    # 3. Typography Stack & Font Hardening
    h3 = doc.add_heading(level=1)
    r3 = h3.add_run("3. Typography & Offline Font Hardening")
    r3.font.name = 'Arial'
    r3.font.color.rgb = c_dark

    doc.add_paragraph(
        "To prevent GitHub's Camo image cache proxy from blocking external Google Fonts, the latin WOFF2 subsets "
        "for the typography stack are directly converted to Base64 strings and embedded inside the SVG's <style> block:"
    )

    typo_items = [
        ("Syne 800 (Extra Bold):", " Geometric display typeface used for 'Hariprasath', 'Full stack developer', 'MAIN QUEST', 'Inventory', 'Commit log', and 'Join my party'."),
        ("DM Sans 400/500:", " Clean modern sans-serif used for the 3-line bio, Main Quest objective description, and commit log entries."),
        ("Space Mono 400/700:", " Technical monospace typeface used for 'PLAYER 01', '@HARIPRASATH2611', tech skill chips, git command, and footer link pills.")
    ]
    for prefix, body in typo_items:
        p = doc.add_paragraph(style='List Bullet')
        r_p = p.add_run(prefix)
        r_p.font.bold = True
        p.add_run(body)

    # 4. Card Breakdown & Living Animations
    h4 = doc.add_heading(level=1)
    r4 = h4.add_run("4. Card Component Architecture & Animations")
    r4.font.name = 'Arial'
    r4.font.color.rgb = c_dark

    components = [
        ("Hero Card", "Features a floating photo card powered by SMIL animateTransform (5s cycle), unedited photo from assets/profile.png, Syne 800 name typography, and a pulsing orange status indicator (Open to new projects)."),
        ("Main Quest Card", "High-contrast lilac badge with breathing glow effect. Formatted with 24px horizontal and 14px vertical padding around Syne 800 text, avoiding any clipping or overflow."),
        ("Inventory Card", "Categorized into FRONTEND, MOBILE, BACKEND, and DATABASE rows. Skill chips feature a staggered micro-flash stroke animation sweep. Special highlight on 'Vector DBs' chip."),
        ("Commit Log & Contribution Snake", "Includes terminal header with blinking orange cursor ('git log --oneline'), dashed graph container with the user's real 53-week 2026 contribution history (2,903 contributions), an animated snake with glowing head and gradient body traversing the zigzag trail, and a git timeline with expanding radar pulse rings on commit nodes."),
        ("Footer Card", "Lilac background card ('Join my party') with right-aligned interactive pills. Dark portfolio pill features an animated light shine reflection sweep; outlined pill displays user's contact email.")
    ]

    for title, desc in components:
        p = doc.add_paragraph(style='List Bullet')
        r_t = p.add_run(f"{title}: ")
        r_t.font.bold = True
        p.add_run(desc)

    # 5. Maintenance & Update Workflow
    h5 = doc.add_heading(level=1)
    r5 = h5.add_run("5. Maintenance & Build Instructions")
    r5.font.name = 'Arial'
    r5.font.color.rgb = c_dark

    doc.add_paragraph(
        "To update contribution statistics or modify design elements in the future, follow these steps:"
    )

    steps = [
        "To update the contribution graph: Run python build_full_svg.py. The script automatically reads assets/contributions.json and maps the exact 53-week calendar.",
        "To refresh contribution data from GitHub: Fetch latest JSON from the contributions API and save to assets/contributions.json.",
        "To modify animations or styles: Edit build_full_svg.py, update the respective SVG markup or keyframes, and run python build_full_svg.py.",
        "To test rendered appearance locally: Run node render_full_svg.js to generate assets/profile-animated-render.png."
    ]
    for s in steps:
        p = doc.add_paragraph(style='List Number')
        p.add_run(s)

    # Accessibility note
    p_acc = doc.add_paragraph()
    p_acc.paragraph_format.space_before = Pt(12)
    r_acc_lbl = p_acc.add_run("Accessibility & Motion Safety: ")
    r_acc_lbl.font.bold = True
    p_acc.add_run(
        "All animations within the SVG are conditioned with @media (prefers-reduced-motion: reduce), "
        "disabling transforms, keyframes, and filter animations for users with vestibular or motion sensitivities."
    )

    doc.save("DOCUMENTATION.docx")
    print("Successfully saved DOCUMENTATION.docx")

if __name__ == '__main__':
    create_docx()

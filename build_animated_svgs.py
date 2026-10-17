import base64
import re
import os

# Load embedded fonts
with open('embedded_fonts.css', 'r', encoding='utf-8') as f:
    all_fonts_css = f.read()

# Helper to extract specific font blocks
def get_font_css(families_and_weights):
    blocks = all_fonts_css.split('@font-face')
    selected = []
    for b in blocks:
        for fam, wt in families_and_weights:
            if f"font-family: '{fam}'" in b and f"font-weight: {wt}" in b:
                selected.append('@font-face' + b)
                break
    return '\n'.join(selected)

# Load cropped profile photo base64
with open('assets/profile_crop.b64', 'r', encoding='utf-8') as f:
    photo_b64 = f.read().strip()

os.makedirs('assets', exist_ok=True)
os.makedirs('assets-src', exist_ok=True)

# -------------------------------------------------------------
# BLOCK 1: 01-hero.svg
# -------------------------------------------------------------
hero_fonts = get_font_css([('Syne', '800'), ('DM Sans', '400'), ('Space Mono', '400'), ('Space Mono', '700')])

hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 440" width="100%" height="100%">
<defs>
  <style>
{hero_fonts}

    .bg {{ fill: #1B1030; }}
    
    /* Animations */
    @keyframes heroEntrance {{
      0% {{ opacity: 0; transform: translateY(18px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes floatCard {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-8px); }}
    }}
    
    @keyframes statusBlink {{
      0%, 100% {{ opacity: 1; filter: drop-shadow(0 0 6px rgba(255,138,61,0.8)); }}
      50% {{ opacity: 0.4; filter: drop-shadow(0 0 1px rgba(255,138,61,0.2)); }}
    }}

    .anim-topbar {{
      animation: heroEntrance 0.7s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .anim-card-wrap {{
      animation: heroEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.15s both;
    }}
    .floating-card {{
      animation: floatCard 5s ease-in-out infinite;
    }}
    .anim-name {{
      animation: heroEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
    }}
    .anim-bio {{
      animation: heroEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.45s both;
    }}
    .anim-status {{
      animation: heroEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.6s both;
    }}
    .status-dot {{
      animation: statusBlink 2s ease-in-out infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .anim-topbar, .anim-card-wrap, .floating-card, .anim-name, .anim-bio, .anim-status, .status-dot {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
      }}
    }}
  </style>

  <clipPath id="photoClip">
    <rect x="0" y="0" width="224" height="255" rx="28" ry="28" />
  </clipPath>
</defs>

<!-- Background -->
<rect width="900" height="440" class="bg" />

<!-- Top Bar -->
<g class="anim-topbar" transform="translate(48, 48)">
  <text x="0" y="0" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">PLAYER 01</text>
  <text x="804" y="0" text-anchor="end" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">@HARIPRASATH2611</text>
</g>

<!-- Hero Row -->
<g transform="translate(48, 80)">
  
  <!-- Left: Photo Card (Floating) -->
  <g class="anim-card-wrap">
    <g class="floating-card">
      <!-- Card Container -->
      <rect x="0" y="0" width="224" height="328" rx="28" ry="28" fill="#FF8A3D" />
      
      <!-- Photo with top rounded clip -->
      <g clip-path="url(#photoClip)">
        <image href="data:image/jpeg;base64,{photo_b64}" x="0" y="0" width="224" height="255" preserveAspectRatio="xMidYMid slice" />
      </g>
      
      <!-- Photo Card Label -->
      <text x="18" y="286" fill="#1B1030" font-family="'Syne', sans-serif" font-weight="800" font-size="21" letter-spacing="-0.3">Full stack</text>
      <text x="18" y="310" fill="#1B1030" font-family="'Syne', sans-serif" font-weight="800" font-size="21" letter-spacing="-0.3">developer</text>
    </g>
  </g>

  <!-- Right: Hero Content -->
  <g transform="translate(260, 20)">
    <!-- Name -->
    <g class="anim-name">
      <text x="0" y="48" fill="#F6F1FF" font-family="'Syne', sans-serif" font-weight="800" font-size="64" letter-spacing="-2.5">Hariprasath</text>
    </g>

    <!-- Bio (3 lines matching exact wrap) -->
    <g class="anim-bio" font-family="'DM Sans', sans-serif" font-weight="400" font-size="16.5" fill="#CFC4EA">
      <text x="0" y="102">I build web and mobile apps end to end, from</text>
      <text x="0" y="128">the database to the screen. Clean APIs, fast</text>
      <text x="0" y="154">interfaces, and data models that hold up.</text>
    </g>

    <!-- Status -->
    <g class="anim-status" transform="translate(0, 214)">
      <circle cx="5" cy="-4" r="5" fill="#FF8A3D" class="status-dot" />
      <text x="22" y="0" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13.5" font-weight="400">Open to new projects</text>
    </g>
  </g>

</g>
</svg>'''

with open('assets/01-hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
with open('assets-src/01-hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)
print('Saved 01-hero.svg')

# -------------------------------------------------------------
# BLOCK 2: 02-main-quest.svg
# -------------------------------------------------------------
quest_fonts = get_font_css([('Syne', '800'), ('DM Sans', '500')])

quest_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 98" width="100%" height="100%">
<defs>
  <style>
{quest_fonts}

    .bg {{ fill: #1B1030; }}
    
    @keyframes questEntrance {{
      0% {{ opacity: 0; transform: translateY(16px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    
    @keyframes lilacGlow {{
      0%, 100% {{
        filter: drop-shadow(0 0 3px rgba(183,156,255,0.3));
      }}
      50% {{
        filter: drop-shadow(0 0 14px rgba(183,156,255,0.85));
      }}
    }}

    .anim-card {{
      animation: questEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
    }}
    .glow-badge {{
      animation: lilacGlow 2.6s ease-in-out infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .anim-card, .glow-badge {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
        filter: none !important;
      }}
    }}
  </style>
</defs>

<rect width="900" height="98" class="bg" />

<g class="anim-card" transform="translate(48, 10)">
  <!-- Card Background -->
  <rect x="0" y="0" width="804" height="78" rx="24" ry="24" fill="#2A1A4A" />

  <!-- Lilac Glowing Badge -->
  <g class="glow-badge" transform="translate(24, 18)">
    <rect x="0" y="0" width="168" height="42" rx="12" ry="12" fill="#B79CFF" />
    <text x="84" y="27" text-anchor="middle" fill="#1B1030" font-family="'Syne', sans-serif" font-weight="800" font-size="17" letter-spacing="0.3">MAIN QUEST</text>
  </g>

  <!-- Quest Text -->
  <text x="216" y="45" fill="#F6F1FF" font-family="'DM Sans', sans-serif" font-weight="500" font-size="15.2">Learning vector databases, and how semantic search is built on top of them.</text>
</g>
</svg>'''

with open('assets/02-main-quest.svg', 'w', encoding='utf-8') as f:
    f.write(quest_svg)
with open('assets-src/02-main-quest.svg', 'w', encoding='utf-8') as f:
    f.write(quest_svg)
print('Saved 02-main-quest.svg')

# -------------------------------------------------------------
# BLOCK 3: 03-inventory.svg
# -------------------------------------------------------------
inv_fonts = get_font_css([('Syne', '800'), ('Space Mono', '700')])

inv_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 372" width="100%" height="100%">
<defs>
  <style>
{inv_fonts}

    .bg {{ fill: #1B1030; }}

    /* Title Gradient Flow */
    @keyframes flowGradient {{
      0% {{ stop-color: #FF8A3D; }}
      50% {{ stop-color: #B79CFF; }}
      100% {{ stop-color: #FF8A3D; }}
    }}
    @keyframes flowGradient2 {{
      0% {{ stop-color: #B79CFF; }}
      50% {{ stop-color: #FF8A3D; }}
      100% {{ stop-color: #B79CFF; }}
    }}

    /* Card Entrance */
    @keyframes invEntrance {{
      0% {{ opacity: 0; transform: translateY(16px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Chip Pop-in */
    @keyframes chipPop {{
      0% {{ opacity: 0; transform: scale(0.88); }}
      70% {{ transform: scale(1.04); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}

    /* Sequential Orange Outline Flash */
    @keyframes chipFlash {{
      0%, 100% {{ stroke: transparent; stroke-width: 1.5; }}
      10%, 25% {{ stroke: #FF8A3D; stroke-width: 1.5; filter: drop-shadow(0 0 5px rgba(255,138,61,0.6)); }}
    }}

    .anim-card {{
      animation: invEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.4s both;
    }}

    .chip-pop {{
      transform-origin: center;
      animation: chipPop 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
    }}

    .c1 {{ animation-delay: 0.50s; }}
    .c2 {{ animation-delay: 0.55s; }}
    .c3 {{ animation-delay: 0.60s; }}
    .c4 {{ animation-delay: 0.65s; }}
    .c5 {{ animation-delay: 0.70s; }}
    .c6 {{ animation-delay: 0.75s; }}
    .c7 {{ animation-delay: 0.80s; }}
    .c8 {{ animation-delay: 0.85s; }}
    .c9 {{ animation-delay: 0.90s; }}
    .c10 {{ animation-delay: 0.95s; }}
    .c11 {{ animation-delay: 1.00s; }}

    .flash-rect {{
      animation: chipFlash 6s ease-in-out infinite;
    }}
    .f1  {{ animation-delay: 0.0s; }}
    .f2  {{ animation-delay: 0.5s; }}
    .f3  {{ animation-delay: 1.0s; }}
    .f4  {{ animation-delay: 1.5s; }}
    .f5  {{ animation-delay: 2.0s; }}
    .f6  {{ animation-delay: 2.5s; }}
    .f7  {{ animation-delay: 3.0s; }}
    .f8  {{ animation-delay: 3.5s; }}
    .f9  {{ animation-delay: 4.0s; }}
    .f10 {{ animation-delay: 4.5s; }}
    .f11 {{ animation-delay: 5.0s; }}

    @media (prefers-reduced-motion: reduce) {{
      .anim-card, .chip-pop, .flash-rect {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
      }}
    }}
  </style>

  <linearGradient id="invTitleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%">
      <animate attributeName="stop-color" values="#FF8A3D;#B79CFF;#FF8A3D" dur="5s" repeatCount="indefinite" />
    </stop>
    <stop offset="100%">
      <animate attributeName="stop-color" values="#B79CFF;#FF8A3D;#B79CFF" dur="5s" repeatCount="indefinite" />
    </stop>
  </linearGradient>
</defs>

<rect width="900" height="372" class="bg" />

<g class="anim-card" transform="translate(48, 10)">
  <!-- Card Background -->
  <rect x="0" y="0" width="804" height="352" rx="24" ry="24" fill="#2A1A4A" />

  <!-- Animated Gradient Title -->
  <text x="36" y="52" fill="url(#invTitleGrad)" font-family="'Syne', sans-serif" font-weight="800" font-size="32">Inventory</text>

  <!-- Skill Rows -->
  <!-- ROW 1: FRONTEND -->
  <g transform="translate(36, 78)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">FRONTEND</text>
    <g transform="translate(130, 0)">
      <!-- HTML -->
      <g class="chip-pop c1">
        <rect class="flash-rect f1" x="0" y="0" width="68" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="34" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">HTML</text>
      </g>
      <!-- CSS -->
      <g class="chip-pop c2" transform="translate(80, 0)">
        <rect class="flash-rect f2" x="0" y="0" width="60" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="30" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">CSS</text>
      </g>
      <!-- JavaScript -->
      <g class="chip-pop c3" transform="translate(152, 0)">
        <rect class="flash-rect f3" x="0" y="0" width="124" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="62" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">JavaScript</text>
      </g>
      <!-- React -->
      <g class="chip-pop c4" transform="translate(288, 0)">
        <rect class="flash-rect f4" x="0" y="0" width="76" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="38" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">React</text>
      </g>
    </g>
  </g>

  <!-- ROW 2: MOBILE -->
  <g transform="translate(36, 134)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">MOBILE</text>
    <g transform="translate(130, 0)">
      <!-- React Native -->
      <g class="chip-pop c5">
        <rect class="flash-rect f5" x="0" y="0" width="134" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="67" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">React Native</text>
      </g>
      <!-- Flutter -->
      <g class="chip-pop c6" transform="translate(146, 0)">
        <rect class="flash-rect f6" x="0" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="47" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Flutter</text>
      </g>
    </g>
  </g>

  <!-- ROW 3: BACKEND -->
  <g transform="translate(36, 190)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">BACKEND</text>
    <g transform="translate(130, 0)">
      <!-- Node.js -->
      <g class="chip-pop c7">
        <rect class="flash-rect f7" x="0" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="47" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Node.js</text>
      </g>
      <!-- Express.js -->
      <g class="chip-pop c8" transform="translate(106, 0)">
        <rect class="flash-rect f8" x="0" y="0" width="118" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="59" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Express.js</text>
      </g>
    </g>
  </g>

  <!-- ROW 4: DATABASE -->
  <g transform="translate(36, 246)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">DATABASE</text>
    <g transform="translate(130, 0)">
      <!-- MongoDB -->
      <g class="chip-pop c9">
        <rect class="flash-rect f9" x="0" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="47" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">MongoDB</text>
      </g>
      <!-- PostgreSQL -->
      <g class="chip-pop c10" transform="translate(106, 0)">
        <rect class="flash-rect f10" x="0" y="0" width="118" height="36" rx="8" ry="8" fill="#1B1030" />
        <text x="59" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">PostgreSQL</text>
      </g>
      <!-- Vector DBs (Highlight Orange) -->
      <g class="chip-pop c11" transform="translate(236, 0)">
        <rect class="flash-rect f11" x="0" y="0" width="124" height="36" rx="8" ry="8" fill="#FF8A3D" />
        <text x="62" y="22" text-anchor="middle" fill="#1B1030" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Vector DBs</text>
      </g>
    </g>
  </g>
</g>
</svg>'''

with open('assets/03-inventory.svg', 'w', encoding='utf-8') as f:
    f.write(inv_svg)
with open('assets-src/03-inventory.svg', 'w', encoding='utf-8') as f:
    f.write(inv_svg)
print('Saved 03-inventory.svg')

# -------------------------------------------------------------
# BLOCK 4: 04-commit-log.svg
# -------------------------------------------------------------
commit_fonts = get_font_css([('Syne', '800'), ('DM Sans', '400'), ('Space Mono', '400'), ('Space Mono', '700')])

commit_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 472" width="100%" height="100%">
<defs>
  <style>
{commit_fonts}

    .bg {{ fill: #1B1030; }}

    /* Flowing Title Gradient */
    @keyframes commitTitleFlow {{
      0% {{ stop-color: #F6F1FF; }}
      50% {{ stop-color: #B79CFF; }}
      100% {{ stop-color: #F6F1FF; }}
    }}

    /* Blinking Terminal Cursor */
    @keyframes cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}

    /* Timeline Line Draw */
    @keyframes drawTimeline {{
      0% {{ stroke-dashoffset: 220; }}
      100% {{ stroke-dashoffset: 0; }}
    }}

    /* Timeline Items Slide-in */
    @keyframes slideLeft {{
      0% {{ opacity: 0; transform: translateX(-16px); }}
      100% {{ opacity: 1; transform: translateX(0); }}
    }}

    /* Node Ring Pulse */
    @keyframes ringPulse {{
      0% {{
        r: 5.5;
        stroke: #FF8A3D;
        stroke-width: 2;
        opacity: 0.9;
      }}
      100% {{
        r: 16;
        stroke: #FF8A3D;
        stroke-width: 0.5;
        opacity: 0;
      }}
    }}

    .anim-card {{
      animation: slideLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.5s both;
    }}
    .cursor {{
      animation: cursorBlink 1s infinite;
    }}
    .timeline-line {{
      stroke-dasharray: 220;
      animation: drawTimeline 1.2s cubic-bezier(0.16, 1, 0.3, 1) 0.6s both;
    }}
    .t1 {{ animation: slideLeft 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.7s both; }}
    .t2 {{ animation: slideLeft 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.9s both; }}
    .t3 {{ animation: slideLeft 0.7s cubic-bezier(0.16, 1, 0.3, 1) 1.1s both; }}

    .ring-pulse {{
      animation: ringPulse 2.5s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
      transform-origin: center;
    }}
    .p2 {{ animation-delay: 0.8s; }}
    .p3 {{ animation-delay: 1.6s; }}

    @media (prefers-reduced-motion: reduce) {{
      .anim-card, .cursor, .timeline-line, .t1, .t2, .t3, .ring-pulse {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
        stroke-dashoffset: 0 !important;
      }}
    }}
  </style>

  <linearGradient id="commitGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%">
      <animate attributeName="stop-color" values="#F6F1FF;#B79CFF;#FF8A3D;#F6F1FF" dur="6s" repeatCount="indefinite" />
    </stop>
    <stop offset="100%">
      <animate attributeName="stop-color" values="#B79CFF;#FF8A3D;#F6F1FF;#B79CFF" dur="6s" repeatCount="indefinite" />
    </stop>
  </linearGradient>
</defs>

<rect width="900" height="472" class="bg" />

<g class="anim-card" transform="translate(48, 10)">
  <!-- Card Background -->
  <rect x="0" y="0" width="804" height="452" rx="24" ry="24" fill="#2A1A4A" />

  <!-- Card Header -->
  <text x="36" y="52" fill="url(#commitGrad)" font-family="'Syne', sans-serif" font-weight="800" font-size="32">Commit log</text>
  <g transform="translate(768, 50)">
    <text x="0" y="0" text-anchor="end" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13.5" font-weight="400" letter-spacing="0.5">git log --oneline</text>
    <rect x="3" y="-12" width="7" height="15" fill="#FF8A3D" class="cursor" />
  </g>

  <!-- Dashed Graph Container -->
  <g transform="translate(36, 78)">
    <rect x="0" y="0" width="732" height="76" rx="16" ry="16" fill="#1B1030" stroke="#4A3578" stroke-width="1.5" stroke-dasharray="6 6" />
    <text x="366" y="44" text-anchor="middle" fill="#CFC4EA" font-family="'Space Mono', monospace" font-size="13.5" letter-spacing="0.3">
      Contribution graph: filled live from @HARIPRASATH2611
    </text>
  </g>

  <!-- Vertical Git Timeline -->
  <g transform="translate(36, 186)">
    <!-- Continuous Vertical Branch Line -->
    <line x1="5.5" y1="6" x2="5.5" y2="190" stroke="#4A3578" stroke-width="1.5" class="timeline-line" />

    <!-- Commit 1 -->
    <g class="t1" transform="translate(0, 0)">
      <!-- Pulsing Ring -->
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: on-demand driver booking app</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', sans-serif" font-size="14.5" font-weight="400">Customers book a professional driver for their own vehicle. React Native and Node.</text>
    </g>

    <!-- Commit 2 -->
    <g class="t2" transform="translate(0, 76)">
      <!-- Pulsing Ring -->
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse p2" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: campus ERP attendance module</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', sans-serif" font-size="14.5" font-weight="400">Faculty attendance on mobile, built with React Native and Expo.</text>
    </g>

    <!-- Commit 3 -->
    <g class="t3" transform="translate(0, 152)">
      <!-- Pulsing Ring -->
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse p3" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: SIH 2026 identity platform</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', sans-serif" font-size="14.5" font-weight="400">Blockchain identity, access control and digital assets.</text>
    </g>
  </g>
</g>
</svg>'''

with open('assets/04-commit-log.svg', 'w', encoding='utf-8') as f:
    f.write(commit_svg)
with open('assets-src/04-commit-log.svg', 'w', encoding='utf-8') as f:
    f.write(commit_svg)
print('Saved 04-commit-log.svg')

# -------------------------------------------------------------
# BLOCK 5: 05-footer.svg
# -------------------------------------------------------------
footer_fonts = get_font_css([('Syne', '800'), ('Space Mono', '700')])

footer_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 110" width="100%" height="100%">
<defs>
  <style>
{footer_fonts}

    .bg {{ fill: #1B1030; }}

    @keyframes footerEntrance {{
      0% {{ opacity: 0; transform: translateY(16px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Moving Shine Sweep every ~4.5s */
    @keyframes shineSweep {{
      0% {{ transform: translateX(-160px) skewX(-25deg); opacity: 0; }}
      15% {{ opacity: 0.6; }}
      30% {{ transform: translateX(360px) skewX(-25deg); opacity: 0; }}
      100% {{ transform: translateX(360px) skewX(-25deg); opacity: 0; }}
    }}

    .anim-card {{
      animation: footerEntrance 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.6s both;
    }}
    .shine-rect {{
      animation: shineSweep 4.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .anim-card, .shine-rect {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
      }}
    }}
  </style>

  <clipPath id="darkPillClip">
    <rect x="0" y="0" width="298" height="38" rx="19" ry="19" />
  </clipPath>
</defs>

<rect width="900" height="110" class="bg" />

<g class="anim-card" transform="translate(48, 10)">
  <!-- Lilac Footer Card -->
  <rect x="0" y="0" width="804" height="78" rx="24" ry="24" fill="#B79CFF" />

  <!-- Title -->
  <text x="32" y="48" fill="#1B1030" font-family="'Syne', sans-serif" font-weight="800" font-size="26" letter-spacing="-0.5">Join my party</text>

  <!-- Right Pills Container -->
  <g transform="translate(242, 20)">
    <!-- Dark Portfolio Pill (with Shine Sweep) -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="298" height="38" rx="19" ry="19" fill="#1B1030" />
      <!-- Shine sweep clipped to pill -->
      <g clip-path="url(#darkPillClip)">
        <rect x="0" y="-10" width="50" height="60" fill="url(#shineGrad)" class="shine-rect" />
      </g>
      <text x="149" y="24" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="11" font-weight="700" letter-spacing="-0.2">hariprasathportfolio-zeta.vercel.app</text>
    </g>

    <!-- Outlined Email Pill -->
    <g transform="translate(308, 0)">
      <rect x="0" y="0" width="218" height="38" rx="19" ry="19" fill="none" stroke="#1B1030" stroke-width="1.2" />
      <text x="109" y="24" text-anchor="middle" fill="#1B1030" font-family="'Space Mono', monospace" font-size="10.5" font-weight="700" letter-spacing="-0.3">[hariprasathd26112006@gmail.com]</text>
    </g>
  </g>
</g>

<linearGradient id="shineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
  <stop offset="50%" stop-color="#ffffff" stop-opacity="0.45" />
  <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
</linearGradient>
</svg>'''

with open('assets/05-footer.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
with open('assets-src/05-footer.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print('Saved 05-footer.svg')

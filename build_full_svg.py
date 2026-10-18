import base64
import json
import urllib.request

# Load cropped profile photo base64
with open('assets/profile_crop.b64', 'r', encoding='utf-8') as f:
    photo_b64 = f.read().strip()

# Fetch real contribution data for HARIPRASATH2611
req = urllib.request.Request('https://github-contributions-api.jogruber.de/v4/HARIPRASATH2611', headers={'User-Agent': 'Mozilla/5.0'})
data = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))
contributions = data.get('contributions', [])
recent_days = contributions[-371:]
while len(recent_days) < 371:
    recent_days.insert(0, {'count': 0, 'level': 0})

colors = ['#34225A', '#6E4FB5', '#B79CFF', '#FFB27A', '#FF8A3D']

# Generate snake inside commit log dashed container
# Dashed box: x=84, y=1000, width=732, height=110
# 53 cols x 7 rows
cols = 53
rows = 7
cell_size = 9
gap = 3
grid_x0 = 84 + (732 - (cols * cell_size + (cols - 1) * gap)) / 2 # center horizontally
grid_y0 = 1000 + 16

snake_cells = []
snake_points = []
cell_idx = 0

for c in range(cols):
    col_cx = grid_x0 + c * (cell_size + gap) + cell_size / 2
    if c % 2 == 0:
        row_range = range(rows)
    else:
        row_range = range(rows - 1, -1, -1)
    
    for r in row_range:
        snake_points.append((col_cx, grid_y0 + r * (cell_size + gap) + cell_size / 2))

for col in range(cols):
    for row in range(rows):
        if cell_idx < len(recent_days):
            level = min(recent_days[cell_idx].get('level', 0), 4)
        else:
            level = 0
        fill = colors[level]
        x = grid_x0 + col * (cell_size + gap)
        y = grid_y0 + row * (cell_size + gap)
        
        step = col * 7 + (row if col % 2 == 0 else (6 - row))
        delay = (step / 371.0) * 22.0
        snake_cells.append(f'<rect class="grid-cell" x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" fill="{fill}" style="animation-delay: {delay:.2f}s;" />')
        cell_idx += 1

path_d = f"M {snake_points[0][0]:.1f},{snake_points[0][1]:.1f} " + " ".join([f"L {p[0]:.1f},{p[1]:.1f}" for p in snake_points[1:]])

# Build complete profile-animated.svg
full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 1540" width="100%" height="100%">
<defs>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&amp;family=Space+Mono:wght@400;700&amp;family=Syne:wght@700;800&amp;display=swap');

    * {{ box-sizing: border-box; }}
    
    .bg {{ fill: #1B1030; }}
    
    /* Animations */
    @keyframes floatCard {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-7px); }}
    }}
    
    @keyframes statusBlink {{
      0%, 100% {{ opacity: 1; filter: drop-shadow(0 0 6px rgba(255,138,61,0.85)); }}
      50% {{ opacity: 0.35; filter: drop-shadow(0 0 1px rgba(255,138,61,0.2)); }}
    }}

    @keyframes lilacGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 4px rgba(183,156,255,0.35)); }}
      50% {{ filter: drop-shadow(0 0 14px rgba(183,156,255,0.85)); }}
    }}

    @keyframes chipFlash {{
      0%, 100% {{ stroke: transparent; stroke-width: 1.5; }}
      10%, 25% {{ stroke: #FF8A3D; stroke-width: 1.5; filter: drop-shadow(0 0 6px rgba(255,138,61,0.7)); }}
    }}

    @keyframes cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}

    @keyframes ringPulse {{
      0% {{ r: 5.5; stroke: #FF8A3D; stroke-width: 2; opacity: 0.9; }}
      100% {{ r: 16; stroke: #FF8A3D; stroke-width: 0.5; opacity: 0; }}
    }}

    @keyframes eatEffect {{
      0%, 100% {{ transform: scale(1); opacity: 1; }}
      1.5% {{ transform: scale(0.3); opacity: 0.2; fill: #1B1030; }}
      12% {{ transform: scale(1); opacity: 1; }}
    }}

    @keyframes shineSweep {{
      0% {{ transform: translateX(-160px) skewX(-25deg); opacity: 0; }}
      15% {{ opacity: 0.6; }}
      30% {{ transform: translateX(360px) skewX(-25deg); opacity: 0; }}
      100% {{ transform: translateX(360px) skewX(-25deg); opacity: 0; }}
    }}

    .floating-card {{
      animation: floatCard 5s ease-in-out infinite;
    }}
    .status-dot {{
      animation: statusBlink 2s ease-in-out infinite;
    }}
    .glow-badge {{
      animation: lilacGlow 2.6s ease-in-out infinite;
    }}
    .cursor {{
      animation: cursorBlink 1s infinite;
    }}
    .ring-pulse {{
      animation: ringPulse 2.5s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
      transform-origin: center;
    }}
    .p2 {{ animation-delay: 0.8s; }}
    .p3 {{ animation-delay: 1.6s; }}
    .shine-rect {{
      animation: shineSweep 4.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }}
    .grid-cell {{
      transform-box: fill-box;
      transform-origin: center;
      animation: eatEffect 22s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }}
    .flash-rect {{
      animation: chipFlash 6s ease-in-out infinite;
    }}
    .f1 {{ animation-delay: 0.0s; }}
    .f2 {{ animation-delay: 0.5s; }}
    .f3 {{ animation-delay: 1.0s; }}
    .f4 {{ animation-delay: 1.5s; }}
    .f5 {{ animation-delay: 2.0s; }}
    .f6 {{ animation-delay: 2.5s; }}
    .f7 {{ animation-delay: 3.0s; }}
    .f8 {{ animation-delay: 3.5s; }}
    .f9 {{ animation-delay: 4.0s; }}
    .f10 {{ animation-delay: 4.5s; }}
    .f11 {{ animation-delay: 5.0s; }}

    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation: none !important;
        transform: none !important;
        filter: none !important;
      }}
    }}
  </style>

  <clipPath id="photoClip">
    <rect x="0" y="0" width="224" height="255" rx="28" ry="28" />
  </clipPath>

  <clipPath id="darkPillClip">
    <rect x="0" y="0" width="298" height="38" rx="19" ry="19" />
  </clipPath>

  <linearGradient id="invTitleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%">
      <animate attributeName="stop-color" values="#FF8A3D;#B79CFF;#FF8A3D" dur="5s" repeatCount="indefinite" />
    </stop>
    <stop offset="100%">
      <animate attributeName="stop-color" values="#B79CFF;#FF8A3D;#B79CFF" dur="5s" repeatCount="indefinite" />
    </stop>
  </linearGradient>

  <linearGradient id="commitGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%">
      <animate attributeName="stop-color" values="#F6F1FF;#B79CFF;#FF8A3D;#F6F1FF" dur="6s" repeatCount="indefinite" />
    </stop>
    <stop offset="100%">
      <animate attributeName="stop-color" values="#B79CFF;#FF8A3D;#F6F1FF;#B79CFF" dur="6s" repeatCount="indefinite" />
    </stop>
  </linearGradient>

  <linearGradient id="shineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
    <stop offset="50%" stop-color="#ffffff" stop-opacity="0.45" />
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
  </linearGradient>

  <path id="snakePath" d="{path_d}" fill="none" />
</defs>

<!-- Overall Canvas Background -->
<rect width="900" height="1540" class="bg" />

<!-- ========================================== -->
<!-- 1. TOP BAR & HERO SECTION -->
<!-- ========================================== -->
<!-- Top Bar -->
<text x="48" y="48" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">PLAYER 01</text>
<text x="852" y="48" text-anchor="end" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">@HARIPRASATH2611</text>

<!-- Hero Row -->
<g transform="translate(48, 80)">
  <!-- Floating Photo Card -->
  <g class="floating-card">
    <rect x="0" y="0" width="224" height="328" rx="28" ry="28" fill="#FF8A3D" />
    <g clip-path="url(#photoClip)">
      <image href="data:image/jpeg;base64,{photo_b64}" x="0" y="0" width="224" height="255" preserveAspectRatio="xMidYMid slice" />
    </g>
    <text x="18" y="286" fill="#1B1030" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="21" letter-spacing="-0.3">Full stack</text>
    <text x="18" y="310" fill="#1B1030" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="21" letter-spacing="-0.3">developer</text>
  </g>

  <!-- Right: Hero Content -->
  <g transform="translate(260, 20)">
    <text x="0" y="48" fill="#F6F1FF" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="64" letter-spacing="-2.5">Hariprasath</text>
    <g font-family="'DM Sans', system-ui, sans-serif" font-weight="400" font-size="16.5" fill="#CFC4EA">
      <text x="0" y="102">I build web and mobile apps end to end, from</text>
      <text x="0" y="128">the database to the screen. Clean APIs, fast</text>
      <text x="0" y="154">interfaces, and data models that hold up.</text>
    </g>
    <g transform="translate(0, 214)">
      <circle cx="5" cy="-4" r="5" fill="#FF8A3D" class="status-dot" />
      <text x="22" y="0" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13.5" font-weight="400">Open to new projects</text>
    </g>
  </g>
</g>

<!-- ========================================== -->
<!-- 2. MAIN QUEST CARD -->
<!-- ========================================== -->
<g transform="translate(48, 434)">
  <rect x="0" y="0" width="804" height="78" rx="24" ry="24" fill="#2A1A4A" />
  <g class="glow-badge" transform="translate(24, 18)">
    <rect x="0" y="0" width="168" height="42" rx="12" ry="12" fill="#B79CFF" />
    <text x="84" y="27" text-anchor="middle" fill="#1B1030" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="17" letter-spacing="0.3">MAIN QUEST</text>
  </g>
  <text x="216" y="45" fill="#F6F1FF" font-family="'DM Sans', system-ui, sans-serif" font-weight="500" font-size="15.2">Learning vector databases, and how semantic search is built on top of them.</text>
</g>

<!-- ========================================== -->
<!-- 3. INVENTORY CARD -->
<!-- ========================================== -->
<g transform="translate(48, 536)">
  <rect x="0" y="0" width="804" height="344" rx="24" ry="24" fill="#2A1A4A" />
  <text x="36" y="52" fill="url(#invTitleGrad)" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="32">Inventory</text>

  <!-- Row 1: FRONTEND -->
  <g transform="translate(36, 78)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">FRONTEND</text>
    <g transform="translate(130, 0)">
      <rect class="flash-rect f1" x="0" y="0" width="68" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="34" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">HTML</text>
      <rect class="flash-rect f2" x="80" y="0" width="60" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="110" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">CSS</text>
      <rect class="flash-rect f3" x="152" y="0" width="124" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="214" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">JavaScript</text>
      <rect class="flash-rect f4" x="288" y="0" width="76" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="326" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">React</text>
    </g>
  </g>

  <!-- Row 2: MOBILE -->
  <g transform="translate(36, 134)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">MOBILE</text>
    <g transform="translate(130, 0)">
      <rect class="flash-rect f5" x="0" y="0" width="134" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="67" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">React Native</text>
      <rect class="flash-rect f6" x="146" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="193" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Flutter</text>
    </g>
  </g>

  <!-- Row 3: BACKEND -->
  <g transform="translate(36, 190)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">BACKEND</text>
    <g transform="translate(130, 0)">
      <rect class="flash-rect f7" x="0" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="47" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Node.js</text>
      <rect class="flash-rect f8" x="106" y="0" width="118" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="165" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Express.js</text>
    </g>
  </g>

  <!-- Row 4: DATABASE -->
  <g transform="translate(36, 246)">
    <text x="0" y="24" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13" font-weight="700" letter-spacing="0.5">DATABASE</text>
    <g transform="translate(130, 0)">
      <rect class="flash-rect f9" x="0" y="0" width="94" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="47" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">MongoDB</text>
      <rect class="flash-rect f10" x="106" y="0" width="118" height="36" rx="8" ry="8" fill="#1B1030" />
      <text x="165" y="22" text-anchor="middle" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="13" font-weight="700">PostgreSQL</text>
      <rect class="flash-rect f11" x="236" y="0" width="124" height="36" rx="8" ry="8" fill="#FF8A3D" />
      <text x="298" y="22" text-anchor="middle" fill="#1B1030" font-family="'Space Mono', monospace" font-size="13" font-weight="700">Vector DBs</text>
    </g>
  </g>
</g>

<!-- ========================================== -->
<!-- 4. COMMIT LOG CARD (WITH REAL SNAKE!) -->
<!-- ========================================== -->
<g transform="translate(48, 904)">
  <rect x="0" y="0" width="804" height="492" rx="24" ry="24" fill="#2A1A4A" />

  <!-- Header -->
  <text x="36" y="52" fill="url(#commitGrad)" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="32">Commit log</text>
  <g transform="translate(768, 50)">
    <text x="0" y="0" text-anchor="end" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="13.5" font-weight="400" letter-spacing="0.5">git log --oneline</text>
    <rect x="3" y="-12" width="7" height="15" fill="#FF8A3D" class="cursor" />
  </g>

  <!-- Dashed Graph Container with Live Contribution Snake -->
  <g transform="translate(36, 78)">
    <rect x="0" y="0" width="732" height="118" rx="16" ry="16" fill="#1B1030" stroke="#4A3578" stroke-width="1.5" stroke-dasharray="6 6" />
    
    <!-- Real Grid Cells -->
    <g transform="translate(-48, -988)">
      {''.join(snake_cells)}
    </g>
    
    <!-- Real Zigzag Snake -->
    <g transform="translate(-48, -988)">
      <rect x="-4" y="-4" width="8" height="8" rx="2" ry="2" fill="#6E4FB5" opacity="0.6">
        <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.35s"><mpath href="#snakePath" /></animateMotion>
      </rect>
      <rect x="-4" y="-4" width="8.5" height="8.5" rx="2" ry="2" fill="#B79CFF" opacity="0.8">
        <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.26s"><mpath href="#snakePath" /></animateMotion>
      </rect>
      <rect x="-4.5" y="-4.5" width="9" height="9" rx="2" ry="2" fill="#FFB27A">
        <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.18s"><mpath href="#snakePath" /></animateMotion>
      </rect>
      <rect x="-4.5" y="-4.5" width="9" height="9" rx="2" ry="2" fill="#FF8A3D">
        <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.09s"><mpath href="#snakePath" /></animateMotion>
      </rect>
      <!-- Glowing Head -->
      <g filter="drop-shadow(0 0 6px #FFFFFF) drop-shadow(0 0 10px #FF8A3D)">
        <rect x="-5" y="-5" width="10" height="10" rx="2.5" ry="2.5" fill="#FFF8F2">
          <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="0s"><mpath href="#snakePath" /></animateMotion>
        </rect>
      </g>
    </g>
  </g>

  <!-- Git Timeline -->
  <g transform="translate(36, 226)">
    <line x1="5.5" y1="6" x2="5.5" y2="204" stroke="#4A3578" stroke-width="1.5" />

    <!-- Commit 1 -->
    <g transform="translate(0, 0)">
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: on-demand driver booking app</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', system-ui, sans-serif" font-size="14.5" font-weight="400">Customers book a professional driver for their own vehicle. React Native and Node.</text>
    </g>

    <!-- Commit 2 -->
    <g transform="translate(0, 80)">
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse p2" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: campus ERP attendance module</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', system-ui, sans-serif" font-size="14.5" font-weight="400">Faculty attendance on mobile, built with React Native and Expo.</text>
    </g>

    <!-- Commit 3 -->
    <g transform="translate(0, 160)">
      <circle cx="5.5" cy="5.5" r="5.5" fill="none" class="ring-pulse p3" />
      <circle cx="5.5" cy="5.5" r="5.5" fill="#FF8A3D" />
      <text x="28" y="9" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="15" font-weight="700">feat: SIH 2026 identity platform</text>
      <text x="28" y="32" fill="#CFC4EA" font-family="'DM Sans', system-ui, sans-serif" font-size="14.5" font-weight="400">Blockchain identity, access control and digital assets.</text>
    </g>
  </g>
</g>

<!-- ========================================== -->
<!-- 5. FOOTER CARD -->
<!-- ========================================== -->
<g transform="translate(48, 1420)">
  <rect x="0" y="0" width="804" height="78" rx="24" ry="24" fill="#B79CFF" />
  <text x="32" y="48" fill="#1B1030" font-family="'Syne', system-ui, sans-serif" font-weight="800" font-size="26" letter-spacing="-0.5">Join my party</text>

  <g transform="translate(242, 20)">
    <!-- Dark Portfolio Pill -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="298" height="38" rx="19" ry="19" fill="#1B1030" />
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

</svg>'''

with open('assets/profile-animated.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)
with open('assets-src/profile-animated.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)
print('Saved assets/profile-animated.svg (Height: 1540px)')

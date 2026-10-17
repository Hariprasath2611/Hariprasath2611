import urllib.request
import json

# Fetch real contribution data for HARIPRASATH2611
req = urllib.request.Request('https://github-contributions-api.jogruber.de/v4/HARIPRASATH2611', headers={'User-Agent': 'Mozilla/5.0'})
data = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))

contributions = data.get('contributions', [])
# We want the last 53 * 7 = 371 days
recent_days = contributions[-371:]
while len(recent_days) < 371:
    recent_days.insert(0, {'count': 0, 'level': 0})

# Level colors
colors = ['#34225A', '#6E4FB5', '#B79CFF', '#FFB27A', '#FF8A3D']

# Grid dimensions
cols = 53
rows = 7
cell_size = 11
gap = 3
pad_x = 24
pad_y = 20
width = pad_x * 2 + cols * cell_size + (cols - 1) * gap
height = pad_y * 2 + rows * cell_size + (rows - 1) * gap + 24

svg_cells = []
cell_index = 0
for col in range(cols):
    for row in range(rows):
        if cell_index < len(recent_days):
            level = recent_days[cell_index].get('level', 0)
            if level > 4:
                level = 4
        else:
            level = 0
        fill = colors[level]
        x = pad_x + col * (cell_size + gap)
        y = pad_y + row * (cell_size + gap)
        
        # Calculate snake traversal order (down col 0, up col 1, down col 2...)
        if col % 2 == 0:
            step_in_col = row
        else:
            step_in_col = 6 - row
        snake_step = col * 7 + step_in_col
        delay = (snake_step / 371.0) * 22.0
        
        svg_cells.append(f'''<rect id="c_{col}_{row}" class="grid-cell" x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" ry="2" fill="{fill}" data-orig="{fill}" style="animation-delay: {delay:.2f}s;" />''')
        cell_index += 1

# Generate the snake path points for zigzag traversal (col 0 down, col 1 up...)
snake_points = []
for c in range(cols):
    col_x = pad_x + c * (cell_size + gap) + cell_size / 2
    if c % 2 == 0:
        for r in range(rows):
            snake_points.append((col_x, pad_y + r * (cell_size + gap) + cell_size / 2))
    else:
        for r in range(rows - 1, -1, -1):
            snake_points.append((col_x, pad_y + r * (cell_size + gap) + cell_size / 2))

# Create smooth SVG motion path
path_d = f"M {snake_points[0][0]},{snake_points[0][1]} " + " ".join([f"L {p[0]},{p[1]}" for p in snake_points[1:]])

snake_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
<defs>
  <style>
    .bg {{ fill: #1B1030; }}
    
    /* Eaten cell effect */
    @keyframes eatEffect {{
      0%, 100% {{ transform: scale(1); filter: none; }}
      1.5% {{ transform: scale(0.3); opacity: 0.3; fill: #1B1030; }}
      12% {{ transform: scale(1); opacity: 1; }}
    }}

    .grid-cell {{
      transform-box: fill-box;
      transform-origin: center;
      animation: eatEffect 22s cubic-bezier(0.4, 0, 0.2, 1) infinite;
    }}

    @keyframes headGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 6px #FFFFFF) drop-shadow(0 0 12px #FF8A3D); }}
      50% {{ filter: drop-shadow(0 0 3px #FFFFFF) drop-shadow(0 0 8px #B79CFF); }}
    }}

    .snake-head {{
      animation: headGlow 2s ease-in-out infinite;
    }}

    @media (prefers-reduced-motion: reduce) {{
      .grid-cell, .snake-head, animateMotion {{
        animation: none !important;
      }}
    }}
  </style>

  <path id="snakePath" d="{path_d}" fill="none" />
</defs>

<!-- Outer Container -->
<rect width="{width}" height="{height}" rx="16" ry="16" fill="#1B1030" stroke="#4A3578" stroke-width="1.5" />

<!-- Header: Real Contributions Stats -->
<text x="{pad_x}" y="{height - 10}" fill="#B79CFF" font-family="'Space Mono', monospace" font-size="11" font-weight="700">@HARIPRASATH2611</text>
<text x="{width - pad_x}" y="{height - 10}" text-anchor="end" fill="#F6F1FF" font-family="'Space Mono', monospace" font-size="11" font-weight="400">2,865 contributions in 2026</text>

<!-- Grid Cells -->
<g id="gridGroup">
  {''.join(svg_cells)}
</g>

<!-- The Snake (7 body segments + head) -->
<!-- Body Segment 6 (Tail - Lilac) -->
<rect x="-5" y="-5" width="10" height="10" rx="2" ry="2" fill="#6E4FB5" opacity="0.6">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.42s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Body Segment 5 -->
<rect x="-5" y="-5" width="10" height="10" rx="2" ry="2" fill="#B79CFF" opacity="0.75">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.35s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Body Segment 4 -->
<rect x="-5" y="-5" width="10" height="10" rx="2" ry="2" fill="#B79CFF" opacity="0.9">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.28s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Body Segment 3 -->
<rect x="-5" y="-5" width="10.5" height="10.5" rx="2" ry="2" fill="#FFB27A">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.21s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Body Segment 2 -->
<rect x="-5.5" y="-5.5" width="11" height="11" rx="2.5" ry="2.5" fill="#FF8A3D">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.14s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Body Segment 1 (Neck) -->
<rect x="-5.5" y="-5.5" width="11" height="11" rx="2.5" ry="2.5" fill="#FFA566">
  <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="-0.07s">
    <mpath href="#snakePath" />
  </animateMotion>
</rect>

<!-- Snake Head (Glowing near-white square) -->
<g class="snake-head">
  <rect x="-6" y="-6" width="12" height="12" rx="3" ry="3" fill="#FFF8F2">
    <animateMotion dur="22s" repeatCount="indefinite" rotate="auto" begin="0s">
      <mpath href="#snakePath" />
    </animateMotion>
  </rect>
</g>
</svg>'''

with open('assets/fallback-snake.svg', 'w', encoding='utf-8') as f:
    f.write(snake_svg)
with open('assets-src/fallback-snake.svg', 'w', encoding='utf-8') as f:
    f.write(snake_svg)
print('Saved fallback-snake.svg with real data (371 days)')

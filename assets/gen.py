#!/usr/bin/env python3
# Generates beastly monochrome animated SVGs for the GitHub profile README.
import math, os

OUT = "/home/just-brainwaves/Public/just-brainwaves/assets"
os.makedirs(OUT, exist_ok=True)

# ---- monochrome palette ----
BG0, BG1 = "#0d0d10", "#08080a"
HAIR, HAIR2 = "#1c1c20", "#2a2a30"
INK_DIM, INK_MUT = "#5a5a62", "#8a8a92"
INK, INK_HI = "#d4d4d8", "#e8e8ea"
WHITE = "#ffffff"
MONO = "'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace"
SANS = "ui-sans-serif,system-ui,-apple-system,'Segoe UI',Inter,sans-serif"

def f(x): return f"{x:.2f}".rstrip("0").rstrip(".")

# ====================================================================
# 1) HERO  — morphing topographic flow field behind sharp typography
# ====================================================================
def hero():
    W, H = 880, 260
    cx_field = 440
    lines = 18
    top, bot = 26, 232
    step = 14
    xs = list(range(0, W + step, step))
    rows = []
    for i in range(lines):
        t = i / (lines - 1)
        base = top + t * (bot - top)
        amp = 6 + 16 * math.sin(math.pi * t)            # fat in the middle
        freq = 1.4 + 0.9 * math.sin(t * 3.1)            # per-line wavelength
        ph0 = t * 2.4
        ph1 = ph0 + 1.15                                # morph target (undulation)
        def dstr(ph):
            pts = []
            for x in xs:
                # horizontal envelope: flatter at edges, taller mid-canvas
                env = math.sin(math.pi * min(max(x / W, 0), 1)) ** 0.6
                y = base + amp * env * math.sin(freq * 2 * math.pi * x / W + ph)
                pts.append((x, y))
            d = "M" + " L".join(f"{f(px)} {f(py)}" for px, py in pts)
            return d
        d0, d1 = dstr(ph0), dstr(ph1)
        op = 0.06 + 0.5 * math.sin(math.pi * t) ** 1.4  # brighter mid rows
        col = INK_DIM if abs(t - 0.5) < 0.28 else HAIR2
        dur = 7.5 + 2.5 * math.sin(t * 2.0)
        beg = -(i * 0.34)
        rows.append(
            f'<path d="{d0}" fill="none" stroke="{col}" stroke-width="1" stroke-opacity="{f(op)}">'
            f'<animate attributeName="d" values="{d0};{d1};{d0}" dur="{f(abs(dur))}s" '
            f'begin="{f(beg)}s" calcMode="spline" keyTimes="0;0.5;1" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1" repeatCount="indefinite"/></path>'
        )
    field = "\n    ".join(rows)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="Aditya Shrimali — AI Engineer">
  <defs>
    <linearGradient id="hc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <linearGradient id="hscrim" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BG1}" stop-opacity="0.96"/>
      <stop offset="46%" stop-color="{BG1}" stop-opacity="0.62"/>
      <stop offset="100%" stop-color="{BG1}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="hvig" cx="50%" cy="46%" r="72%">
      <stop offset="60%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.55"/>
    </radialGradient>
    <linearGradient id="htop" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hsheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#fff" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="hclip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18"/></clipPath>
  </defs>

  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="url(#hc)" stroke="{HAIR}" stroke-width="1"/>
  <g clip-path="url(#hclip)">
    {field}
    <rect x="0" y="0" width="{W}" height="{H}" fill="url(#hvig)"/>
    <rect x="0" y="0" width="520" height="{H}" fill="url(#hscrim)"/>
    <rect x="-320" y="0" width="320" height="{H}" fill="url(#hsheen)">
      <animate attributeName="x" values="-320;{W}" dur="9s" begin="2s" repeatCount="indefinite"/>
    </rect>
    <rect x="1" y="1" width="{W-2}" height="78" rx="17" fill="url(#htop)"/>
  </g>

  <!-- monogram -->
  <g transform="translate(46,34)">
    <rect x="0.5" y="0.5" width="38" height="38" rx="9" fill="{BG0}" stroke="{HAIR2}"/>
    <text x="19.5" y="25" text-anchor="middle" font-family="{MONO}" font-size="15" font-weight="600" fill="{INK}" letter-spacing="0.5">AS</text>
  </g>

  <text x="100" y="62" font-family="{SANS}" font-size="36" font-weight="650" letter-spacing="-0.8" fill="{INK_HI}">Aditya Shrimali</text>

  <circle cx="102" cy="92" r="4" fill="{INK_HI}">
    <animate attributeName="opacity" values="0.35;0.95;0.35" dur="3.6s" repeatCount="indefinite"/>
    <animate attributeName="r" values="4;4.6;4" dur="3.6s" repeatCount="indefinite"/>
  </circle>
  <text x="116" y="96" font-family="{MONO}" font-size="13" fill="{INK_MUT}" letter-spacing="2">AI&#160;ENGINEER</text>

  <text x="834" y="44" text-anchor="end" font-family="{MONO}" font-size="11" fill="{INK_DIM}" letter-spacing="1">@just-brainwaves</text>

  <line x1="46" y1="206" x2="834" y2="206" stroke="{HAIR}"/>
  <text x="46" y="230" font-family="{MONO}" font-size="11" fill="{INK_DIM}" letter-spacing="0.5">RAG · LLM SYSTEMS · AGENTS · RETRIEVAL</text>
  <text x="834" y="230" text-anchor="end" font-family="{MONO}" font-size="11" fill="{INK_DIM}" letter-spacing="0.5">INDIA · UTC+5:30</text>
</svg>
'''
    open(f"{OUT}/hero.svg", "w").write(svg)
    print("hero.svg", len(svg))

# ====================================================================
# 2) PIPELINE — agentic RAG runtime: nodes + bezier edges + flowing packets
# ====================================================================
def pipeline():
    W, H = 880, 300
    # node: id -> (cx, cy, w, label, sublabel)
    N = {
        "q":   (78, 168, 78,  "query",     "in"),
        "emb": (232, 96, 90,  "embed",     "e5"),
        "vec": (232, 240, 96, "vector db", "pg"),
        "ret": (392, 168, 86, "retrieve",  "knn"),
        "ctx": (520, 168, 84, "context",   "topk"),
        "agt": (676, 168, 104,"agent · llm","run"),
        "tool":(676, 60, 78,  "tools",     "fn"),
        "mem": (676, 276, 84, "memory",    "kv"),
        "out": (818, 168, 86, "response",  "out"),
    }
    NH = 40
    def box(nid):
        cx, cy, w, lab, sub = N[nid]
        x, y = cx - w/2, cy - NH/2
        return f'''<g>
      <rect x="{f(x)}" y="{f(y)}" width="{w}" height="{NH}" rx="10" fill="{BG0}" stroke="{HAIR2}"/>
      <rect x="{f(x)}" y="{f(y)}" width="{w}" height="{NH}" rx="10" fill="none" stroke="{INK_HI}" stroke-opacity="0.0">
        <animate attributeName="stroke-opacity" values="0;0.22;0" dur="4.5s" begin="{f(-hash(nid)%40/10)}s" repeatCount="indefinite"/>
      </rect>
      <circle cx="{f(x+11)}" cy="{f(cy)}" r="2" fill="{INK_MUT}"/>
      <text x="{f(x+22)}" y="{f(cy-1)}" font-family="{MONO}" font-size="12" fill="{INK_HI}">{lab}</text>
      <text x="{f(x+w-9)}" y="{f(cy+13)}" text-anchor="end" font-family="{MONO}" font-size="8" fill="{INK_DIM}" letter-spacing="1">{sub}</text>
    </g>'''

    def edge_path(a, b):
        ax, ay, aw, *_ = N[a]; bx, by, bw, *_ = N[b]
        x0 = ax + aw/2; x1 = bx - bw/2
        # if b is above/below same column, exit right/enter left still ok; handle verticals
        if abs(bx - ax) < 6:   # vertical-ish (agent<->tool/mem)
            x0 = ax; x1 = bx
            y0 = ay + (NH/2 if by > ay else -NH/2)
            y1 = by + (-NH/2 if by > ay else NH/2)
            mx = (x0 + x1) / 2
            return f"M{f(x0)} {f(y0)} C{f(x0)} {f((y0+y1)/2)} {f(x1)} {f((y0+y1)/2)} {f(x1)} {f(y1)}"
        cxd = (x1 - x0) * 0.5
        return f"M{f(x0)} {f(ay)} C{f(x0+cxd)} {f(ay)} {f(x1-cxd)} {f(by)} {f(x1)} {f(by)}"

    edges = [
        ("q","emb"), ("q","vec"), ("emb","ret"), ("vec","ret"),
        ("ret","ctx"), ("ctx","agt"), ("agt","out"),
        ("agt","tool"), ("agt","mem"),
    ]
    edge_svgs, packet_svgs = [], []
    for i,(a,b) in enumerate(edges):
        p = edge_path(a,b)
        edge_svgs.append(f'<path d="{p}" fill="none" stroke="{HAIR2}" stroke-width="1"/>')
        dur = 3.2 + (i % 4) * 0.5
        for k in range(2):
            beg = -(k * dur/2) - (i*0.2)
            packet_svgs.append(
                f'<g><circle r="6" fill="{WHITE}" opacity="0.10"/><circle r="2.1" fill="{INK_HI}"/>'
                f'<animateMotion path="{p}" dur="{f(dur)}s" begin="{f(beg)}s" '
                f'keyPoints="0;1" keyTimes="0;1" calcMode="linear" repeatCount="indefinite"/></g>'
            )
    # feedback packets (tool->agent, mem->agent) going back
    for a,b in [("tool","agt"),("mem","agt")]:
        p = edge_path(a,b)
        packet_svgs.append(
            f'<g><circle r="5" fill="{WHITE}" opacity="0.08"/><circle r="1.8" fill="{INK_MUT}"/>'
            f'<animateMotion path="{p}" dur="3.6s" begin="-1.8s" repeatCount="indefinite"/></g>'
        )

    nodes = "\n    ".join(box(n) for n in N)
    edges_s = "\n    ".join(edge_svgs)
    packets_s = "\n    ".join(packet_svgs)

    # outer frame is larger than the graph design space; the graph is padded
    # in via a translate so the header and edges get breathing room.
    CW, CH = 960, 400          # canvas
    OX, OY = 30, 55            # graph offset inside the frame
    HX = CW - 40               # right-aligned header x

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" viewBox="0 0 {CW} {CH}" fill="none" role="img" aria-label="Agentic RAG runtime">
  <defs>
    <linearGradient id="pc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.7" fill="{HAIR2}" fill-opacity="0.5"/>
    </pattern>
    <clipPath id="pclip"><rect x="0.5" y="0.5" width="{CW-1}" height="{CH-1}" rx="18"/></clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{CW-1}" height="{CH-1}" rx="18" fill="url(#pc)" stroke="{HAIR}"/>
  <g clip-path="url(#pclip)">
    <rect x="0" y="0" width="{CW}" height="{CH}" fill="url(#dots)"/>
    <!-- header -->
    <circle cx="40" cy="30" r="3" fill="{INK_HI}"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.6s" repeatCount="indefinite"/></circle>
    <text x="54" y="34" font-family="{MONO}" font-size="12" fill="{INK_MUT}" letter-spacing="2">AGENTIC&#160;RAG&#160;·&#160;runtime</text>
    <text x="{HX}" y="34" text-anchor="end" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">stream ▸ live</text>
    <line x1="40" y1="48" x2="{HX}" y2="48" stroke="{HAIR}"/>
    <!-- graph -->
    <g transform="translate({OX}, {OY})">
      {edges_s}
      {nodes}
      {packets_s}
    </g>
  </g>
</svg>
'''
    open(f"{OUT}/pipeline-rag.svg", "w").write(svg)
    print("pipeline-rag.svg", len(svg))

# ====================================================================
# 3) GLOBE — rotating wireframe sphere (latent space) — generative art
# ====================================================================
def globe():
    W, H = 880, 250
    cx, cy = 440, 126
    R = 86
    meridians = 9
    dur = 14.0
    mer = []
    for i in range(meridians):
        beg = -(i / meridians) * dur
        # rx = R*|cos|: sample a half period for spinning illusion
        vals = "{0};{1};0;{1};{0};{1};0;{1};{0}".format(R, f(R*0.7071))
        op = 0.5 if i % 2 == 0 else 0.32
        mer.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{R}" ry="{R}" fill="none" stroke="{INK_MUT}" stroke-width="1" stroke-opacity="{op}">'
            f'<animate attributeName="rx" values="{vals}" keyTimes="0;0.125;0.25;0.375;0.5;0.625;0.75;0.875;1" '
            f'dur="{f(dur)}s" begin="{f(beg)}s" calcMode="spline" '
            f'keySplines="{";".join(["0.4 0 0.6 1"]*8)}" repeatCount="indefinite"/></ellipse>'
        )
    # latitudes (static, perspective-foreshortened horizontal ellipses)
    lat = []
    for j in range(1, 6):
        t = (j / 6) * 2 - 1            # -1..1 across sphere
        yy = cy + t * R * 0.86
        rx = math.sqrt(max(R*R - (t*R)**2, 0))
        ry = rx * 0.16 + 1
        lat.append(f'<ellipse cx="{cx}" cy="{f(yy)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" stroke="{HAIR2}" stroke-width="1" stroke-opacity="0.55"/>')
    # outline
    outline = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{INK_MUT}" stroke-opacity="0.6"/>'
    # orbiting satellites on tilted ellipse paths
    sats = []
    for k,(rx,ry,d,col) in enumerate([(120,34,9,INK_HI),(150,46,13,INK_MUT),(104,28,7,INK)]):
        path = f"M{cx-rx} {cy} a{rx} {ry} 0 1 0 {2*rx} 0 a{rx} {ry} 0 1 0 {-2*rx} 0"
        sats.append(
            f'<g><circle r="{4-k*0.6}" fill="{col}"/><circle r="9" fill="{WHITE}" opacity="0.07"/>'
            f'<animateMotion path="{path}" dur="{d}s" begin="{f(-k*2)}s" repeatCount="indefinite"/></g>'
        )
    # twinkles
    tw = []
    import random; random.seed(7)
    for _ in range(14):
        a = random.uniform(0, 2*math.pi); rr = random.uniform(0, R*0.92)
        px, py = cx + rr*math.cos(a), cy + rr*math.sin(a)*0.92
        d = random.uniform(2.5, 5)
        tw.append(f'<circle cx="{f(px)}" cy="{f(py)}" r="1" fill="{INK_HI}"><animate attributeName="opacity" values="0;0.8;0" dur="{f(d)}s" begin="{f(-random.uniform(0,d))}s" repeatCount="indefinite"/></circle>')

    mer_s = "\n    ".join(mer); lat_s = "\n    ".join(lat)
    sat_s = "\n    ".join(sats); tw_s = "\n    ".join(tw)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="latent space">
  <defs>
    <linearGradient id="gc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <radialGradient id="gcore" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{WHITE}" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="{WHITE}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="gclip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18"/></clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="url(#gc)" stroke="{HAIR}"/>
  <g clip-path="url(#gclip)">
    <text x="32" y="34" font-family="{MONO}" font-size="12" fill="{INK_MUT}" letter-spacing="2">LATENT&#160;SPACE</text>
    <text x="848" y="34" text-anchor="end" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">dim ▸ 1536</text>
    {lat_s}
    {mer_s}
    {outline}
    <circle cx="{cx}" cy="{cy}" r="26" fill="url(#gcore)"><animate attributeName="opacity" values="0.5;1;0.5" dur="4s" repeatCount="indefinite"/></circle>
    <circle cx="{cx}" cy="{cy}" r="3" fill="{INK_HI}"><animate attributeName="r" values="2.6;3.6;2.6" dur="4s" repeatCount="indefinite"/></circle>
    {tw_s}
    {sat_s}
    <text x="32" y="232" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">cos_sim ▸ retrieval</text>
    <text x="848" y="232" text-anchor="end" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">k=8 · hnsw</text>
  </g>
</svg>
'''
    open(f"{OUT}/globe.svg", "w").write(svg)
    print("globe.svg", len(svg))

# ====================================================================
# 4) STACK — monochrome pills + sweeping scan highlight
# ====================================================================
def stack():
    W, H = 880, 120
    pills = ["python","pytorch","langchain","go","rust","typescript","postgres","pgvector","docker"]
    # measure-ish
    def wf(s): return int(len(s)*7.4)+26
    x = 36; y = 58; row_y = [58, 90]; ri = 0; gx = 36
    items = []
    cur_x = gx
    cur_row = 0
    placed = []
    for s in pills:
        w = wf(s)
        if cur_x + w > W-36:
            cur_row += 1; cur_x = gx
        placed.append((cur_x, row_y[cur_row], w, s))
        cur_x += w + 10
    for px,py,w,s in placed:
        items.append(
            f'<g transform="translate({px},{py})">'
            f'<rect width="{w}" height="26" rx="8" fill="{BG0}" stroke="{HAIR2}"/>'
            f'<text x="{w/2:.0f}" y="17" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{INK}">{s}</text></g>'
        )
    items_s = "\n    ".join(items)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="Stack">
  <defs>
    <linearGradient id="stc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <linearGradient id="stscan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#fff" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="stclip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16"/></clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#stc)" stroke="{HAIR}"/>
  <g clip-path="url(#stclip)">
    <circle cx="36" cy="28" r="3" fill="{INK_HI}"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.6s" repeatCount="indefinite"/></circle>
    <text x="50" y="32" font-family="{MONO}" font-size="12" fill="{INK_MUT}" letter-spacing="2">STACK</text>
    <text x="844" y="32" text-anchor="end" font-family="{MONO}" font-size="11" fill="{INK_DIM}" letter-spacing="1">09 / TOOLS</text>
    <line x1="36" y1="44" x2="844" y2="44" stroke="{HAIR}"/>
    {items_s}
    <rect x="-220" y="44" width="220" height="{H-44}" fill="url(#stscan)">
      <animate attributeName="x" values="-220;{W}" dur="6.5s" begin="1s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
'''
    open(f"{OUT}/stack.svg", "w").write(svg)
    print("stack.svg", len(svg))

# ====================================================================
# 4.5) PROJECTS — clickable deployed-site cards (one SVG per project)
# ====================================================================
def projects():
    # name, tagline, short-domain, index
    cards = [
        ("portfolio",  "design + dev portfolio",      "portfolio.workers.dev",  "01"),
        ("whetstone",  "ai-assisted code editor",     "whetstone.workers.dev",  "02"),
        ("moonshrine", "hyprland desktop rice",        "moonshrine.workers.dev", "03"),
        ("strat",      "visual algo-trading platform", "strat.workers.dev",      "04"),
    ]
    W, H = 430, 132
    for name, tag, dom, idx in cards:
        pill_w = 78
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="{name} — {tag}">
  <defs>
    <linearGradient id="pjc" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/>
    </linearGradient>
    <linearGradient id="pjtop" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#fff" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="pjsheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#fff" stop-opacity="0.045"/>
      <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <pattern id="pjdots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.7" fill="{HAIR2}" fill-opacity="0.45"/>
    </pattern>
    <clipPath id="pjclip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16"/></clipPath>
  </defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#pjc)" stroke="{HAIR}"/>
  <g clip-path="url(#pjclip)">
    <rect x="0" y="0" width="{W}" height="{H}" fill="url(#pjdots)"/>
    <rect x="1" y="1" width="{W-2}" height="60" rx="15" fill="url(#pjtop)"/>
    <!-- header -->
    <circle cx="28" cy="28" r="3" fill="{INK_HI}"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="3.6s" repeatCount="indefinite"/></circle>
    <text x="40" y="32" font-family="{MONO}" font-size="10" fill="{INK_MUT}" letter-spacing="2">PROJECT</text>
    <text x="{W-22}" y="32" text-anchor="end" font-family="{MONO}" font-size="11" fill="{INK_DIM}" letter-spacing="1">{idx} / 04</text>
    <line x1="22" y1="44" x2="{W-22}" y2="44" stroke="{HAIR}"/>
    <!-- body -->
    <text x="22" y="84" font-family="{SANS}" font-size="26" font-weight="650" letter-spacing="-0.6" fill="{INK_HI}">{name}</text>
    <text x="22" y="106" font-family="{MONO}" font-size="11" fill="{INK_MUT}" letter-spacing="0.5">{tag}</text>
    <!-- footer -->
    <text x="22" y="{H-14}" font-family="{MONO}" font-size="9" fill="{INK_DIM}" letter-spacing="0.5">{dom}</text>
    <g transform="translate({W-pill_w-22},{H-32})">
      <rect width="{pill_w}" height="24" rx="8" fill="{BG0}" stroke="{HAIR2}"/>
      <rect width="{pill_w}" height="24" rx="8" fill="none" stroke="{INK_HI}" stroke-opacity="0">
        <animate attributeName="stroke-opacity" values="0;0.30;0" dur="3.2s" repeatCount="indefinite"/>
      </rect>
      <text x="{pill_w/2-6:.0f}" y="16" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{INK}" letter-spacing="1">VISIT</text>
      <path d="M{pill_w-22} 12 l5 0 m-2 -2.5 l2 2.5 l-2 2.5" stroke="{INK_HI}" stroke-width="1.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" repeatCount="indefinite"/>
      </path>
    </g>
    <rect x="-160" y="0" width="160" height="{H}" fill="url(#pjsheen)">
      <animate attributeName="x" values="-160;{W}" dur="7s" begin="{int(idx)*0.6}s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>
'''
        open(f"{OUT}/project-{name}.svg", "w").write(svg)
        print(f"project-{name}.svg", len(svg))

# ====================================================================
# 5) DIVIDER  &  6) FOOTER waveform signature
# ====================================================================
def divider():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="14" viewBox="0 0 880 14" fill="none" role="img" aria-label="divider">
  <defs><linearGradient id="dl" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#6b7280" stop-opacity="0"/>
    <stop offset="50%" stop-color="#6b7280" stop-opacity="0.30"/>
    <stop offset="100%" stop-color="#6b7280" stop-opacity="0"/></linearGradient></defs>
  <line x1="0" y1="7" x2="424" y2="7" stroke="url(#dl)"/>
  <line x1="456" y1="7" x2="880" y2="7" stroke="url(#dl)"/>
  <circle cx="440" cy="7" r="2.5" fill="{INK}"><animate attributeName="opacity" values="0.3;0.85;0.3" dur="3.6s" repeatCount="indefinite"/></circle>
</svg>
'''
    open(f"{OUT}/divider.svg","w").write(svg); print("divider.svg", len(svg))

def footer():
    W, H = 880, 96
    bars = []
    bx = 372; n = 47; sp = 9
    for i in range(n):
        x = bx + i*sp
        t = i/(n-1)
        base = 7 + 26*math.sin(math.pi*t)**0.85
        dur = 1.1 + 0.9*math.sin(i*1.7)**2
        h0 = 6; h1 = base
        bars.append(
            f'<rect x="{x}" y="{f(48-h0/2)}" width="3" height="{h0}" rx="1.5" fill="{INK_MUT}">'
            f'<animate attributeName="height" values="{f(h0)};{f(h1)};{f(h0)}" dur="{f(abs(dur))}s" begin="{f(-i*0.08)}s" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.4 0 0.6 1;0.4 0 0.6 1" repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{f(48-h0/2)};{f(48-h1/2)};{f(48-h0/2)}" dur="{f(abs(dur))}s" begin="{f(-i*0.08)}s" calcMode="spline" keyTimes="0;0.5;1" keySplines="0.4 0 0.6 1;0.4 0 0.6 1" repeatCount="indefinite"/></rect>'
        )
    bars_s = "\n    ".join(bars)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" fill="none" role="img" aria-label="footer">
  <defs><linearGradient id="ftc" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{BG0}"/><stop offset="100%" stop-color="{BG1}"/></linearGradient>
    <clipPath id="ftclip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16"/></clipPath></defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#ftc)" stroke="{HAIR}"/>
  <g clip-path="url(#ftclip)">
    <text x="36" y="44" font-family="{MONO}" font-size="13" fill="{INK_HI}" letter-spacing="0.5">aditya<tspan fill="{INK_DIM}">.</tspan>shrimali</text>
    <text x="36" y="64" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">always shipping · always learning</text>
    <text x="844" y="44" text-anchor="end" font-family="{MONO}" font-size="10" fill="{INK_DIM}" letter-spacing="1">© 2026</text>
    <line x1="340" y1="20" x2="340" y2="76" stroke="{HAIR}"/>
    {bars_s}
  </g>
</svg>
'''
    open(f"{OUT}/footer.svg","w").write(svg); print("footer.svg", len(svg))

hero(); pipeline(); globe(); stack(); projects(); divider(); footer()
print("done")

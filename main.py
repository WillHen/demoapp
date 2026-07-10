from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Czech Republic History — Hot Pink Edition")

HISTORY = (
    "From the early Slavic settlements of Bohemia and Moravia through the medieval "
    "Kingdom of Bohemia under the Přemyslid and Luxembourg dynasties, the Czech lands "
    "became a heart of Central European culture—crowned by Charles IV’s Prague and "
    "shaken by the Hussite Wars—before falling under Habsburg rule for centuries; "
    "after the collapse of Austria-Hungary in 1918, Czechoslovakia was born as a "
    "democratic republic, endured Nazi occupation and then decades of communist rule "
    "behind the Iron Curtain, and finally, through the Velvet Revolution of 1989 and "
    "the peaceful Velvet Divorce of 1993, emerged as today’s independent Czech Republic—"
    "a proud European democracy with Prague as its glittering capital."
)

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Czech Republic History ✨</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Outfit:wght@400;700;900&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --hot: #ff1493;
      --candy: #ff69b4;
      --blush: #ffb6c1;
      --bubble: #ff85c8;
      --neon: #ff00aa;
      --ink: #4a0028;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      min-height: 100vh;
      font-family: "Outfit", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(ellipse at 20% 20%, #ff9ad5 0%, transparent 45%),
        radial-gradient(ellipse at 80% 10%, #ff4db8 0%, transparent 40%),
        radial-gradient(ellipse at 50% 90%, #ff1493 0%, transparent 50%),
        linear-gradient(160deg, #ffe0f0 0%, #ff8cc8 40%, #ff2d95 100%);
      background-attachment: fixed;
      overflow-x: hidden;
      display: grid;
      place-items: center;
      padding: 2rem 1.25rem;
      position: relative;
    }}

    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      background-image:
        radial-gradient(circle, rgba(255,255,255,0.55) 1px, transparent 1px),
        radial-gradient(circle, rgba(255,20,147,0.35) 1.5px, transparent 1.5px);
      background-size: 48px 48px, 72px 72px;
      background-position: 0 0, 24px 36px;
      animation: drift 18s linear infinite;
      pointer-events: none;
      z-index: 0;
    }}

    @keyframes drift {{
      from {{ transform: translateY(0); }}
      to {{ transform: translateY(-72px); }}
    }}

    .sparkle {{
      position: fixed;
      width: 10px;
      height: 10px;
      background: white;
      border-radius: 50%;
      box-shadow: 0 0 12px 4px rgba(255, 255, 255, 0.9), 0 0 28px 8px rgba(255, 20, 147, 0.7);
      animation: twinkle 2.4s ease-in-out infinite;
      z-index: 1;
      pointer-events: none;
    }}

    .sparkle:nth-child(1) {{ top: 12%; left: 8%; animation-delay: 0s; }}
    .sparkle:nth-child(2) {{ top: 22%; right: 12%; animation-delay: 0.4s; }}
    .sparkle:nth-child(3) {{ bottom: 18%; left: 18%; animation-delay: 0.8s; }}
    .sparkle:nth-child(4) {{ bottom: 28%; right: 10%; animation-delay: 1.2s; }}
    .sparkle:nth-child(5) {{ top: 48%; left: 6%; animation-delay: 1.6s; }}

    @keyframes twinkle {{
      0%, 100% {{ opacity: 0.3; transform: scale(0.6); }}
      50% {{ opacity: 1; transform: scale(1.4); }}
    }}

    main {{
      position: relative;
      z-index: 2;
      width: min(720px, 100%);
      text-align: center;
      animation: pop-in 0.9s cubic-bezier(0.22, 1, 0.36, 1) both;
    }}

    @keyframes pop-in {{
      from {{ opacity: 0; transform: translateY(28px) scale(0.96); }}
      to {{ opacity: 1; transform: translateY(0) scale(1); }}
    }}

    .brand {{
      font-family: "Pacifico", cursive;
      font-size: clamp(2.6rem, 8vw, 4.4rem);
      line-height: 1.15;
      background: linear-gradient(90deg, #fff, #ffd6ec, #fff, #ff69b4, #fff);
      background-size: 200% auto;
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      animation: shimmer 3s linear infinite, bounce 2.5s ease-in-out infinite;
      text-shadow: 0 0 40px rgba(255, 0, 170, 0.55);
      filter: drop-shadow(0 4px 0 #ff1493) drop-shadow(0 8px 24px rgba(255, 20, 147, 0.45));
      margin-bottom: 0.75rem;
    }}

    @keyframes shimmer {{
      to {{ background-position: 200% center; }}
    }}

    @keyframes bounce {{
      0%, 100% {{ transform: translateY(0) rotate(-1deg); }}
      50% {{ transform: translateY(-8px) rotate(1deg); }}
    }}

    h1 {{
      font-size: clamp(1.15rem, 3.5vw, 1.55rem);
      font-weight: 900;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #fff;
      text-shadow: 0 2px 0 var(--hot), 0 0 20px rgba(255, 0, 170, 0.8);
      margin-bottom: 1.5rem;
      animation: pulse-glow 2s ease-in-out infinite;
    }}

    @keyframes pulse-glow {{
      0%, 100% {{ text-shadow: 0 2px 0 var(--hot), 0 0 16px rgba(255, 0, 170, 0.6); }}
      50% {{ text-shadow: 0 2px 0 var(--hot), 0 0 32px rgba(255, 255, 255, 0.95); }}
    }}

    .history {{
      font-size: clamp(1.05rem, 2.4vw, 1.2rem);
      line-height: 1.75;
      font-weight: 400;
      color: var(--ink);
      background: linear-gradient(135deg, rgba(255, 255, 255, 0.55), rgba(255, 182, 193, 0.35));
      backdrop-filter: blur(10px);
      border: 3px solid rgba(255, 255, 255, 0.75);
      border-radius: 1.5rem;
      padding: 1.75rem 1.5rem;
      box-shadow:
        0 0 0 4px rgba(255, 20, 147, 0.25),
        0 20px 50px rgba(255, 20, 147, 0.35),
        inset 0 1px 0 rgba(255, 255, 255, 0.8);
      animation: border-flash 3s ease-in-out infinite;
    }}

    @keyframes border-flash {{
      0%, 100% {{ box-shadow: 0 0 0 4px rgba(255, 20, 147, 0.25), 0 20px 50px rgba(255, 20, 147, 0.35); }}
      50% {{ box-shadow: 0 0 0 6px rgba(255, 0, 170, 0.55), 0 24px 60px rgba(255, 105, 180, 0.55); }}
    }}

    .flag {{
      display: inline-block;
      margin-top: 1.5rem;
      font-size: 2rem;
      animation: spin-y 4s ease-in-out infinite;
      filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.9));
    }}

    @keyframes spin-y {{
      0%, 100% {{ transform: rotateY(0deg) scale(1); }}
      50% {{ transform: rotateY(180deg) scale(1.15); }}
    }}

    @media (max-width: 480px) {{
      .history {{ padding: 1.25rem 1rem; border-radius: 1.1rem; }}
    }}
  </style>
</head>
<body>
  <span class="sparkle" aria-hidden="true"></span>
  <span class="sparkle" aria-hidden="true"></span>
  <span class="sparkle" aria-hidden="true"></span>
  <span class="sparkle" aria-hidden="true"></span>
  <span class="sparkle" aria-hidden="true"></span>

  <main>
    <p class="brand">Česko Flash</p>
    <h1>History of the Czech Republic</h1>
    <p class="history">{HISTORY}</p>
    <span class="flag" aria-hidden="true">💖</span>
  </main>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return PAGE


@app.get("/api/history")
def history_json() -> dict[str, str]:
    return {"title": "History of the Czech Republic", "paragraph": HISTORY}

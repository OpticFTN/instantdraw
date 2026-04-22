<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>instantdraw — README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0d0f14;
    --surface: #13161e;
    --border: #1e222e;
    --accent: #e8ff47;
    --accent2: #47c2ff;
    --text: #d4d8e8;
    --muted: #6b7394;
    --code-bg: #0a0c10;
    --green: #52e88a;
    --red: #ff6b6b;
    --radius: 8px;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    line-height: 1.75;
    min-height: 100vh;
  }

  /* NOISE OVERLAY */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
  }

  .wrapper {
    max-width: 860px;
    margin: 0 auto;
    padding: 60px 32px 100px;
    position: relative;
    z-index: 1;
  }

  /* HEADER */
  .header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 56px;
    flex-wrap: wrap;
  }

  .header-left { flex: 1; }

  .repo-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 5px 12px;
    border-radius: 20px;
    margin-bottom: 20px;
    letter-spacing: 0.02em;
  }

  .repo-tag::before {
    content: '';
    width: 6px; height: 6px;
    background: var(--green);
    border-radius: 50%;
    box-shadow: 0 0 6px var(--green);
  }

  h1 {
    font-size: clamp(42px, 7vw, 72px);
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1;
    color: #fff;
    margin-bottom: 16px;
  }

  h1 span { color: var(--accent); }

  .tagline {
    font-size: 16px;
    color: var(--muted);
    max-width: 520px;
  }

  /* LANG TOGGLE */
  .lang-toggle {
    display: flex;
    gap: 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
    align-self: flex-start;
    margin-top: 8px;
    flex-shrink: 0;
  }

  .lang-btn {
    padding: 10px 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.05em;
    cursor: pointer;
    border: none;
    background: transparent;
    color: var(--muted);
    transition: all 0.2s;
    text-transform: uppercase;
  }

  .lang-btn.active {
    background: var(--accent);
    color: #0d0f14;
  }

  .lang-btn:hover:not(.active) { color: var(--text); }

  /* BADGES */
  .badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 48px;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 5px 12px;
    border-radius: 4px;
    border: 1px solid var(--border);
    color: var(--muted);
    background: var(--surface);
  }

  .badge-dot { width: 6px; height: 6px; border-radius: 50%; }
  .dot-yellow { background: var(--accent); }
  .dot-blue { background: var(--accent2); }
  .dot-green { background: var(--green); }

  /* DIVIDER */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, var(--accent) 0%, transparent 60%);
    margin: 40px 0;
    opacity: 0.3;
  }

  /* SECTIONS */
  h2 {
    font-size: 22px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  h2 .icon {
    width: 32px; height: 32px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    flex-shrink: 0;
  }

  h3 {
    font-size: 16px;
    font-weight: 600;
    color: var(--accent);
    font-family: 'JetBrains Mono', monospace;
    margin: 28px 0 12px;
    letter-spacing: 0.02em;
  }

  p { color: var(--text); margin-bottom: 14px; }
  p:last-child { margin-bottom: 0; }

  strong { color: #fff; font-weight: 600; }

  /* CODE BLOCKS */
  pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: var(--radius);
    padding: 20px 24px;
    overflow-x: auto;
    margin: 16px 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.7;
    color: #c9d0e8;
  }

  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    background: var(--code-bg);
    border: 1px solid var(--border);
    padding: 2px 7px;
    border-radius: 4px;
    color: var(--accent2);
  }

  pre code {
    background: none;
    border: none;
    padding: 0;
    color: inherit;
  }

  /* STEPS */
  .steps { counter-reset: step; display: flex; flex-direction: column; gap: 16px; margin: 20px 0; }

  .step {
    display: flex;
    gap: 20px;
    align-items: flex-start;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px 24px;
    position: relative;
    overflow: hidden;
  }

  .step::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: var(--accent);
    opacity: 0.5;
  }

  .step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    background: rgba(232,255,71,0.08);
    border: 1px solid rgba(232,255,71,0.2);
    width: 28px; height: 28px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-body h4 { font-size: 14px; font-weight: 700; color: #fff; margin-bottom: 6px; }
  .step-body p { font-size: 14px; color: var(--muted); margin: 0; }

  /* TABLE */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 14px;
  }

  th {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
    text-align: left;
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
  }

  td {
    padding: 12px 16px;
    border-bottom: 1px solid rgba(30,34,46,0.6);
    color: var(--text);
    vertical-align: top;
  }

  tr:last-child td { border-bottom: none; }
  tr:hover td { background: var(--surface); }

  td:first-child { font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--accent2); }

  /* CALLOUT */
  .callout {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 18px 20px;
    border-radius: var(--radius);
    margin: 20px 0;
    font-size: 14px;
  }

  .callout-warn {
    background: rgba(255,107,107,0.06);
    border: 1px solid rgba(255,107,107,0.2);
    color: #ffaaaa;
  }

  .callout-tip {
    background: rgba(82,232,138,0.05);
    border: 1px solid rgba(82,232,138,0.2);
    color: #9affc5;
  }

  .callout-info {
    background: rgba(71,194,255,0.05);
    border: 1px solid rgba(71,194,255,0.2);
    color: #9ad8ff;
  }

  .callout-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
  .callout p { margin: 0; }

  /* CONTRIBUTE BOX */
  .contribute-box {
    background: linear-gradient(135deg, rgba(232,255,71,0.04) 0%, rgba(71,194,255,0.04) 100%);
    border: 1px solid rgba(232,255,71,0.15);
    border-radius: 12px;
    padding: 32px;
    margin-top: 20px;
  }

  .contribute-box h3 {
    color: var(--accent);
    margin-top: 0;
  }

  .ideas-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
    margin-top: 16px;
  }

  .idea-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 14px 16px;
    font-size: 13px;
    color: var(--muted);
    transition: border-color 0.2s, color 0.2s;
  }

  .idea-card:hover { border-color: var(--accent); color: var(--text); }
  .idea-card strong { color: var(--accent2); display: block; margin-bottom: 4px; font-size: 13px; }

  /* FILE TREE */
  .file-tree {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 2;
  }

  .file-tree .dir { color: var(--accent2); }
  .file-tree .file { color: var(--text); }
  .file-tree .comment { color: var(--muted); }
  .file-tree .required { color: var(--accent); }

  /* STOP TABLE */
  .stop-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }

  .stop-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
  }

  .stop-card .method {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--muted);
    margin-bottom: 8px;
  }

  .stop-card .key {
    font-size: 20px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 8px;
  }

  .stop-card p { font-size: 13px; color: var(--muted); margin: 0; }

  /* SECTION WRAPPER */
  .section { margin-bottom: 52px; }

  /* FOOTER */
  footer {
    margin-top: 80px;
    padding-top: 28px;
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
  }

  footer p { font-size: 13px; color: var(--muted); margin: 0; }
  footer a { color: var(--accent); text-decoration: none; }

  /* LANG TOGGLE */
  [data-lang] { display: none; }
  body.lang-en [data-lang="en"] { display: block; }
  body.lang-fr [data-lang="fr"] { display: block; }
  body.lang-en [data-lang="both"] { display: block; }
  body.lang-fr [data-lang="both"] { display: block; }
  body.lang-en .lang-btn[data-target="en"] { background: var(--accent); color: #0d0f14; }
  body.lang-fr .lang-btn[data-target="fr"] { background: var(--accent); color: #0d0f14; }
  body.lang-en .lang-btn[data-target="fr"] { background: transparent; color: var(--muted); }
  body.lang-fr .lang-btn[data-target="en"] { background: transparent; color: var(--muted); }

  /* inline lang spans */
  span[data-lang] { display: none; }
  body.lang-en span[data-lang="en"] { display: inline; }
  body.lang-fr span[data-lang="fr"] { display: inline; }

  @media (max-width: 600px) {
    .stop-grid { grid-template-columns: 1fr; }
    .header { flex-direction: column; }
    .lang-toggle { align-self: flex-start; }
  }
</style>
</head>
<body class="lang-en">
<div class="wrapper">

  <!-- HEADER -->
  <div class="header">
    <div class="header-left">
      <div class="repo-tag">github.com/your-username/instantdraw</div>
      <h1>instant<span>draw</span></h1>
      <p class="tagline">
        <span data-lang="en">A Python bot that traces any image directly on screen using automated mouse control.</span>
        <span data-lang="fr">Un bot Python qui retrace n'importe quelle image directement à l'écran via le contrôle automatique de la souris.</span>
      </p>
    </div>
    <div>
      <div class="lang-toggle">
        <button class="lang-btn" data-target="en" onclick="setLang('en')">EN</button>
        <button class="lang-btn" data-target="fr" onclick="setLang('fr')">FR</button>
      </div>
    </div>
  </div>

  <!-- BADGES -->
  <div class="badges">
    <span class="badge"><span class="badge-dot dot-yellow"></span>Python 3.7+</span>
    <span class="badge"><span class="badge-dot dot-blue"></span>OpenCV · PyAutoGUI · Keyboard</span>
    <span class="badge"><span class="badge-dot dot-green"></span>
      <span data-lang="en">Tested on BlueStacks 5</span>
      <span data-lang="fr">Testé sur BlueStacks 5</span>
    </span>
    <span class="badge"><span class="badge-dot dot-yellow"></span>
      <span data-lang="en">Open for contributions</span>
      <span data-lang="fr">Contributions bienvenues</span>
    </span>
  </div>

  <!-- HOW IT WORKS -->
  <div class="section">
    <h2><span class="icon">⚙️</span>
      <span data-lang="en">How It Works</span>
      <span data-lang="fr">Fonctionnement</span>
    </h2>

    <div data-lang="en">
      <p>instantdraw processes your image through a computer vision pipeline, then replays it as real mouse strokes on any drawing surface — tested on <strong>BlueStacks 5</strong> with Instagram's <strong>Direct Message drawing feature</strong> (the brush tool inside conversations, not Stories).</p>
    </div>
    <div data-lang="fr">
      <p>instantdraw traite votre image via un pipeline de vision par ordinateur, puis la rejoue sous forme de vrais mouvements de souris sur n'importe quelle surface de dessin — testé sur <strong>BlueStacks 5</strong> avec la <strong>fonctionnalité de dessin dans les messages directs Instagram</strong> (l'outil pinceau dans les conversations, pas les Stories).</p>
    </div>

    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-body">
          <h4><span data-lang="en">Grayscale conversion</span><span data-lang="fr">Conversion en niveaux de gris</span></h4>
          <p><span data-lang="en">The image is converted to black and white using OpenCV.</span><span data-lang="fr">L'image est convertie en noir et blanc via OpenCV.</span></p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-body">
          <h4><span data-lang="en">Adaptive resizing</span><span data-lang="fr">Redimensionnement adaptatif</span></h4>
          <p><span data-lang="en">The image is scaled to 50% of your screen height while preserving the aspect ratio.</span><span data-lang="fr">L'image est mise à l'échelle à 50% de la hauteur d'écran en conservant le ratio.</span></p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-body">
          <h4><span data-lang="en">Canny edge detection</span><span data-lang="fr">Détection de contours Canny</span></h4>
          <p><span data-lang="en">Edges are extracted using Canny (thresholds 50–150), isolating lines and shapes.</span><span data-lang="fr">Les contours sont extraits avec Canny (seuils 50–150), isolant lignes et formes.</span></p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <div class="step-body">
          <h4><span data-lang="en">Contour extraction</span><span data-lang="fr">Extraction des chemins connectés</span></h4>
          <p><span data-lang="en">OpenCV groups edge pixels into connected paths (contours) that the mouse will follow.</span><span data-lang="fr">OpenCV regroupe les pixels en chemins connectés que la souris va suivre.</span></p>
        </div>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <div class="step-body">
          <h4><span data-lang="en">Centered mouse drawing</span><span data-lang="fr">Dessin centré à la souris</span></h4>
          <p><span data-lang="en">Each contour is replayed as a click-drag stroke, perfectly centered on screen.</span><span data-lang="fr">Chaque contour est rejoué comme un trait cliqué-glissé, parfaitement centré à l'écran.</span></p>
        </div>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- REQUIREMENTS & INSTALL -->
  <div class="section">
    <h2><span class="icon">📦</span>
      <span data-lang="en">Installation</span>
      <span data-lang="fr">Installation</span>
    </h2>

    <h3><span data-lang="en">1 — Clone the repository</span><span data-lang="fr">1 — Cloner le dépôt</span></h3>
    <pre><code>git clone https://github.com/your-username/instantdraw.git
cd instantdraw</code></pre>

    <h3><span data-lang="en">2 — Install dependencies</span><span data-lang="fr">2 — Installer les dépendances</span></h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <div data-lang="en">
      <div class="callout callout-info">
        <span class="callout-icon">🐧</span>
        <p>On Linux, <code>pyautogui</code> requires additional system packages:<br>
        <code>sudo apt-get install python3-tk python3-dev scrot</code></p>
      </div>
    </div>
    <div data-lang="fr">
      <div class="callout callout-info">
        <span class="callout-icon">🐧</span>
        <p>Sur Linux, <code>pyautogui</code> nécessite des paquets système supplémentaires :<br>
        <code>sudo apt-get install python3-tk python3-dev scrot</code></p>
      </div>
    </div>

    <h3><span data-lang="en">3 — Add your image</span><span data-lang="fr">3 — Ajouter votre image</span></h3>
    <div data-lang="en"><p>Place the image you want to draw in the project folder and name it <code>image.png</code>. This is the only file the bot looks for by default.</p></div>
    <div data-lang="fr"><p>Placez l'image à dessiner dans le dossier du projet et nommez-la <code>image.png</code>. C'est le seul fichier que le bot cherche par défaut.</p></div>
  </div>

  <div class="divider"></div>

  <!-- USAGE -->
  <div class="section">
    <h2><span class="icon">▶️</span>
      <span data-lang="en">Usage</span>
      <span data-lang="fr">Utilisation</span>
    </h2>

    <div data-lang="en">
      <p><strong>Recommended setup with BlueStacks 5 + Instagram DMs:</strong></p>
      <ol style="padding-left:20px; color: var(--muted); font-size:14px; line-height:2.2;">
        <li>Open <strong>BlueStacks 5</strong> and launch Instagram.</li>
        <li>Open a conversation and tap the <strong>drawing brush icon</strong> inside the message input area.</li>
        <li>Select a <strong>thin brush</strong> and a dark color for best results.</li>
        <li>Run the bot: <code>python bot.py</code></li>
        <li>Switch back to BlueStacks — you have <strong>5 seconds</strong> before drawing starts.</li>
      </ol>
    </div>
    <div data-lang="fr">
      <p><strong>Configuration recommandée avec BlueStacks 5 + Instagram DMs :</strong></p>
      <ol style="padding-left:20px; color: var(--muted); font-size:14px; line-height:2.2;">
        <li>Ouvrez <strong>BlueStacks 5</strong> et lancez Instagram.</li>
        <li>Ouvrez une conversation et appuyez sur l'<strong>icône pinceau</strong> dans la zone de saisie de message.</li>
        <li>Choisissez un <strong>pinceau fin</strong> et une couleur foncée pour de meilleurs résultats.</li>
        <li>Lancez le bot : <code>python bot.py</code></li>
        <li>Repassez sur BlueStacks — vous avez <strong>5 secondes</strong> avant que le dessin commence.</li>
      </ol>
    </div>

    <div data-lang="en">
      <div class="callout callout-warn">
        <span class="callout-icon">⚠️</span>
        <p>This bot <strong>takes full control of your mouse</strong> during drawing. Do not use your computer for anything else in the meantime.</p>
      </div>
    </div>
    <div data-lang="fr">
      <div class="callout callout-warn">
        <span class="callout-icon">⚠️</span>
        <p>Ce bot <strong>prend le contrôle total de votre souris</strong> pendant le dessin. N'utilisez pas votre ordinateur pour autre chose entre-temps.</p>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- CONFIGURATION -->
  <div class="section">
    <h2><span class="icon">🔧</span>
      <span data-lang="en">Configuration & Tuning</span>
      <span data-lang="fr">Configuration & Réglages</span>
    </h2>

    <div data-lang="en">
      <p>Every image is different — you may need to adjust these values in <code>bot.py</code> to get the best result for your specific drawing surface or image type. There is no single perfect setting.</p>
    </div>
    <div data-lang="fr">
      <p>Chaque image est différente — il vous faudra peut-être ajuster ces valeurs dans <code>bot.py</code> pour obtenir le meilleur résultat selon votre surface de dessin ou type d'image. Il n'existe pas de réglage parfait universel.</p>
    </div>

    <table>
      <thead>
        <tr>
          <th><span data-lang="en">Parameter</span><span data-lang="fr">Paramètre</span></th>
          <th><span data-lang="en">Default</span><span data-lang="fr">Défaut</span></th>
          <th><span data-lang="en">Description</span><span data-lang="fr">Description</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>pyautogui.PAUSE</td>
          <td>0.010</td>
          <td><span data-lang="en">Delay between each mouse move. Lower = faster but riskier. Try <code>0.005</code>–<code>0.02</code>.</span><span data-lang="fr">Délai entre chaque mouvement. Plus bas = plus rapide mais risqué. Essayez entre <code>0.005</code> et <code>0.02</code>.</span></td>
        </tr>
        <tr>
          <td>max_size</td>
          <td>50% screen height</td>
          <td><span data-lang="en">Controls how large the drawing appears. Increase for more detail.</span><span data-lang="fr">Contrôle la taille du dessin. Augmentez pour plus de détails.</span></td>
        </tr>
        <tr>
          <td>Canny low / high</td>
          <td>50 / 150</td>
          <td><span data-lang="en">Edge detection sensitivity. Lower values = more edges detected = more detail.</span><span data-lang="fr">Sensibilité de détection. Valeurs plus basses = plus de contours = plus de détails.</span></td>
        </tr>
        <tr>
          <td>image filename</td>
          <td>"image.png"</td>
          <td><span data-lang="en">Change to any <code>.png</code> or <code>.jpg</code> path.</span><span data-lang="fr">Changez vers n'importe quel chemin <code>.png</code> ou <code>.jpg</code>.</span></td>
        </tr>
      </tbody>
    </table>

    <div data-lang="en">
      <div class="callout callout-tip">
        <span class="callout-icon">💡</span>
        <p><strong>Tip:</strong> If the drawing looks too cluttered, raise the Canny thresholds (e.g. <code>80, 200</code>). If it's too sparse, lower them (e.g. <code>30, 100</code>). Every image needs its own sweet spot.</p>
      </div>
    </div>
    <div data-lang="fr">
      <div class="callout callout-tip">
        <span class="callout-icon">💡</span>
        <p><strong>Astuce :</strong> Si le dessin est trop chargé, augmentez les seuils Canny (ex : <code>80, 200</code>). S'il est trop vide, baissez-les (ex : <code>30, 100</code>). Chaque image a son propre réglage idéal.</p>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- STOPPING -->
  <div class="section">
    <h2><span class="icon">🛑</span>
      <span data-lang="en">Stopping the Bot</span>
      <span data-lang="fr">Arrêter le bot</span>
    </h2>

    <div class="stop-grid">
      <div class="stop-card">
        <div class="method"><span data-lang="en">Method 1</span><span data-lang="fr">Méthode 1</span></div>
        <div class="key">SPACE</div>
        <p><span data-lang="en">Hold down the Space key at any time for a clean stop.</span><span data-lang="fr">Maintenez la touche Espace pour un arrêt propre.</span></p>
      </div>
      <div class="stop-card">
        <div class="method"><span data-lang="en">Method 2 — Fail-Safe</span><span data-lang="fr">Méthode 2 — Sécurité</span></div>
        <div class="key" style="font-size:15px;">↖ Corner</div>
        <p><span data-lang="en">Move your mouse to the top-left corner of the screen rapidly to trigger PyAutoGUI's built-in fail-safe.</span><span data-lang="fr">Déplacez rapidement votre souris vers le coin supérieur gauche de l'écran pour déclencher la sécurité intégrée de PyAutoGUI.</span></p>
      </div>
    </div>

    <div data-lang="en"><p style="font-size:13px; color:var(--muted)">Both methods safely release the mouse button before stopping.</p></div>
    <div data-lang="fr"><p style="font-size:13px; color:var(--muted)">Les deux méthodes relâchent la souris en toute sécurité avant de s'arrêter.</p></div>
  </div>

  <div class="divider"></div>

  <!-- TIPS -->
  <div class="section">
    <h2><span class="icon">✨</span>
      <span data-lang="en">Tips for Best Results</span>
      <span data-lang="fr">Conseils pour de meilleurs résultats</span>
    </h2>

    <table>
      <thead>
        <tr>
          <th><span data-lang="en">Tip</span><span data-lang="fr">Conseil</span></th>
          <th><span data-lang="en">Why</span><span data-lang="fr">Pourquoi</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span data-lang="en">Use a thin brush</span><span data-lang="fr">Pinceau fin</span></td>
          <td><span data-lang="en">The bot draws outlines only — thin strokes look much sharper.</span><span data-lang="fr">Le bot dessine uniquement des contours — les traits fins donnent un rendu bien plus net.</span></td>
        </tr>
        <tr>
          <td><span data-lang="en">Use high-contrast images</span><span data-lang="fr">Images à fort contraste</span></td>
          <td><span data-lang="en">Logos, portraits, and line art give the best edge detection results.</span><span data-lang="fr">Logos, portraits et dessins au trait donnent les meilleurs résultats en détection de contours.</span></td>
        </tr>
        <tr>
          <td><span data-lang="en">Don't touch the canvas</span><span data-lang="fr">Ne pas bouger le canvas</span></td>
          <td><span data-lang="en">Any scroll or pan while the bot runs will misalign all strokes.</span><span data-lang="fr">Tout défilement ou panoramique pendant l'exécution décalera tous les traits.</span></td>
        </tr>
        <tr>
          <td><span data-lang="en">Close other windows</span><span data-lang="fr">Fermer les autres fenêtres</span></td>
          <td><span data-lang="en">Pop-ups that steal focus will break the drawing mid-run.</span><span data-lang="fr">Les pop-ups qui volent le focus interrompront le dessin en cours d'exécution.</span></td>
        </tr>
        <tr>
          <td><span data-lang="en">Test on a blank canvas first</span><span data-lang="fr">Tester sur un canvas vierge d'abord</span></td>
          <td><span data-lang="en">Verify positioning and scale before drawing on your actual target.</span><span data-lang="fr">Vérifiez le positionnement et l'échelle avant de dessiner sur votre cible réelle.</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="divider"></div>

  <!-- CONTRIBUTING -->
  <div class="section">
    <h2><span class="icon">🤝</span>
      <span data-lang="en">Contributing</span>
      <span data-lang="fr">Contribuer</span>
    </h2>

    <div data-lang="en">
      <p>instantdraw is a solid foundation, but there is a <strong>lot of room to improve it</strong>. Whether you want to add a feature, fix a bug, or experiment with a new drawing technique, contributions are very welcome. Feel free to open a pull request or an issue on GitHub.</p>
    </div>
    <div data-lang="fr">
      <p>instantdraw est une base solide, mais il y a <strong>énormément de marge pour l'améliorer</strong>. Que vous souhaitiez ajouter une fonctionnalité, corriger un bug ou expérimenter une nouvelle technique de dessin, les contributions sont très bienvenues. N'hésitez pas à ouvrir une pull request ou une issue sur GitHub.</p>
    </div>

    <div class="contribute-box">
      <h3><span data-lang="en">💡 Ideas for improvement</span><span data-lang="fr">💡 Idées d'amélioration</span></h3>
      <div data-lang="en">
        <div class="ideas-grid">
          <div class="idea-card"><strong>Color support</strong>Detect dominant colors and switch the brush automatically.</div>
          <div class="idea-card"><strong>GUI launcher</strong>A simple interface to pick the image and adjust settings without editing code.</div>
          <div class="idea-card"><strong>Speed control</strong>A real-time slider to speed up or slow down drawing mid-run.</div>
          <div class="idea-card"><strong>Progress indicator</strong>Show how many contours remain and an estimated time left.</div>
          <div class="idea-card"><strong>Preview mode</strong>Show what the bot will draw before it actually starts.</div>
          <div class="idea-card"><strong>Multi-platform testing</strong>Test and document compatibility with other Android emulators or drawing apps.</div>
        </div>
      </div>
      <div data-lang="fr">
        <div class="ideas-grid">
          <div class="idea-card"><strong>Support couleur</strong>Détecter les couleurs dominantes et changer de pinceau automatiquement.</div>
          <div class="idea-card"><strong>Interface graphique</strong>Une interface simple pour choisir l'image et ajuster les réglages sans toucher au code.</div>
          <div class="idea-card"><strong>Contrôle de vitesse</strong>Un curseur en temps réel pour accélérer ou ralentir le dessin en cours d'exécution.</div>
          <div class="idea-card"><strong>Indicateur de progression</strong>Afficher les contours restants et une estimation du temps.</div>
          <div class="idea-card"><strong>Mode prévisualisation</strong>Montrer ce que le bot va dessiner avant de commencer.</div>
          <div class="idea-card"><strong>Tests multi-plateformes</strong>Tester et documenter la compatibilité avec d'autres émulateurs ou applis de dessin.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- PROJECT STRUCTURE -->
  <div class="section">
    <h2><span class="icon">📁</span>
      <span data-lang="en">Project Structure</span>
      <span data-lang="fr">Structure du projet</span>
    </h2>

    <div class="file-tree">
      <div><span class="dir">instantdraw/</span></div>
      <div>&nbsp;&nbsp;├── <span class="file">bot.py</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment"># <span data-lang="en">Main bot script</span><span data-lang="fr">Script principal du bot</span></span></div>
      <div>&nbsp;&nbsp;├── <span class="required">image.png</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment"># <span data-lang="en">⚠ Your source image — required</span><span data-lang="fr">⚠ Votre image source — obligatoire</span></span></div>
      <div>&nbsp;&nbsp;├── <span class="file">requirements.txt</span> &nbsp;&nbsp;<span class="comment"># <span data-lang="en">Python dependencies</span><span data-lang="fr">Dépendances Python</span></span></div>
      <div>&nbsp;&nbsp;└── <span class="file">README.html</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="comment"># <span data-lang="en">This file</span><span data-lang="fr">Ce fichier</span></span></div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer>
    <p>
      <span data-lang="en">Made with Python · Open source · <a href="https://github.com/your-username/instantdraw">github.com/your-username/instantdraw</a></span>
      <span data-lang="fr">Fait avec Python · Open source · <a href="https://github.com/your-username/instantdraw">github.com/your-username/instantdraw</a></span>
    </p>
    <p style="font-size:12px;">
      <span data-lang="en">instantdraw is an open project — feel free to fork, improve, and share.</span>
      <span data-lang="fr">instantdraw est un projet ouvert — forkez, améliorez, et partagez librement.</span>
    </p>
  </footer>

</div>

<script>
  function setLang(lang) {
    document.body.className = 'lang-' + lang;
  }
</script>
</body>
</html>

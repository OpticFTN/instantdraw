# InstantDraw

[English](#english) | [Français](#français)

A Python bot that automatically draws an image on your screen by simulating mouse movements.  
It is designed for any app or canvas that lets you draw with the mouse, including **messaging / conversation drawing features**, simple drawing tools, and emulator-based environments.

> Tested with **BlueStacks 5**.

---

## English

### What It Does

InstantDraw takes an image and tries to reproduce its outlines on a drawing surface by controlling the mouse automatically.

It is useful for:
- simple drawing canvases,
- chat or conversation drawing tools,
- desktop drawing apps,
- Android emulators such as BlueStacks.

It is **not limited to one platform**, as long as the target accepts mouse input.

---

### How It Works

The bot follows a basic image-processing pipeline:

1. **Convert to grayscale**  
   The image is transformed into black and white.

2. **Resize**  
   The image is scaled to fit a target drawing area while keeping the aspect ratio.

3. **Detect edges**  
   Canny Edge Detection is used to extract visible contours and important lines.

4. **Find contours**  
   OpenCV identifies connected paths in the processed image.

5. **Map to screen coordinates**  
   The contours are centered and positioned on the drawing surface.

6. **Simulate mouse drawing**  
   The bot presses the mouse button, drags along each contour, then releases it.

---

### Requirements

- Python 3.7+
- Packages listed in `requirements.txt`

```txt
opencv-python
numpy
pyautogui
keyboard
````

---

### Installation

#### 1) Clone the repository

```bash
git clone https://github.com/your-username/instantdraw.git
cd instantdraw
```

#### 2) Install dependencies

```bash
pip install -r requirements.txt
```

On Linux, `pyautogui` may require extra packages:

```bash
sudo apt-get install python3-tk python3-dev scrot
```

#### 3) Add your image

Place the image you want to draw in the project folder and name it:

```txt
image.png
```

You can change the filename in the configuration if needed.

---

### Usage

1. Open the target app or canvas.
2. Make sure the drawing area is visible and focused.
3. Run the bot:

```bash
python bot.py
```

4. Switch to the target window during the countdown.

The bot will start drawing automatically after a short delay.

---

### Configuration

Several values can be adjusted in `bot.py`.

| Variable          |                Default | Meaning                                                       |
| ----------------- | ---------------------: | ------------------------------------------------------------- |
| `pyautogui.PAUSE` |                `0.010` | Delay between mouse actions. Lower = faster, but less stable. |
| Resize limit      | `50% of screen height` | Maximum size used for the drawing.                            |
| Canny thresholds  |              `50, 150` | Edge detection sensitivity. Lower = more details.             |
| Input filename    |            `image.png` | Source image used by the bot.                                 |

---

### Important Notes

This project is intentionally simple, which means it is **meant to be improved**.

People can tune it in many ways:

* better contour simplification,
* smoother stroke generation,
* better resizing logic,
* adaptive threshold values,
* brush-size calibration,
* smarter handling of complex images,
* better timing for slower apps or emulators.

In practice, you will often need to change some values depending on:

* the app you are using,
* the brush size,
* the screen resolution,
* the emulator or window scaling,
* the speed of mouse input handling.

That is normal. The bot is **configurable and improvable**, not a one-size-fits-all solution.

---

### Tested Environment

This project was tested with:

* **BlueStacks 5**

It may also work in other environments, but results can vary depending on how mouse input is handled.

---

### Stopping the Bot

You can stop the bot safely in two ways:

| Method                  | How it works                                                 |
| ----------------------- | ------------------------------------------------------------ |
| **Space key**           | Hold `SPACE` to stop the bot cleanly.                        |
| **PyAutoGUI fail-safe** | Move the mouse quickly to the top-left corner of the screen. |

The bot should release the mouse button before stopping.

---

### Tips for Better Results

* Use a **thin brush**.
* Prefer **high-contrast images**.
* Avoid very detailed photos; line art works better.
* Keep the canvas centered and do not pan or scroll while drawing.
* Reduce `pyautogui.PAUSE` carefully if you want faster output.
* Test and adjust the values depending on the target app.

---

### Project Structure

```txt
instantdraw/
├── bot.py
├── requirements.txt
├── image.png
└── README.md
```

---

### Disclaimer

InstantDraw controls your mouse automatically.
Use it carefully and keep the stop methods ready in case you need to interrupt it.

This project is provided as a practical automation tool and is intended to be modified, tuned, and improved by users.

---

## Français

### Ce que fait le projet

InstantDraw prend une image et essaie de la reproduire sous forme de contours en contrôlant automatiquement la souris.

Il peut servir pour :

* des canvas de dessin simples,
* des outils de dessin dans une conversation ou un chat,
* des applications de dessin sur ordinateur,
* des émulateurs Android comme BlueStacks.

Il ne dépend pas d’une seule plateforme, tant que l’application accepte les mouvements de souris.

---

### Comment ça marche

Le bot suit une chaîne de traitement simple :

1. **Conversion en niveaux de gris**
   L’image est transformée en noir et blanc.

2. **Redimensionnement**
   L’image est adaptée à une zone de dessin cible en gardant les proportions.

3. **Détection des bords**
   La détection de contours de Canny sert à extraire les lignes visibles importantes.

4. **Extraction des contours**
   OpenCV repère les chemins continus dans l’image traitée.

5. **Placement à l’écran**
   Les contours sont centrés et placés sur la zone de dessin.

6. **Simulation du dessin**
   Le bot appuie sur le clic, suit les contours, puis relâche.

---

### Remarques importantes

Ce projet est volontairement simple, donc il est **fait pour être amélioré**.

On peut l’améliorer en :

* simplifiant mieux les contours,
* rendant les traits plus fluides,
* améliorant le redimensionnement,
* adaptant automatiquement les seuils,
* calibrant la taille du pinceau,
* gérant mieux les images complexes,
* ajustant les délais selon l’application utilisée.

En pratique, il faut souvent modifier certaines valeurs selon :

* l’application utilisée,
* la taille du pinceau,
* la résolution de l’écran,
* le zoom de l’émulateur ou de la fenêtre,
* la vitesse à laquelle la souris est traitée.

C’est normal : le bot est **modifiable et améliorable**.

---

### Environnement testé

Ce projet a été testé avec :

* **BlueStacks 5**

Il peut aussi fonctionner ailleurs, mais le résultat dépend de la manière dont l’application gère les entrées souris.

---

### Arrêter le bot

Deux méthodes permettent de l’arrêter proprement :

| Méthode                 | Fonctionnement                                               |
| ----------------------- | ------------------------------------------------------------ |
| **Touche Espace**       | Maintenir `SPACE` pour arrêter le bot proprement.            |
| **Fail-safe PyAutoGUI** | Déplacer rapidement la souris dans le coin supérieur gauche. |

Le bot doit relâcher le clic avant de s’arrêter.

---

### Conseils pour de meilleurs résultats

* Utiliser un **pinceau fin**.
* Préférer des images à **fort contraste**.
* Éviter les photos très détaillées ; les dessins simples marchent mieux.
* Garder le canvas centré et ne pas déplacer la zone pendant le dessin.
* Baisser `pyautogui.PAUSE` avec prudence si tu veux aller plus vite.
* Tester et ajuster les paramètres selon l’application cible.

---

### Structure du projet

```txt
instantdraw/
├── bot.py
├── requirements.txt
├── image.png
└── README.md
```

---

### Avertissement

InstantDraw prend le contrôle de la souris automatiquement.
Utilise-le avec prudence et garde toujours une méthode d’arrêt rapide disponible.

Le projet est conçu comme un outil d’automatisation pratique, et il est fait pour être modifié, réglé et amélioré.

```

Si tu veux, je peux aussi te faire une **:contentReference[oaicite:0]{index=0}** avec badges, GIF, screenshot, et un style plus clean.
```

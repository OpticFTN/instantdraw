import cv2
import numpy as np
import pyautogui
import time
import keyboard

# We reduce the pause time so the bot draws faster
pyautogui.PAUSE = 0.010 

print("In 5 seconds, the drawing will start.")
print("WARNING: For better details, choose a THIN brush on Instagram before the bot starts!")
time.sleep(5)

# Load the image
img = cv2.imread("image.png")
if img is None:
    print("Error: Unable to find 'image.png'. Please check the file name.")
    exit()

# 1. Convert the image to grayscale (black and white)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# Get the screen size to adapt the drawing
screen_w, screen_h = pyautogui.size()

# 2. Resize the image (50% of the screen size)
max_size = int(screen_h * 0.50)
scale = max_size / max(h, w)
new_w = int(w * scale)
new_h = int(h * scale)
gray = cv2.resize(gray, (new_w, new_h))

# 3. Better detail detection (Canny Edge Detection with lower thresholds)
edges = cv2.Canny(gray, 50, 150)

# 4. Find the "contours" (the connected paths)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 5. Calculate coordinates to PERFECTLY CENTER the drawing on screen
start_x = (screen_w - new_w) // 2
start_y = (screen_h - new_h) // 2

print(f"Starting to draw (Size: {new_w}x{new_h})! There are {len(contours)} lines to trace.")
print("WARNING: HOLD DOWN THE 'SPACE' KEY TO FORCE-STOP THE DRAWING!")

try:
    for contour in contours:
        # If there is more than one point in the path, we can draw a line
        if len(contour) > 1:
            # Check if the user is pressing space between two lines
            if keyboard.is_pressed('space'):
                raise Exception("The bot was stopped by the user (Space key).")
                
            first_point = contour[0][0]
            # Move to the first point of the line
            pyautogui.moveTo(start_x + first_point[0], start_y + first_point[1])
            # Hold down the mouse button to start drawing
            pyautogui.mouseDown()
            
            # Drag the mouse over the remaining points
            for point in contour[1:]:
                # Constantly check if we want to stop!
                if keyboard.is_pressed('space'):
                    raise Exception("The bot was stopped by the user (Space key).")
                    
                p = point[0]
                pyautogui.moveTo(start_x + p[0], start_y + p[1])
            
            # Release the mouse button at the end of the line
            pyautogui.mouseUp()
except pyautogui.FailSafeException:
    print("\nDrawing cancelled by fail-safe (mouse moved to the top-left corner of the screen).")
    pyautogui.mouseUp()
except Exception as e:
    pyautogui.mouseUp()
    print("\n" + str(e))

print("Drawing complete! :)")
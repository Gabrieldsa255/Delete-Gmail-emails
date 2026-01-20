import time
import pyautogui

print("Mova o mouse. Ctrl+C para parar.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X={x} Y={y}", end="\r", flush=True)
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nParado.")

import pyautogui

input("Posicione o mouse no ponto desejado e aperte ENTER...")
x, y = pyautogui.position()
print(f"X={x} Y={y}")


import time
import pyautogui

# ====== SEGURANÇA ======
pyautogui.FAILSAFE = True          # canto superior esquerdo aborta
pyautogui.PAUSE = 0.12             # pausa automática entre comandos

# ====== COORDENADAS (CONFIRMADAS) ======
SELECT_X, SELECT_Y = 124, 221       # Selecionar (checkbox do topo)
DELETE_X, DELETE_Y = 314, 216    # Lixeira (delete) no topo

REPEAT = 10
WAIT_AFTER_SELECT = 0.25
WAIT_AFTER_DELETE = 0.25

# Clique pra garantir foco no Gmail antes do loop
FOCUS_X, FOCUS_Y = 450, 300

def countdown(seconds=5):
    print(f"Vai começar em {seconds}s... (deixe o Gmail aberto e parado)")
    for i in range(seconds, 0, -1):
        print(f"  {i}...", end="\r", flush=True)
        time.sleep(1)
    print(" " * 40, end="\r")

def safe_click(x, y, clicks=1):
    pyautogui.moveTo(x, y, duration=0.08)
    pyautogui.click(clicks=clicks, interval=0.08)

countdown(5)

try:
    # Garantir foco no Gmail
    safe_click(FOCUS_X, FOCUS_Y, clicks=1)
    time.sleep(0.2)

    for i in range(1, REPEAT + 1):
        print(f"Apagando {i}/{REPEAT}")

        # 1) Selecionar (2 cliques: 1º foca, 2º marca)
        safe_click(SELECT_X, SELECT_Y, clicks=1)
        time.sleep(WAIT_AFTER_SELECT)

        # 2) Apagar (lixeira)
        safe_click(DELETE_X, DELETE_Y, clicks=1)
        time.sleep(WAIT_AFTER_DELETE)

        # pausa extra a cada 10 para o Gmail atualizar
        if i % 10 == 0:
            time.sleep(0.6)

    print("Concluído.")

except pyautogui.FailSafeException:
    print("\nABORTADO: você moveu o mouse pro canto superior esquerdo (FailSafe).")

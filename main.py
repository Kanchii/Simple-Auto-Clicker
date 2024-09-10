import pyautogui
import keyboard
import time
import threading

# Variável global para controlar o estado do autoclicker
clicking         = False
all_source_pos   = None
all_upgrades_pos = None
clicker_pos      = None

def clicker():
    global all_source_pos, all_upgrades_pos, clicker_pos
    counter = 0
    while True:
        if clicking:
            pyautogui.click(clicker_pos[0], clicker_pos[1])
            time.sleep(0.01)  # Ajuste o tempo entre os cliques conforme necessário
            counter += 1
            if(counter % 250 == 0):
                counter = 0
                pyautogui.leftClick(all_upgrades_pos[0], all_upgrades_pos[1], 2)
                time.sleep(2)
                pyautogui.leftClick(all_source_pos[0], all_source_pos[1], 2)
                time.sleep(2)
        else:
            counter = 0

def toggle_clicking():
    global clicking, clicker_pos
    if clicker_pos is None:
        clicker_pos = pyautogui.position()

    clicking = not clicking

def set_buy_all_sources():
    global all_source_pos
    all_source_pos = pyautogui.position()

def set_buy_all_upgrades():
    global all_upgrades_pos
    all_upgrades_pos = pyautogui.position()

# Inicia o thread do autoclicker
click_thread = threading.Thread(target=clicker)

# Associa a tecla "G" para startar/pausar o autoclicker
keyboard.add_hotkey('g', toggle_clicking)
print("Pressione 'G' para startar/pausar o autoclicker. Pressione 'Esc' para sair.")

keyboard.add_hotkey('a', set_buy_all_sources)
print("Pressione 'A' para setar a posição do Buy All Sources.")

keyboard.add_hotkey('b', set_buy_all_upgrades)
print("Pressione 'B' para setar a posição do Buy All Upgrades.")

click_thread.daemon = True
click_thread.start()

# Mantém o script rodando até que 'Esc' seja pressionado
keyboard.wait('esc')

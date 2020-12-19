#RATORI-game
from modules import game
from pyautogui import *

msg = 'Обновить версию'
win = 'Обнавление'
game_version = 2 #Запрос версии с интернета

if __name__ == '__main__':
    local_version = game.local_version
    if local_version < game_version:
        print(msg)
        alert(msg, win, button='ОК' )
    else:
        game.game_cycle()
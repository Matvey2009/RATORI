#RATORI-game
from modules import game

game_version = 1 #Запрос версии с интернета

if __name__ == '__main__':
    local_version = game.local_version
    if local_version < game_version:
        print("Обновить версию")
    else:
        game.game_cycle
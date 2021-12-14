from single import TicTacToeSingle
from multi import TicTacToeMulti
            


print("Hello and welcome to your TicTacToe Game!")
print("Thats the Map:")
print(["0","1","2"])
print(["3","4","5"])
print(["6","7","8"])
print("If you need, use the commands \"field\" and \"played\".")

while True:
    game_mode = input("Please insert Gamemode. Singleplayer (s) or Multiplayer (m): ")
    if game_mode == "s":
        game = TicTacToeSingle()
        break
    elif game_mode == "m":
        game = TicTacToeMulti()
        break
    else:
        print("Please insert correctly")


game.play()


from random import randrange
import names

field = [" "," "," "," "," "," "," "," "," "]

winings = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

player1PlayedList = []
player2PlayedList = []
playerAllPlayedList = []

play_mode = ""

name_player_1 = ""
name_player_2 = ""

keep_playing=1
p1_played = 0
p2_played = 0
            

def check_is_win(player, name_player):
    for win in winings:
        place_counter = 0
        for place in win:
            if place in player:
                place_counter+=1
                if place_counter == 3:
                    keep_playing = 0
                    print("The Winner is " + name_player + ". Win:" + str(win))
                    quit()
                    

while play_mode != "s" or play_mode != "m":
        play_mode = input("Chose mode (multi or single): m/s ")

        if play_mode == "s":
            print("You chose single-player mode.")
            break
        elif play_mode == "m":
            print("You chose multiplayer mode.")
            break
        else:
            print("Wrong answer please try again.")

#Singleplayer-Mode
if play_mode == "s":
    name_player_1 = input("Please insert your Name: ")
    name_player_2 = names.get_first_name()
    print(f"Welcome, {name_player_1}. Your opponent is {name_player_2}.")

    while keep_playing == 1:
        p1_played = 0
        p2_played = 0

        #Player 1 turn
        while p1_played != 1:
            p1 = int(input("Its your turn, " + name_player_1 + ". Please insert your number (0-8): "))
            if p1 not in playerAllPlayedList:
                field[p1] = "o"
                playerAllPlayedList.append(p1)
                player1PlayedList.append(p1)
                print("Current field:")
                print(field[0:3])
                print(field[3:6])
                print(field[6:9])
                p1_played = 1
            else:
                print("field is already used")
        check_is_win(player1PlayedList, name_player_1)

        #Bot turn 
        while p2_played != 1:
            print("Its your turn " + name_player_2)
            p2 = randrange(9)
            if p2 not in playerAllPlayedList:
                field[p2] = "x"
                playerAllPlayedList.append(p2)
                player2PlayedList.append(p2)
                print(name_player_2 + " chose Number " + str(p2))
                print("Current field:")
                print(field[0:3])
                print(field[3:6])
                print(field[6:9])
                p2_played = 1
            else:
                print("field is already used")
        check_is_win(player2PlayedList, name_player_2)

#Multiplayer-Mode
elif play_mode == "m":
    name_player_1 = input("Player 1, please insert your Name: ")
    name_player_2 = input("Player 2, please insert your Name: ")
    
    while keep_playing == 1:
        p1_played = 0
        p2_played = 0
        #Player 1 turn
        while p1_played != 1:
            p1 = int(input("Its your turn, " + name_player_1 + ". Please insert your number (0-8): "))
            if p1 not in playerAllPlayedList:
                field[p1] = "o"
                playerAllPlayedList.append(p1)
                player1PlayedList.append(p1)
                print("Current field:")
                print(field[0:3])
                print(field[3:6])
                print(field[6:9])
                p1_played = 1
            else:
                print("field is already used")
            check_is_win(player1PlayedList, name_player_1)
        #Player 2 turn
        while p2_played != 1:
            p2 = int(input("Its your turn, " + name_player_2 + ". Please insert your number (0-8): "))
            if p2 not in playerAllPlayedList:
                field[p2] = "x"
                playerAllPlayedList.append(p2)
                player2PlayedList.append(p2)
                print("Current field:")
                print(field[0:3])
                print(field[3:6])
                print(field[6:9])
                p2_played = 1
            else:
                print("field is already used")
            check_is_win(player2PlayedList, name_player_2)

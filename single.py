from random import randrange
from time import sleep
import names 

class TicTacToeSingle:

    def __init__(self):
        #self.number = number
        self.name1 = input("Please enter your Name: ")
        self.name2 = names.get_first_name()
        print(f"Welcome, {self.name1}. Your opponent is {self.name2}.")
        self.min = 0
        self.max = 8
        self.field = [" "," "," "," "," "," "," "," "," "]
        self.winings = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.player1PlayedList = []
        self.player2PlayedList = []
        self.playerAllPlayedList = []

    
    def get_number1(self):
        number = input(f"Its your turn, {self.name1}. Please insert your number ({self.min} - {self.max}): ")        
        if self.valid_number(number):
            print(f"You chose {number}.")
            self.field[int(number)] = "o"
            self.playerAllPlayedList.append(int(number))
            self.player1PlayedList.append(int(number))
            print("Current field:")
            print(self.field[0:3])
            print(self.field[3:6])
            print(self.field[6:9])
            self.check_is_win(self.player1PlayedList, self.name1)
        elif self.commands(number):
            return self.get_number1()
        else:
            print("Please enter a valid number.")
            return self.get_number1()

    def get_number2(self):
        print(f"Its your turn, {self.name2}")
        sleep(randrange(8))     #some delay for more fun
        number = randrange(9)
        if self.valid_number(number):
            print(f"You chose {number}.")
            self.field[int(number)] = "x"
            self.playerAllPlayedList.append(int(number))
            self.player2PlayedList.append(int(number))
            print("Current field:")
            print(self.field[0:3])
            print(self.field[3:6])
            print(self.field[6:9])
            self.check_is_win(self.player2PlayedList, self.name2)
        else:
            print("Please enter a valid number.")
            return self.get_number2()

    def valid_number(self, number):
        try:
            return 0 <= int(number) <= 8 and int(number) not in self.playerAllPlayedList
        except:
            return False
                     
    def check_is_win(self, player, name_player):
        for win in self.winings:
            place_counter = 0
            for place in win:
                if place in player:
                    place_counter+=1
                    if place_counter == 3:
                        print(f"The Winner is {name_player}. Win: {str(win)}")
                        quit()
                    
    def play(self):
        while True:
            self.get_number1()
            self.get_number2()

    def commands(self, command):
        if command == "field":
            print(self.field[0:3])
            print(self.field[3:6])
            print(self.field[6:9])
        elif command == "played":
            sorted_list = []
            for num in self.playerAllPlayedList:
                sorted_list.append(num)
            sorted_list.sort()
            print(sorted_list)
        else:
            return False
        

import random

player_count = 4
spaces_between_players = 10
total_places = player_count * spaces_between_players


class Board:
    pass

class Piece:
    def __init__(self, position = 0, on_board = False):
        self.position = position
        self.on_board = on_board
    
        

class Player:
    def __init__(self, index, pieces):
        self.index = index
        self.pieces = pieces
        self.starting_pos = index * spaces_between_players

    def player_num(self):
        self.index + 1

players = [Player(i, [Piece(), Piece(), Piece(), Piece()]) for i in range(4)]

print([players[i].starting_pos for i in range(4)]) 

def turn(player, pieces_on_board):
    if player_count >= 2 and player_count <= 6:
        if pieces_on_board > 0:
            diceroll = random.randint(1, 6)
            print(diceroll) 
            players[player].pieces[0].position += diceroll 
            player
        else:
            for i in range(3):
                diceroll = random.randint(1, 6)
                if diceroll == 6:
                    pieces_on_board  = pieces_on_board + 1               
                    return
                else:
                    return 
    else:
        print("invalid amount of players")

turn(0, 1)
turn(1, 1)
turn(2, 1)
turn(3, 1)

print(players[0].pieces[0].position)

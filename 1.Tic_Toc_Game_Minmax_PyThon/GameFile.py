
# Computer Vs AI
#MinMax Algorithm
#Python
# Wasif
import numpy as np
from math import inf as infinity

game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
players = ['X','O']

def move(state, player, block_num):
    if state[int((block_num-1)/3)][(block_num-1)%3] is ' ':
        state[int((block_num-1)/3)][(block_num-1)%3] = player
    else:
        block_num = int(input("Already Used,Please Choose Different one "))
        play_move(state, player, block_num)
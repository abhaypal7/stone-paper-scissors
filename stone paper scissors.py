#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
moves =['stone','paper','scissor']
computer=random.choice(moves)
name=input('Enter your name: ')
player =False

while player==False:
    your_move=input('stone or pape')
    if your_move==computer:
        print('its a tie')
    elif your_move== 'stone':
        if computer=='paper':
            print('computer wins')
        else:
            print('{} won'.format(name))
    elif your_move=='paper':
        if computer =='scissors':
            print('computer won')
        else:
            print('{} won'.format(name))
    elif your_move == 'scissors':
        if computer=='paper':
            print('computer wins')
        else:
            print('{} won'.format(name))
    player == True
        

    new_game = input('Do you want to play another round? (y/n) ')
    if new_game == 'y':
        player = False
    else:
        print('Thanks for playing!!!')
        break;


# In[ ]:





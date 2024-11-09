# 9 November 2024 Yusuf Ismail Shukor
# Dice rolling simulator game

import random
from app.die_faces import die_faces
from app.greet import greet

greet()

keep_rolling = True

while keep_rolling:
  roll = input('Roll the dice? (y/n) ')
  if roll == 'y':
    print(random.choice(die_faces))
  else:
    keep_rolling = False

print('Thanks for playing!')
print('GAME OVER')
print(' ')

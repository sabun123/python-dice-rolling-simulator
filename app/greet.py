import datetime
from app.die_faces import die_faces

def greet():
  now = datetime.datetime.now()

  print('')
  print('Good ' + ('morning' if now.hour < 12 else 'afternoon') + '!')
  print('Welcome to the dice rolling simulator!')
  print('')
  print(die_faces[0])
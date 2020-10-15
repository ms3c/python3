import random as ran
import time
import threading

SecretNum = ran.randint(1, 10)
def GuessGame():
  while(True):
  
    print(f'Welcome to Guess Game')
    
    UserGuess = int(input('Enter Your Guess: '))
    return UserGuess
    
    def CheckGuess1():
      if UserGuess == SecretNum:
        print(f'Congratulations!!')
    def CheckGuess2():
      elif UserGuess <= SecretNum:
        print(f'Too low!')
        
    def CheckGuess1(): 
      elif UserGuess >= SecretNum:
        print(f'Too High!')
        
  t1 = threading.thread(CheckGuess1)
  t2 = threading.thread(CheckGuess2)
  t3 = threading.thread(CheckGuess3)
  
  threading.start()

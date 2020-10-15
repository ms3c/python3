import random as ran
import time
import threading

SecretNum = ran.randint(1, 10)
def GuessGame():
  while(True):
  
    print(f'Welcome to Guess Game')
    
    UserGuess = int(input(f'Enter Your Guess: '))
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
        
t1 = threading.Thread(target=CheckGuess1)
t2 = threading.Thread(target=CheckGuess2)
t3 = threading.Thread(target=CheckGuess3)
  
t2.start()
t2.start()
t2.start()

t2.join()
t2.join()
t2.join()

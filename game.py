""" Game find the number"""

from tkinter.tix import Tree
import numpy as np

number = np.random.randint (1, 101)

# how much time try
count = 0


while True:
    count +=1
    predict_number = int(input("What the number 1 to 100"))
    
    if predict_number > number:
        print(" Number have to be less!")
        
    elif predict_number < number:
        print ("Numer have to be more") 
        
        
    else :
        print(f"This is right number! it's {number}, {count} times ")   
        break #stop cycle while true
    
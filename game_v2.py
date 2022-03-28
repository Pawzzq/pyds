""" Game find the number"""
"""Comp find by himself"""



import numpy as np

def random_predict (number:int=1)-> int:
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # maybe this number
        if number == predict_number:
            break # stop cycle
        return (count)
    
    print(f"{random_predict(10)}")
    
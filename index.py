import numpy as np
import pandas as pd 

words = input("Enter a sentence to show latin words")
words_list = words.split('')
for word in words_list:
    if len(word) >= 3:
        print(word)
    else:
        pass

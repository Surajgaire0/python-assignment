# 7. Write a Python function to check whether a string is a pangram or not. 
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.

import re

def ispangram(sentence):
    sentence = re.sub('[^a-zA-Z]', '', sentence)
    if len(set(sentence.upper())) == 26:
        return True
    return False


print (ispangram('The quick brown fox jumps over the lazy dog..'))
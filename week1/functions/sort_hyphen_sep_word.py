# 8. Write a Python program that accepts a hyphen-separated sequence of words as input and 
# prints the words in a hyphen-separated sequence after sorting them alphabetically
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def sort_words_in_hyphen(text):
    return '-'.join(sorted(text.split('-')))


a = 'green-red-yellow-black-white'

print (sort_words_in_hyphen(a))
# 3. Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

results={}
while True:
    place = input('If you could visit one place in the world, where would you go? \
    (Type exit and press enter to see result) :').lower()

    if place: # if place is not empty
        if place == 'exit':
            print (results)
            break
        if place in results:
            results[place] += 1
        else:
            results[place] = 1
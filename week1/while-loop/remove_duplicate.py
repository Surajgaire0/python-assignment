# 1. bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
# Remove all the duplicates from the following list using while.

bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']

counter = 0
length = len(bird)
tmp = []
while counter < length:
    if bird[counter] not in tmp:
        tmp.append(bird[counter])
    counter += 1

bird = tmp
del tmp

print (bird)
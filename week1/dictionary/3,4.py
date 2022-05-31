# 3. users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
#         'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
#         'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
# Generate a list of usernames, name, age and poison from the above dictionary.

# 4. Take the above list and put it in order.

users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}

usernames = []
names = []
age = []
poison = []

for key, value in users.items():
    usernames.append(key)
    names.append(value['name'])
    age.append(value['age'])
    poison.append(value['poison'])

usernames.sort()
names.sort()
age.sort()
poison.sort()

print (usernames, names, age, poison, sep='\n')


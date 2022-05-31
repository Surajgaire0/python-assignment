# 5. Create an empty dictionary called milk_carton. Add the following key/value pairs. 
# You can make up the values or use a real milk carton.
# a.	Expiration_date: a tuple with day, month, year
# b.	Vol: volume of milk 
# c.	Cost: cost of milk
# d.	Brand_name

# 6. Print out the values of all of the elements of the milk_carton using the values in the dictionary.

# 7. Show how to calculate the cost of six cartons of milk based on the cost of the milk_carton.

milk_cartoon = {}

milk_cartoon = {'expiration_date':(12,4,2079), 'vol':1, 'cost': 100, 'brand_name':'ddc'}

# printing values
for key, values in milk_cartoon.items():
    print(key, ':', values)

# calculating cost of 6 cartoons
print ('Cost of 6 cartoons: ', milk_cartoon['cost'] * 6)
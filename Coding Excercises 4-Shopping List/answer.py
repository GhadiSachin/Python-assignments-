my_cart=["apples","bananas","milk"]
print(my_cart)

my_cart.append("bread")
print(my_cart)


my_cart.insert(0,"ketchup")
print(my_cart)

my_cart.remove("bananas")
print(my_cart)

removed_item=my_cart.pop()
print(removed_item)

my_cart.append("rice")
my_cart.append("butter")
print(my_cart)

my_cart.sort()
print(my_cart)

my_cart.reverse()
print(my_cart)

# operator overloading
new_cart = my_cart + ["juice", "jam"]
print(new_cart)

my_cart=my_cart *2
print(my_cart)

string_value = "tomato cucumber spinach"
converted_list = string_value.split()
print(converted_list)   

# git and github
print("Hello")
data_list = [1, 2, 4, ["piyush", "sharma", "kumar"], {"firstname": "praveen"},
             {"relation": "friend"}]
# output should look like
# Praveen Sharma and Piyush Kumar is good friend.
my_name = data_list[4]["firstname"]
print("capitalize()", "piyush kumar".capitalize())
print(my_name.lower())
print(my_name.upper())
print("piyush kumar".title())

print(f"{data_list[4]["firstname"].capitalize()} {data_list[3][1]} and {data_list[3][0].capitalize()} {data_list[3][2]} is good {data_list[5]["relation"]}.")

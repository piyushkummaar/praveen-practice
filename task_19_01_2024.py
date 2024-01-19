user_data = [
    {"name": "user_1", "spend": 1000, "date": "31/12/2023"},
    {"name": "user_1", "spend": 2000, "date": "30/12/2023"},
    {"name": "user_2", "spend": 3000, "date": "15/02/2023"},
    {"name": "user_1", "spend": 4000, "date": "01/02/2023"},
    {"name": "user_2", "spend": 5000, "date": "31/12/2023"}
]

customer_data = [
    {"cust_name": "Praveen", "name": "user_1"},
    {"cust_name": "Piyush", "name": "user_2"}
]

new_data = []

# logic here
for i in user_data:
    for j in customer_data:
        if j.get("name") == i.get("name"):
            n_dict = j.copy()
            n_dict["spend"] = i.get("spend")
            n_dict["date"] = i.get("date")
            new_data.append(n_dict)
print(new_data)
# [{'cust_name': 'Praveen', 'name': 'user_1', 'spend': 4000, 'date':'01/02/2023'},
# ----]


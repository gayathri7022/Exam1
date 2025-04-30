customer = {
}

menu = {
    "tiffin" : {
        "dosa" : 30,
        "vada" : 20,
        "upma" : 40,
        "pulav" : 45
    }, 
    "meals" : {
        "north indian" : 120,
        "south indian" : 100,
    },
    "sweets" : {
        "jamun" : 20,
        "rasgulla" : 25,
        "kesaribath" : 30
    }
    
}

def register(name, email, password):
    if email.endswith("@gmail.com"):
        if len(password) >= 8:
            if password.isalnum():
                return "Registeration successfull"
            else:
                return "Password must be alphanumeric"
        return "Password must be 8 characters long"
    return "Invalid email"


def view_menu(customer_id, food_type, item, quantity):
    food_type = food_type.lower()
    item = item.lower()
    qty = int(quantity)

    if food_type.lower() not in menu:
        return f"{food_type} not available"
    
    if item not in menu[food_type]:
        return f"{item} is not available in {food_type}"
    
    price = menu[food_type][item] * qty

    if customer_id in customer:
        customer[customer_id] += price
        return f"Order placed succesfully. For {item.capitalize()} price : {menu[food_type][item]}. Total price : {customer[customer_id]}"
    
    customer[customer_id] = price
    return f"Order placed succesfully. For {item.capitalize()} price : {menu[food_type][item]}. Total price : {customer[customer_id]}"
     
            
        

# print(register("Gayathri", "gaythri@gmail.com", "12345dfg"))    #Registeration successfull
# print(register("Gayathri", "gaythri@gmail", "12345dfg"))        #Invalid email
# print(register("Gayathri", "gaythri@gmail.com", "12345ab"))     #Password must be 8 characters long

print(view_menu("001", "tiffin", "vada", 2))     #Order placed succesfully. For Vada price = 20. Total price = 40
print(view_menu("001", "tiffin", "dosa", 1))     #Order placed succesfully. For Dosa price = 30. Total price = 70

print(view_menu("002", "desserts", "cake", 1))   #desserts not available

print(view_menu("004", "Meals", "Thali", 3))     #thali is not available in meals



    

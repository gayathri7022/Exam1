customer = {
    "001" : 0
}

menu = ["tiffin", "meals", "sweets"]
food = {
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


def view_menu(food_type, item, cid):
    if food_type not in menu:
        return f"{food_type} not available"
    else:
        food_type = food_type.lower()
        item = item.lower()
        if item in food[food_type]:
            if cid in customer:
                customer[cid] += food[food_type][item]
            else:
                customer[cid] = food[food_type][item]
            return f"{item} Price = {food[food_type][item]} Order placed succesfully Total price: {customer[cid]}"
            
        else:
            return f"{item} is not available in {food_type}"
        

print(register("Gayathri", "gaythri@gmail.com", "12345dfg"))    #Registeration successfull
print(register("Gayathri", "gaythri@gmail", "12345dfg"))        #Invalid email
print(register("Gayathri", "gaythri@gmail.com", "12345ab"))     #Password must be 8 characters long


print(view_menu("tiffin", "vada", "001"))       #vada Price = 20 Order placed succesfully Total price: 20

print(view_menu("tiffin", "kesari", "002"))     #kesari is not available in tiffin

print(view_menu("meals", "north indian", "003"))    #north indian Price = 120 Order placed succesfully Total price: 120

print(view_menu("meals", "thali", "001"))       #thali is not available in meals

print(view_menu("sweets", "jamun", "001"))      #jamun Price = 20 Order placed succesfully Total price: 40

print(view_menu("desserts", "cake", "004"))     #desserts not available


            
        



    

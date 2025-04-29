customer = {
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


def view_menu(food_type, item):
    if food_type not in menu:
        return f"{food_type} not available"
    else:
        food_type = food_type.lower()
        item = item.lower()
        if item in food[food_type]:
            
            return f"{item} Total price = {food[food_type][item]}"
            
        else:
            return f"{item} is not available in {food_type}"
        

print(register("Gayathri", "gaythri@gmail.com", "12345dfg"))    #Registeration successfull
print(register("Gayathri", "gaythri@gmail", "12345dfg"))        #Invalid email
print(register("Gayathri", "gaythri@gmail.com", "12345ab"))     #Password must be 8 characters long




print(view_menu("tiffin", "kesari"))     #kesari is not available in tiffin

print(view_menu("meals", "north indian"))  
        



    

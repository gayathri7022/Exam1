from Register import register, view_menu

def test_cases():
    assert register("Gayathri", "gaythri@gmail.com", "12345dfg") == "Registeration successfull"
    assert register("Gayathri", "gaythri@gmail", "12345dfg") ==  "Invalid email"   #Invalid email
    assert register("Gayathri", "gaythri@gmail.com", "12345ab") == "Password must be 8 characters long"     #Password must be 8 characters long


    assert view_menu("tiffin", "vada", "001") == "vada Price = 20 Order placed succesfully Total price: 20"

    assert view_menu("tiffin", "kesari", "002") == "kesari is not available in tiffin"

    assert view_menu("meals", "north indian", "003") == "north indian Price = 120 Order placed succesfully Total price: 120"

    assert view_menu("meals", "thali", "001") == "thali is not available in meals"

    assert view_menu("sweets", "jamun", "001") == "jamun Price = 20 Order placed succesfully Total price: 40"

    assert view_menu("desserts", "cake", "004") == "desserts not available"

    
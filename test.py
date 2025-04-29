from Register import register, view_menu

def test_cases():
    assert register("Gayathri", "gaythri@gmail.com", "12345dfg") == "Registeration successfull"
    assert register("Gayathri", "gaythri@gmail", "12345dfg") ==  "Invalid email"   #Invalid email
    assert register("Gayathri", "gaythri@gmail.com", "12345ab") == "Password must be 8 characters long"     #Password must be 8 characters long


    

    assert view_menu("tiffin", "kesari") == "kesari is not available in tiffin"

    assert view_menu("meals", "north indian") == "north indian Total price = 120"


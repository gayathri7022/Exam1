from Register import view_menu, register, customer

def test_cases():
    customer.clear()

    assert register("Gayathri", "gaythri@gmail.com", "12345dfg") == "Registeration successfull"

    assert register("Gayathri", "gaythri@gmail", "12345dfg") == "Invalid email"


    assert register("Gayathri", "gaythri@gmail.com", "12345ab") == "Password must be 8 characters long"



    result = view_menu("001", "tiffin", "vada", 2)
    assert result == "Order placed succesfully. For Vada price : 20. Total price : 40"

    result2 = view_menu("001", "tiffin", "dosa", 1)
    assert result2 == "Order placed succesfully. For Dosa price : 30. Total price : 70"

    result3 = view_menu("002", "desserts", "cake", 1)
    assert result3 == "desserts not available"

    result4 = view_menu("004", "Meals", "Thali", 3)
    assert result4 == "thali is not available in meals"


test_cases()
print("All tests passed")
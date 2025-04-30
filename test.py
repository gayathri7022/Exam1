from Register import view_menu

def test_cases():
    assert view_menu("001", "tiffin", "vada", 2) == "Order placed succesfully. For Vada price : 20. Total price : 40"
    assert view_menu("001", "tiffin", "dosa", 1) == "Order placed succesfully. For Dosa price : 30. Total price : 70"
    assert view_menu("002", "desserts", "cake", 1) == "desserts not available"
    assert view_menu("004", "Meals", "Thali", 3) == "thali is not available in meals"


test_cases()
print("All tests passed")
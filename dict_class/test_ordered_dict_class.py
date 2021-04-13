# TODO: Task 2 - OrderedDict. Keeps the order of adding elements.

ordered_dict = MyOrderedDict()
ordered_dict.add("Nikola", "11111") # Creates key 
ordered_dict.add("Simo", 2222) # Creates key
ordered_dict.add("Nikola", 3333) # Updates existing

def test_get_ordered_method():
    assert ordered_dict.get("Simo") == 2222
    assert ordered_dict.get("Nikola") == 3333
    ordered_dict.remove("Nikola") # Only Simo key left
    assert ordered_dict.get("Nikola") == None

ordered_dict.remove("Nikola")
ordered_dict.remove("Simo")

ordered_dict["First"] = 1 
ordered_dict["Second"] = 2
ordered_dict["Third"] = 3

def test_return_ordered():
    assert d[0] == ("First", 1) # Returns ("First", 1) 
    assert d[1] == ("Second", 2) # Returns ("Second", 2) 
    assert d[2] == ("Third", 3) # Returns ("Third", 3)
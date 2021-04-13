from dict_class import MyDict

def test_get_method():
    d = MyDict()
    d.add("Nikola", "11111") # Creates key 
    d.add("Simo", 2222) # Creates key
    d.add("Nikola", 3333) # Updates existing
    assert d.get("Simo") == 2222 #WHYYYYYYYYYYYYYYYYYYYYYYYYY
    assert d.get("Nikola") == 3333
    d.remove("Nikola") # Only Simo key left
    assert d.get("Nikola") == None
    del d


def test_return_by_order():
    d2 = MyDict()
    d2["First"] = 1
    d2["Second"] = 2
    d2["Third"] = 3
    assert d2[0] == ("First", 1) # Returns ("First", 1) 
    assert d2[1] == ("Second", 2) # Returns ("Second", 2) 
    assert d2[2] == ("Third", 3) # Returns ("Third", 3)

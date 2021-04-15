from dict_class import *

def test_get_method():
    d = MyDict()
    d.add("Nikola", "11111") # Creates key 
    d.add("Simo", 2222) # Creates key
    d.add("Nikola", 3333) # Updates existing
    assert d.get("Simo") == 2222 #WHYYYYYYYYYYYYYYYYYYYYYYYYY
    assert d.get("Nikola") == 3333
    d.remove("Nikola") # Only Simo key left
    assert d.get("Nikola") == None


def test_return_by_order():
    d2 = MyDict()
    d2["First"] = 1
    d2["Second"] = 2
    d2["Third"] = 3
    assert d2[0] == ("First", 1) # Returns ("First", 1) 
    assert d2[1] == ("Second", 2) # Returns ("Second", 2) 
    assert d2[2] == ("Third", 3) # Returns ("Third", 3)

def test_ordered_dict():
    tracked = MyOrderedDict()
    tracked.add("Nikola", "1234")
    assert tracked.get("Nikola") == "1234"

    tracked.add("Simo", "4321")
    tracked.add("Nikola", "1243")

    assert tracked.get_order() == ["Nikola", "Simo"]

    assert tracked.get("Nikola") == "1243"
    tracked.remove("Nikola")
    assert tracked.get("Nikola") == None

    tracked.clear()
    tracked["First"] = 1
    tracked["Second"] = 2
    tracked["Third"] = 3
    
    assert tracked[0] == ("First", 1) # Returns ("First", 1) 
    assert tracked[1] == ("Second", 2) # Returns ("Second", 2) 
    assert tracked[2] == ("Third", 3) # Returns ("Third", 3)
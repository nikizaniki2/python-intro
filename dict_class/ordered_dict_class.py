import collections

class MyOrderedDict:
    def __init__(self, init_value = collections.OrderedDict()):
        self.dictionary = init_value

    def get(self, key):
        # Return value by ky or None
        return self.dictionary.get(key)

    def add(self, key, value):
        # Add or update by key
        self.dictionary[str(key)] = value
    
    def remove(self, key):
        self.dictionary.pop(key)

    def __setitem__(self, key, value):
      self.dictionary[str(key)] = value

    def __getitem__(self, key):
        items = list(self.dictionary.items())
        return items[key]



# ordered_dict = MyOrderedDict()
# ordered_dict.add("Nikola", "11111") # Creates key
# ordered_dict.add("Simo", "2222") # Creates key
# ordered_dict.add("Nikola", "3333") # Updates existing
# ordered_dict.remove("Nikola") # Only Simo key left

# ordered_dict.get("Simo") # 2222
# ordered_dict.get("Nikola") # None
# ordered_dict["Simo"] = 2222
# ordered_dict.remove("Simo")

# ordered_dict["First"] = 1 
# ordered_dict["Second"] = 2
# ordered_dict["Third"] = 3

# ordered_dict[0] # Returns ("First", 1) 
# ordered_dict[1] # Returns ("Second", 2) 
# ordered_dict[2] # Returns ("Third", 3)
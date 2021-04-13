# Create dict by {} or dict()

class MyDict:
    def __init__(self, init_value = {}):
        self.dictionary = init_value

    def get(self, key):
        # Return value by key or None
        return self.dictionary.get(key)

    def add(self, key, value):
        # Add or update by key
        self.dictionary[str(key)] = value
    
    def remove(self, key):
        self.dictionary.pop(key)

    def __setitem__(self, key, value):
        self.dictionary[str(key)] = value

    def __getitem__(self, key):
        keys = list(self.dictionary.keys())
        return str(keys[key]), self.dictionary.get(keys[key])



# d = MyDict()
# d.add("Nikola", "11111") # Creates key
# d.add("Simo", "2222") # Creates key
# d.add("Nikola", "3333") # Updates existing
# d.remove("Nikola") # Only Simo key left
# d.get("Simo") # 2222
# d.get("Nikola") # None

# # LEARN: Magic methods / Special methods / dunders (__<method>__)
# d["Simo"] = 2222
# d.remove("Simo")

# d["First"] = 1 
# d["Second"] = 2
# d["Third"] = 3

# d[0] # Returns ("First", 1) 
# d[1] # Returns ("Second", 2) 
# d[2] # Returns ("Third", 3)

# # Hashing: unique input -> unique hash string
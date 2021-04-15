# Create dict by {} or dict()

class MyDict:
    # Warning: dont use default parameters of mutable types
    # as next instances will refer them by name and cause side effects.
    # Make a copy instead.
    def __init__(self, init_value = {}):
        # Expand/spread key-value pairs
        # self.dictionary = dict(init_value)
        self.dictionary = { **init_value }

    # https://realpython.com/python-kwargs-and-args/
    def method(self, *args, **kwargs):
        pass

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
        

class MyOrderedDict(MyDict):
    def __init__(self):
        self.tracker = []
        super().__init__(init_value = {})

    def get_order(self):
        return self.tracker

    def get(self, key):
        super().get(key)
        return self.dictionary.get(key)

    def add(self, key, value):
        #Don't append on change!!!
        if key in self.tracker:
            super().add(key, value)
            return
        self.tracker.append(key)
        super().add(key, value)
    
    def remove(self, key):
        self.tracker.remove(key)
        super().remove(key)

    def __setitem__(self, key, value):
        self.tracker.append(key)
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return super().__getitem__(key)
    
    def clear(self):
        for i in self.tracker:
            super().remove(i)
            self.tracker.remove(i)

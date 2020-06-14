

class Item:

    def __init__(self, property_1=None, property_2=None, property_3=None,
                 property_4=None):
        self.property_1 = property_1
        self.property_2 = property_2
        self.property_3 = property_3
        self.property_4 = property_4

    def __str__(self):
        return f'You can change what you want to see in the object, ' \
                f'when you print it, say its first property: {self.property_1}'



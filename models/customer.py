class Customer():

    # Class initializer. It has 4 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, email):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
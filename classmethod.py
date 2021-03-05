class Pasta:
    __CARBONARA_INGREDIENT = ['bacon', 'parmesan', 'eggs']
    __BOLOGNAISE_INGREDIENT = ['forcemeat', 'tomatoes']

    def __init__(self, ingredient):
        self.ingredient = ingredient

    @classmethod
    def carbonara(cls):
        return Pasta(cls.__CARBONARA_INGREDIENT)

    @classmethod
    def bolognaise(cls):
        return Pasta(cls.__BOLOGNAISE_INGREDIENT)

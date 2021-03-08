# 1
import collections
import dataclasses


class Laptop:
    def __init__(self, battery_type):
        self.battery = Battery(battery_type)


class Battery:
    def __init__(self, battery_type):
        self.battery_type = battery_type


laptop = Laptop('lithium')


# 2
class Guitar:
    def __init__(self, guitar_type, strings):
        self.guitar_type = guitar_type
        self.strings = strings


class GuitarString:
    def __init__(self, string_tone):
        self.string_tone = string_tone


string_A = GuitarString('A')
string_E = GuitarString('E')
string_G = GuitarString('G')
string_C = GuitarString('C')

guitar_strings = [string_A, string_E, string_G, string_C]
guitar = Guitar('ukulele', guitar_strings)


# 3
class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


numbers = Calc()
print(Calc.add_nums(15, 28, -45))


# 4
class Pasta:
    CARBONARA_INGREDIENT = ['bacon', 'parmesan', 'eggs']
    BOLOGNAISE_INGREDIENT = ['forcemeat', 'tomatoes']

    def __init__(self, ingredient):
        self.ingredient = ingredient

    @classmethod
    def carbonara(cls):
        return Pasta(cls.CARBONARA_INGREDIENT)

    @classmethod
    def bolognaise(cls):
        return Pasta(cls.BOLOGNAISE_INGREDIENT)


pasta_1 = Pasta(['mushrooms', 'parmesan'])
print(f'pasta_1 ingredients are {pasta_1.ingredient}')
pasta_2 = Pasta.bolognaise()
print(f'pasta_2 ingredients are {pasta_2.ingredient}')
pasta_3 = Pasta.carbonara()
print(f'pasta_3 ingredients are {pasta_3.ingredient}')


# 5
class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, _visitors_count):
        if _visitors_count >= self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = _visitors_count


concert_1 = Concert()
concert_2 = Concert()

Concert.max_visitors_num = 250

print('concert_1.max_visitors_num:', concert_1.max_visitors_num)
concert_1.visitors_count = 698
print('concert_1.visitors_count:', concert_1.visitors_count)

Concert.max_visitors_num = 784

print('concert_2.max_visitors_num:', concert_2.max_visitors_num)
concert_2.visitors_count = 452
print('concert_2.visitors_count:', concert_2.visitors_count)


# 6
@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(5879, 'Jason', '54-78-236', 'Minsk/Belorussia', 'jason@test.com', '13/05/1994', 26)
print(address_book)

# 7
AddressBookNameTuple = collections.namedtuple('AddressBook_1',
                                              ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

address_book_1 = AddressBookNameTuple(4567, 'Efim', '12-78-563', 'Kherson/Ukraine', 'efim@just.com', '04/07/2002', 18)
print(address_book_1)


# 8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'{__class__.__name__}(key = {self.key}, name = {self.name}, phone_number = {self.phone_number}, ' \
               f'address = {self.address}, email = {self.email}, birthday = {self.birthday}, age = {self.age}) '


address_book_2 = AddressBook(7632, 'Jan', '23-48-149', 'Riga/Latvia', 'jan@just.com', '03/03/2000', 20)
print(address_book_2)


# 9
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
print('person age = ', person.age)
person.age = 21
print('person age = ', person.age)


# 10
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(id=2045, name='Efim')

student.email = 'efim@just.com'
student_email = getattr(student, 'email')
print(student_email)


# 11
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


celsius_temp = 14.5
t = Celsius(celsius_temp)

print(f'{celsius_temp}\u2103 is {t.temperature}\u2109')

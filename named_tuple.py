import dataclasses
import collections


@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


AddressBookNameTuple = collections.namedtuple('AddressBook_1',
                                      ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

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

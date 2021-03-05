from cursore_hw.oop_2_hw_5.change_the_value import Person
from cursore_hw.oop_2_hw_5.classmethod import Pasta
from cursore_hw.oop_2_hw_5.getter_setter import student_email
from cursore_hw.oop_2_hw_5.named_tuple import AddressBookDataClass, AddressBookNameTuple, AddressBook
from cursore_hw.oop_2_hw_5.property import Concert, Celsius
from cursore_hw.oop_2_hw_5.staticmethod import Calc

numbers = Calc()
print(Calc.add_nums(15, 28, -45))

pasta_1 = Pasta(['mushrooms', 'parmesan'])
print(f'pasta_1 ingredients are {pasta_1.ingredient}')
pasta_2 = Pasta.bolognaise()
print(f'pasta_2 ingredients are {pasta_2.ingredient}')
pasta_3 = Pasta.carbonara()
print(f'pasta_3 ingredients are {pasta_3.ingredient}')

concert_1 = Concert
concert_2 = Concert

Concert.max_visitors_num = 250

print('concert_1.max_visitors_num:', concert_1.max_visitors_num)
Concert.visitors_count = 698
print('concert_1.visitors_count:', concert_1.visitors_count)

Concert.max_visitors_num = 784

print('concert_2.max_visitors_num:', concert_1.max_visitors_num)
Concert.visitors_count = 452
print('concert_2.visitors_count:', concert_1.visitors_count)

address_book = AddressBookDataClass(5879, 'Jason', '54-78-236', 'Minsk/Belorussia', 'jason@test.com', '13/05/1994', 26)
print(address_book)

address_book_1 = AddressBookNameTuple(4567, 'Efim', '12-78-563', 'Kherson/Ukraine', 'efim@just.com', '04/07/2002', 18)
print(address_book_1)

address_book_2 = AddressBook(7632, 'Jan', '23-48-149', 'Riga/Latvia', 'jan@just.com', '03/03/2000', 20)
print(address_book_2)

person = Person()
print('person age = ', person.age)
person.age = 21
print('person age = ', person.age)

print(student_email)

celsius_temp = 14.5
t = Celsius(celsius_temp)

print(f'{celsius_temp}\u2103 is {t.temperature}\u2109')

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass 

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        for user_phone in self.phones:
            if user_phone == phone:
                self.phones.remove(user_phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones = [new_phone if phone == old_phone else phone for phone in self.phones]
    

    def find_phone(self, phone):
        for user_phone in self.phones:
            if user_phone == phone:
                return user_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    
class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()

    def add_record(self, record):
        name = record.name.value
        self.data[name] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return "No contact found."
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact '{name}' deleted."
        else:
            return f"Contact '{name}' not found."


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
# book.delete("Jane")




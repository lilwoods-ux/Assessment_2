class Person:

    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self._age = age
        self.__salary = salary
    def name(self):
        return self.name
    def get_age(self):
        return self._age
    def get__salary(self):
        return self.__salary
    def display_info(self)->None:
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary: {self.__salary}")



person_1 = Person("Timothy", 20, 600000)
print(person_1.name)
print(person_1.get_age())
print(person_1.get__salary())
person_1.display_info()

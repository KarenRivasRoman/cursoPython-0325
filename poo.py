class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, ni nombre es {self.name} y tengo {self.age}")

person1 = Person("Ana",27)
person2 = Person("Luis",15)

person1.greet()
person2.greet()
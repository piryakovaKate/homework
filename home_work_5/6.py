class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Zebra(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return self.color

    def print_self(self):
        print('name:', self.get_name())
        print('age:', self.get_age())
        print('color:', self.get_color())


class Dolphin(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return self.color

    def print_self(self):
        print('name:', self.get_name())
        print('age:', self.get_age())
        print('color:', self.get_color())


print('Характеристики зебры',"\n")
a = Zebra('Марти', 4, 'красный')
a.print_self()
print('Характеристики дельфина',"\n")
b = Dolphin('Туби', 7,'фиолетовый')
b.print_self()

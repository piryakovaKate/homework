class Mother:
    def __str__(self):
        return "MOTHER"


class Daughter(Mother):
    def __str__(self):
        return "DAUGHTER"



a = Daughter()
b = Mother()
print(a)
print(b)

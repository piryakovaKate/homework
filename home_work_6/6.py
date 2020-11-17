class Complex:

    def __init__(self, re, im):
        self.a = re
        self.b = im

    def __str__(self):
        if self.b < 0:
            return (str(self.a)+' '+str(self.b)+'i')
        if self.b == 0:
            return (str(self.a))
        return (str(self.a)+' + '+str(self.b)+'i')

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        return Complex((self.a * other.a - self.b * other.b)/(other.a**2 + other.b**2),
                       (other.a * self.b - self.a * other.b) / (self.b**2 + other.b**2))

    def __pow__(self,other):
        a = self.a
        b = self.a
        step=other.a
        for i in range (step-1):
            a = self.a * a - self.b * b
            b = b * self.a + a * self.b
        return Complex(a,b)

    def __neg__(self):
        return Complex(self.a, - self.b)

    def __abs__(self):
        return (self.a**2 + self.b**2)**0.5

a=Complex(3,5)
b=Complex(4,7)
c=Complex(2,0)

print(a+b) 
print(b-a) 
print(a-b) 
print(a/b) 
print(a*b) 
print(a**c) 
print(-a) 
print(abs(a)) 

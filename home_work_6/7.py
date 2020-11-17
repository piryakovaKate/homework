class Vector:

    def __init__(self, a):
        arr=list(map(int,a.split(',')))
        self.x = arr[0]
        self.y = arr[1]
        self.z = arr[2]

    def __add__(self, other):
        return Vector('{},{},{}'.format(self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        return Vector('{},{},{}'.format(self.x - other.x, self.y - other.y, self.z - other.z))

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __and__(self, other):
        return Vector('{},{},{}'.format(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x))


    def __str__(self):
        return f"{self.x,self.y,self.z}"


vect1=Vector('1,2,3')
vect2=Vector ('3,4,5')

print("Sum:",vect1+vect2)
print("Sub:",vect1-vect2) 
print("Mul:",vect1*vect2) 
print("And:",vect1 & vect2) 

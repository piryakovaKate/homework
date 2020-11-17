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

    def dist(self):
        return round((self.x**2 + self.y**2 + self.z**2)**0.5, 2)

    def __str__(self):
        return f"{self.x,self.y,self.z}"


maximum = float('-inf')
N = int(input())
for i in range(N):
    Vec = []
    A = list(map(int,input().split()))
    v = Vector('{},{},{}'.format(A[0],A[1],A[2]))
    distant = Vector.dist(v)
    if distant >= maximum:
        maximum = distant
        Vec.append(A)
print ("Vec::", *Vec)


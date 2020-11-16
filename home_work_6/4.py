import math
class MyMath:

    @staticmethod
    def sin(self, x):
        return math.sin(x)

    @staticmethod 
    def pi():
        return 3.14

    @classmethod
    def _complex(cls):
        return False

    @classmethod
    def sqrt(cls, x):
        try:
            if cls._complex():
                return (math.sqrt(-x), 'i')
            else:
                return math.sqrt(x)
        except ValueError:
            return "Error"


class MyComplexMath(MyMath):

    @classmethod
    def _complex(cls):
        return True

print(MyMath.sqrt(25))
print(MyComplexMath.sqrt(-25))
print(MyMath.sqrt(-25))

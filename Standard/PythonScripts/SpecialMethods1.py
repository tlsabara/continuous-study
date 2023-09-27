from __future__ import annotations

class IntegerVector:
    def __init__(self,x: int,  y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("X and Y values shold be an integer.")

        self.x = x
        self.y = y

    @staticmethod
    def __check_other(other: any) -> None:
        if not isinstance(other, IntegerVector):
            raise ValueError("Math operations on can be done between Vectors")

    def __repr__(self) -> str:
        return f"IntegerVector<x={self.x}, y={self.y}>"

    def __add__(self, other: IntegerVector) -> IntegerVector:
        self.__check_other(other)

        x = self.x + other.x
        y = self.y + other.y

        return IntegerVector(x, y)


    def __sub__(self, other: IntegerVector) -> IntegerVector:
        self.__check_other(other)

        x = self.x - other.x
        y = self.y - other.y

        return IntegerVector(x, y)



if __name__ == '__main__':
    p1 = IntegerVector(1, 2)
    print(p1)

    p2 = IntegerVector(4, 23)
    print(p2)

    p3 = p1 + p2
    print(p3)

    p4 = p1 - p2
    print(p4)
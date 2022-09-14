def get_ab(point1, point2):
    cat_vert = point1[1] - point2[1]
    cat_hor = point1[0] - point2[0]
    a = cat_vert / cat_hor
    b = point2[1] - a * point2[0]
    return a, b


class PieceWise:
    __plot = {}

    def __init__(self, x, y):
        self.__plot[x] = y

    def __call__(self, x=0, y=0):
        return PieceWise(x, y)

    def __str__(self):
        return str(self.__plot)


    def y(self, x):
        if x in self.__plot.keys():
            return self.__plot[x]
        else:
            abscissa = [i for i in sorted(self.__plot.keys())]
            for i in range(0, len(abscissa) - 1):
                if abscissa[i] < x < abscissa[i + 1]:
                    p1 = (abscissa[i], self.__plot[abscissa[i]])
                    p2 = (abscissa[i + 1], self.__plot[abscissa[i + 1]])
                    a, b = get_ab(p1, p2)
                    y = a * x + b
                    return y
            return "Нет такой точки"

    def table(self):
        print("-" * 67)
        print("{:6} {:^8} {:>6}".format("|", "x1", "|"), end="")
        print("{:^20}".format("x2"), end="")
        print("{:4} {:7}".format("|", "a"), end="")
        print("{:1} {:^9} {:>1}".format("|", "b", "|"))
        print("-" * 67)
        counter = 1
        prev_point = None
        for i in sorted(self.__plot.items()):
            if counter == 2:
                print("{:2} {:^16} {:>2}".format("|", str(i), "|"), end="")
                if prev_point is not None:
                    a, b = get_ab(prev_point, i)
                    print("{:^10.3f} {:1}".format(a, "|"), end="")
                    print("{:^10.3f} {:1}".format(b, "|"))
                    print("-" * 67)
                counter = 1
            if i[0] != max(self.__plot.keys()):
                print("{:2} {:^16} {:1}".format("|", str(i), " "), end="")
                counter += 1
                prev_point = i


if __name__ == '__main__':
    f = PieceWise(0, 0)(1, 1)(-4, -9)
    f = f(2, 40)(5, 5)(2, 15)
    print(f)
    print(f.y(4))
    f.table()

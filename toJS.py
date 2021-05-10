    def fromUntil(self, a) -> tuple:
        """2 Zahlen sollen ein ordentlicher Zahlenbereich sein, sonst werden sie es

        @rtype: tuple[int,int]
        @return: Eine Bereichsangabe
        """
        if a[0].isdecimal():
            a[0] = int(a[0])
            if len(a) == 2 and a[1].isdecimal():
                a[1] = int(a[1])
            elif len(a) == 1:
                swap = a[0]
                a[0] = 1
                a += [swap]
                a[0] = 1
            else:
                return (1, 1)
            return tuple(a)
        else:
            return (1, 1)



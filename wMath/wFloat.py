import wInt


class wFloat:

    def __init__(self, val, decimalDetail=32):

        def str2wFloat(s):
            dot = False
            for x in s:
                if x not in '.0123456789':
                    raise ValueError(s + ' is not a valid value for wFloat')
                if x != '.':
                    if not dot:
                        self.lDec += x
                    else:
                        self.rDec += x
                else:
                    dot = True

        self.lOd = decimalDetail
        self.isNegative = False
        self.lDec = ''
        self.rDec = ''
        if isinstance(val, str):
            if val[0] == '-':
                self.isNegative = True
                str2wFloat(val[1:])
            else:
                str2wFloat(val)
        if isinstance(val, float):
            if val < 0:
                self.isNegative = True
                str2wFloat(str(-val))
            else:
                str2wFloat(str(val))
        if isinstance(val, int):
            if val < 0:
                self.isNegative = True
                self.lDec = str(-val)
            else:
                self.lDec = str(val)
            self.rDec = '0'
        c0 = -1
        for x in self.lDec:
            if x == '0':
                c0 += 1
            else:
                break
        if c0 != -1:
            self.lDec = self.lDec[(1 + c0):]
        if self.lDec == '':
            self.lDec = '0'
        c0 = 0
        for x in range(len(self.rDec) - 1, -1, -1):
            if self.rDec[x] == '0':
                c0 += 1
            else:
                break
        if c0 != 0:
            self.rDec = self.rDec[:-c0]
        if self.rDec == '':
            self.rDec = '0'
        if self.lDec == '0' and self.rDec == '0':
            self.isNegative = False

    def __add__(self, other):
        if len(self.rDec) > len(other.rDec):
            m = len(self.rDec)
            c = self.lDec + self.rDec
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec + '0' * (m - len(other.rDec))
            if other.isNegative:
                d = '-' + d
            a = wInt.wInt(c) + wInt.wInt(d)
        else:
            m = len(other.rDec)
            c = other.lDec + other.rDec
            if other.isNegative:
                c = '-' + c
            d = self.lDec + self.rDec + '0' * (m - len(self.rDec))
            if self.isNegative:
                d = '-' + d
            a = wInt.wInt(c) + wInt.wInt(d)
        if a.isNegative:
            return wFloat('-' + a.val[:-2] + '.' + a.val[-2:])
        else:
            return wFloat(a.val[:-2] + '.' + a.val[-2:])

    def __sub__(self, other):
        if len(self.rDec) > len(other.rDec):
            m = len(self.rDec)
            c = self.lDec + self.rDec
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec + '0' * (m - len(other.rDec))
            if other.isNegative:
                d = '-' + d
            a = wInt.wInt(c) - wInt.wInt(d)
        else:
            m = len(other.rDec)
            c = self.lDec + self.rDec + '0' * (m - len(self.rDec))
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec
            if other.isNegative:
                d = '-' + d
            a = wInt.wInt(c) - wInt.wInt(d)
        if a.isNegative:
            return wFloat('-' + a.val[:-2] + '.' + a.val[-2:])
        else:
            return wFloat(a.val[:-2] + '.' + a.val[-2:])

    def __mul__(self, other):
        lOd = min([self.lOd, other.lOd])
        c = wInt.wInt(self.lDec + self.rDec)
        d = wInt.wInt(other.lDec + other.rDec)
        negate = self.isNegative ^ other.isNegative
        dLen = len(self.rDec + other.rDec)
        m = c * d
        j = str(m)[:-dLen] + '.' + str(m)[-dLen:]
        if negate:
            return wFloat('-' + str(j), lOd)
        else:
            return wFloat(str(j), lOd)

    def __truediv__(self, other):
        print(' DIV ' + str(self) + ' * ' + str(other) + ' = ', end='')
        introLen = 11 + len(str(self) + str(other))
        vLen = 0
        negate = self.isNegative ^ other.isNegative
        if other.rDec != '0':
            dLen = len(other.rDec)
            add = self.rDec + '0' * dLen
            o_divisor = wInt.wInt(other.lDec + other.rDec, other.lOd)
            o_dividend = wFloat(self.lDec + add[:dLen] + '.' + self.rDec[dLen:], self.lOd)
        else:
            o_divisor = wInt.wInt(other.lDec, other.lOd)
            o_dividend = self
        dLen = min([o_dividend.lOd, o_divisor.lOd])
        n = o_dividend.rDec
        if len(n) < dLen:
            n += '0' * (dLen - len(n))
        else:
            i = False
            fI = False
            breakIT = False
            for x in n[dLen:]:
                if fI and (x != '0'):
                    breakIT = True
                    i = True
                if (x in '01234') and (not fI):
                    break
                if (x in '6789') and (not fI):
                    i = True
                    break
                if (x == '5') and (not fI):
                    fI = True
                if breakIT:
                    break
            n = n[:dLen]
            if i:
                n = wInt.wInt(n) + wInt.wInt('0' * dLen + '1')
            else:
                if fI:
                    if int(n[-1]) % 2 != 0:
                        n = wInt.wInt(n) + wInt.wInt('0' * dLen + '1')
        o_dividend = o_dividend.lDec + '.' + n
        quo = ''
        dVal = wInt.wInt(0)
        while len(o_dividend) > 0:
            if o_dividend[0] != '.':
                dVal = wInt.wInt(dVal.val + o_dividend[0], 0)
                o_dividend = o_dividend[1:]
            else:
                quo += '.'
                o_dividend = o_dividend[1:]
                dVal = wInt.wInt(dVal.val + o_dividend[0], 0)
                o_dividend = o_dividend[1:]
            for x in range(10):
                k = o_divisor * x
                s = dVal - k
                if s < 0:
                    quo += str(x - 1)
                    dVal -= o_divisor * (x - 1)
                    break
                if x == 9:
                    quo += '9'
                    dVal -= o_divisor * 9
            print('\b' * vLen, end='')
            print(quo, end='')
            vLen = len(quo)
        print('\b' * (vLen + introLen), end='')
        if negate:
            return wFloat('-' + quo)
        else:
            return wFloat(quo)

    def __floordiv__(self, other):
        return wFloat((self / other).lDec, min([self.lOd, other.lOd]))

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __idiv__(self, other):
        return self / other

    def __ifloordiv__(self, other):
        return self // other

    def __neg__(self):
        if self.isNegative:
            self.isNegative = False
        else:
            self.isNegative = True

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.lDec + '.' + self.rDec
        return out

    def __eq__(self, other):
        if self.isNegative == other.isNegative:
            if self.lDec == other.lDec:
                if self.rDec == other.rDec:
                    return True
        return False

    def __gt__(self, other):
        a, b = self.unify(self, other)
        if a > b:
            return True
        return False

    def __lt__(self, other):
        a, b = self.unify(self, other)
        if a < b:
            return True
        return False

    def __ge__(self, other):
        a, b = self.unify(self, other)
        if a >= b:
            return True
        return False

    def __le__(self, other):
        a, b = self.unify(self, other)
        if a <= b:
            return True
        return False

    def __abs__(self):
        k = self
        k.isNegative = False
        return k

    @staticmethod
    def unify(a, b):
        if len(a.rDec) > len(b.rDec):
            m = a.lDec + a.rDec
            if a.isNegative:
                m = wInt.wInt('-' + m)
            else:
                m = wInt.wInt(m)
            n = b.lDec + b.rDec + '0' * (len(a.rDec) - len(b.rDec))
            if b.isNegative:
                n = wInt.wInt('-' + n)
            else:
                n = wInt.wInt(n)
        else:
            m = a.lDec + a.rDec + '0' * (len(b.rDec) - len(a.rDec))
            if a.isNegative:
                m = wInt.wInt('-' + m)
            else:
                m = wInt.wInt(m)
            n = b.lDec + b.rDec
            if b.isNegative:
                n = wInt.wInt('-' + n)
            else:
                n = wInt.wInt(n)
        return m, n

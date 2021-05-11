import wINT


class weirdFLOAT:

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
        if isinstance(val, wINT.weirdINT):
            if val < wINT.weirdINT(0):
                self.isNegative = True
            self.lDec = str(val)
            self.rDec = '0'
            self.lOd = val.lOd
        if isinstance(val, weirdFLOAT):
            self.isNegative = val.isNegative
            self.lDec = val.lDec
            self.rDec = val.rDec
            self.lOd = val.lOd
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
        other = self.otherFix(other)
        if len(self.rDec) > len(other.rDec):
            m = len(self.rDec)
            c = self.lDec + self.rDec
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec + '0' * (m - len(other.rDec))
            if other.isNegative:
                d = '-' + d
            a = wINT.weirdINT(c) + wINT.weirdINT(d)
        else:
            m = len(other.rDec)
            c = other.lDec + other.rDec
            if other.isNegative:
                c = '-' + c
            d = self.lDec + self.rDec + '0' * (m - len(self.rDec))
            if self.isNegative:
                d = '-' + d
            a = wINT.weirdINT(c) + wINT.weirdINT(d)
        if a.isNegative:
            return weirdFLOAT('-' + a.val[:-m] + '.' + a.val[-m:])
        else:
            return weirdFLOAT(a.val[:-m] + '.' + a.val[-m:])

    def __sub__(self, other):
        other = self.otherFix(other)
        if len(self.rDec) > len(other.rDec):
            m = len(self.rDec)
            c = self.lDec + self.rDec
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec + '0' * (m - len(other.rDec))
            if other.isNegative:
                d = '-' + d
            a = wINT.weirdINT(c) - wINT.weirdINT(d)
        else:
            m = len(other.rDec)
            c = self.lDec + self.rDec + '0' * (m - len(self.rDec))
            if self.isNegative:
                c = '-' + c
            d = other.lDec + other.rDec
            if other.isNegative:
                d = '-' + d
            a = wINT.weirdINT(c) - wINT.weirdINT(d)
        if a.isNegative:
            return weirdFLOAT('-' + a.val[:-2] + '.' + a.val[-2:])
        else:
            return weirdFLOAT(a.val[:-2] + '.' + a.val[-2:])

    def __mul__(self, other):
        other = self.otherFix(other)
        lOd = min([self.lOd, other.lOd])
        c = wINT.weirdINT(self.lDec + self.rDec)
        d = wINT.weirdINT(other.lDec + other.rDec)
        negate = self.isNegative ^ other.isNegative
        dLen = len(self.rDec + other.rDec)
        m = c * d
        j = str(m)[:-dLen] + '.' + str(m)[-dLen:]
        if negate:
            return weirdFLOAT('-' + str(j), lOd)
        else:
            return weirdFLOAT(str(j), lOd)

    def __truediv__(self, other):
        other = self.otherFix(other)
        print(' DIV ' + str(self) + ' * ' + str(other) + ' = ', end='')
        introLen = 11 + len(str(self) + str(other))
        vLen = 0
        negate = self.isNegative ^ other.isNegative
        if other.rDec != '0':
            dLen = len(other.rDec)
            add = self.rDec + '0' * dLen
            o_divisor = wINT.weirdINT(other.lDec + other.rDec, other.lOd)
            o_dividend = weirdFLOAT(self.lDec + add[:dLen] + '.' + self.rDec[dLen:], self.lOd)
        else:
            o_divisor = wINT.weirdINT(other.lDec, other.lOd)
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
                n = wINT.weirdINT(n) + wINT.weirdINT('0' * dLen + '1')
            else:
                if fI:
                    if int(n[-1]) % 2 != 0:
                        n = wINT.weirdINT(n) + wINT.weirdINT('0' * dLen + '1')
        o_dividend = o_dividend.lDec + '.' + n
        quo = ''
        dVal = wINT.weirdINT(0)
        while len(o_dividend) > 0:
            if o_dividend[0] != '.':
                dVal = wINT.weirdINT(dVal.val + o_dividend[0], 0)
                o_dividend = o_dividend[1:]
            else:
                quo += '.'
                o_dividend = o_dividend[1:]
                dVal = wINT.weirdINT(dVal.val + o_dividend[0], 0)
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
            return weirdFLOAT('-' + quo)
        else:
            return weirdFLOAT(quo)

    def __floordiv__(self, other):
        other = self.otherFix(other)
        return weirdFLOAT((self / other).lDec, min([self.lOd, other.lOd]))

    def __iadd__(self, other):
        other = self.otherFix(other)
        return self + other

    def __isub__(self, other):
        other = self.otherFix(other)
        return self - other

    def __imul__(self, other):
        other = self.otherFix(other)
        return self * other

    def __idiv__(self, other):
        other = self.otherFix(other)
        return self / other

    def __ifloordiv__(self, other):
        other = self.otherFix(other)
        return self // other

    def __neg__(self):
        k = self
        if self.isNegative:
            k.isNegative = False
        else:
            k.isNegative = True
        return k

    def __eq__(self, other):
        other = self.otherFix(other)
        if self.isNegative == other.isNegative:
            if self.lDec == other.lDec:
                if self.rDec == other.rDec:
                    return True
        return False

    def __gt__(self, other):
        other = self.otherFix(other)
        a, b = self.unify(self, other)
        if a > b:
            return True
        return False

    def __lt__(self, other):
        other = self.otherFix(other)
        a, b = self.unify(self, other)
        if a < b:
            return True
        return False

    def __ge__(self, other):
        other = self.otherFix(other)
        a, b = self.unify(self, other)
        if a >= b:
            return True
        return False

    def __le__(self, other):
        other = self.otherFix(other)
        a, b = self.unify(self, other)
        if a <= b:
            return True
        return False

    def __abs__(self):
        k = self
        k.isNegative = False
        return k

    def __round__(self, n=None):
        isN = False
        if n is None:
            n = 0
            isN = True
        if self.isNegative:
            out = '-' + self.lDec
        else:
            out = self.lDec
        out += '.' + self.rDec[:n]
        fI = False
        breakIT = False
        i = False
        for x in self.rDec[n:]:
            if fI:
                if x in '123456789':
                    i = True
                    breakIT = True
            if (x in '01234') and (not fI):
                i = False
                break
            if (x in '6789') and (not fI):
                i = True
                break
            if (x == '5') and (not fI):
                fI = True
            if breakIT:
                break
        if fI and (not i):
            if int(out[-1]) % 2 != 0:
                i = True
        if i:
            j = weirdFLOAT(out) + weirdFLOAT('0.' + '0' * (n - 1) + '1')
        else:
            j = weirdFLOAT(out)
        if isN:
            return wINT.weirdINT(j)
        return j

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.lDec + '.' + self.rDec
        return out

    @staticmethod
    def otherFix(other):
        if isinstance(other, wINT.weirdINT):
            j = weirdFLOAT('0.0')
            j.lDec = other.val
            j.rDec = '0'
            j.isNegative = other.isNegative
            other = j
        elif isinstance(other, int):
            other = weirdFLOAT(other)
        elif isinstance(other, weirdFLOAT):
            pass
        elif isinstance(other, float):
            other = weirdFLOAT(other)
        elif isinstance(other, str):
            other = weirdFLOAT(other)
        else:
            raise TypeError(
                str(type(other)) + ' cannot be operated with wFloat. Give int, float, wInt or wFloat instead')
        return other

    @staticmethod
    def unify(a, b):
        if len(a.rDec) > len(b.rDec):
            m = a.lDec + a.rDec
            if a.isNegative:
                m = wINT.weirdINT('-' + m)
            else:
                m = wINT.weirdINT(m)
            n = b.lDec + b.rDec + '0' * (len(a.rDec) - len(b.rDec))
            if b.isNegative:
                n = wINT.weirdINT('-' + n)
            else:
                n = wINT.weirdINT(n)
        else:
            m = a.lDec + a.rDec + '0' * (len(b.rDec) - len(a.rDec))
            if a.isNegative:
                m = wINT.weirdINT('-' + m)
            else:
                m = wINT.weirdINT(m)
            n = b.lDec + b.rDec
            if b.isNegative:
                n = wINT.weirdINT('-' + n)
            else:
                n = wINT.weirdINT(n)
        return m, n

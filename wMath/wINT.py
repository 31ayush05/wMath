import wFLOAT


class weirdINT:

    def __init__(self, val, decimalDetail=32):
        self.lOd = decimalDetail
        self.isNegative = False
        self.val = '0'
        if isinstance(val, int):
            if val < 0:
                self.isNegative = True
                self.val = str(-val)
            else:
                self.val = str(val)
        if isinstance(val, float):
            if val < 0:
                self.isNegative = True
                val = str(-val)
            else:
                val = str(val)
            for x in val:
                if x == '.':
                    break
                else:
                    self.val += x
        if isinstance(val, str):
            add = True
            k = ''
            if val[0] == '-':
                self.isNegative = True
                val = val[1:]
            for x in val:
                if add:
                    if x in '.0123456789':
                        if x == '.':
                            add = False
                        else:
                            k += x
                    else:
                        raise ValueError('Invalid value for wInt')
                else:
                    if x not in '01234567989':
                        raise ValueError('Invalid value for wInt')
            self.val = k
        if isinstance(val, weirdINT):
            self.isNegative = val.isNegative
            self.lOd = val.lOd
            self.val = val.val
        if isinstance(val, wFLOAT.weirdFLOAT):
            self.isNegative = val.isNegative
            self.lOd = val.lOd
            self.val = val.lDec
        c0 = -1
        for x in self.val:
            if x == '0':
                c0 += 1
            else:
                break
        if c0 != -1:
            self.val = self.val[(1 + c0):]
        if self.val == '':
            self.val = '0'
        if self.val == '0':
            self.isNegative = False

    def __add__(self, other):

        def ADD(classAccess, a, b):
            print(' ADD ' + a + ' + ' + b + ' = ', end='')
            introLen = 11 + len(a + b)
            vLen = 0
            a, b = classAccess.unify(a, b)
            out = ''
            carry = 0
            for x in range(len(a) - 1, -1, -1):
                cVal = int(a[x]) + int(b[x]) + carry
                if cVal > 9:
                    carry = 1
                    cVal -= 10
                else:
                    carry = 0
                out = str(cVal) + out
                print('\b' * vLen, end='')
                vLen = len(out)
                print(out, end='')
            if carry != 0:
                out = str(carry) + out
                print('\b' * vLen, end='')
                vLen = len(out)
                print(out, end='')
            print('\b' * (vLen + introLen), end='')
            return out

        other = self.otherFix(other)
        if self.isNegative and (not other.isNegative):  # (+) + (-)
            return weirdINT(other.val) - weirdINT(self.val)
        elif (not self.isNegative) and other.isNegative:  # (-) + (+)
            return weirdINT(self.val) - weirdINT(other.val)
        elif self.isNegative and other.isNegative:  # (-) + (-)
            return weirdINT('-' + ADD(self, self.val, other.val))
        else:  # (+) + (+)
            return weirdINT(ADD(self, self.val, other.val))

    def __sub__(self, other):

        def SUB(classAccess, a, b):
            print(' SUB ' + a + ' - ' + b + ' = ', end='')
            introLen = 11 + len(a + b)
            vLen = 0
            a, b = classAccess.unify(a, b)
            out = ''
            negate = False
            if a == b:
                print('\b' * introLen, end='')
                return '0'
            if weirdINT(b) > weirdINT(a):
                a, b = b, a
                negate = True
            for x in range(len(a) - 1, -1, -1):
                if int(a[x]) < int(b[x]):
                    if a[x] == '0' and a[x - 1] == '0':
                        for y in range(x - 1, -1, -1):
                            if a[y] == '0':
                                a = a[:y] + '9' + a[y + 1:]
                            else:
                                a = a[:y] + str(int(a[y]) - 1) + a[y + 1:]
                                break
                    else:
                        if a[x - 1] == '0':
                            for z in range(x - 1, -1, -1):
                                if a[z] == '0':
                                    a = a[:z] + '9' + a[z + 1:]
                                else:
                                    a = a[:z] + str(int(a[z]) - 1) + a[z + 1:]
                                    break
                        else:
                            a = a[:x - 1] + str(int(a[x - 1]) - 1) + a[x:]
                    cVal = str(10 + int(a[x]) - int(b[x]))
                else:
                    cVal = int(a[x]) - int(b[x])
                out = str(cVal) + out
                print('\b' * vLen, end='')
                vLen = len(out)
                print(out, end='')
            if negate:
                out = '-' + out
                print('\b' * vLen, end='')
                vLen = len(out)
                print(out, end='')
            print('\b' * (vLen + introLen), end='')
            return out

        other = self.otherFix(other)
        if self.isNegative and (not other.isNegative):  # (-) - (+)
            return weirdINT('-' + (weirdINT(self.val) + weirdINT(other.val)).val)
        elif (not self.isNegative) and other.isNegative:  # (+) - (-)
            return weirdINT(other.val) + weirdINT(self.val)
        elif self.isNegative and other.isNegative:  # (-) - (-)
            return weirdINT(SUB(self, other.val, self.val))
        else:  # (+) - (+)
            return weirdINT(SUB(self, self.val, other.val))

    def __mul__(self, other):
        other = self.otherFix(other)
        negate = self.isNegative ^ other.isNegative
        print(' MUL ' + self.val + ' * ' + other.val + ' = ', end='')
        introLen = 11 + len(self.val + other.val)
        vLen = 0
        a, b = self.unify(self.val, other.val)
        l = len(a)
        mX = 2 * (l - 1)
        se = []
        carry = weirdINT(0)
        out = ''
        for m in range(2 * l - 1):
            cVal = weirdINT(0)
            if m == 0:
                se = [l - 1, l - 1]
            else:
                if se[0] != 0:
                    se[0] -= 1
                else:
                    se[1] -= 1
            sampleSpace = []
            for x in range(se[0], se[1] + 1):
                sampleSpace.append(x)
            sX = mX - m
            for x in range(len(sampleSpace)):
                for y in range(len(sampleSpace)):
                    if int(sampleSpace[x]) + int(sampleSpace[y]) == sX:
                        cVal += weirdINT(int(a[sampleSpace[x]]) * int(b[sampleSpace[y]]))
            cVal += carry
            if cVal > weirdINT(9):
                out = cVal.val[-1] + out
                carry = weirdINT(cVal.val[:-1])
            else:
                out = str(cVal.val) + out
                carry = weirdINT(0)
            print('\b' * vLen, end='')
            vLen = len(out)
            print(out, end='')
        if carry > weirdINT(0):
            out = carry.val + out
        if negate:
            out = '-' + out
            print('\b' * vLen, end='')
            vLen = len(out)
            print(out, end='')
        print('\b' * (vLen + introLen), end='')
        return weirdINT(out)

    def __truediv__(self, other):
        other = self.otherFix(other)
        return wFLOAT.weirdFLOAT(self.val, self.lOd) / wFLOAT.weirdFLOAT(other.val, other.lOd)

    def __floordiv__(self, other):
        other = self.otherFix(other)
        return weirdINT((self / other).lDec, max([self.lOd, other.lOd]))

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
        if self.val == other.val:
            if self.isNegative == other.isNegative:
                return True
        return False

    def __gt__(self, other):
        other = self.otherFix(other)
        if isinstance(other, int):
            other = weirdINT(other)
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) > int(b[x]):
                if (self.isNegative and (not other.isNegative)) or (self.isNegative and other.isNegative):
                    return False
                return True
            if int(a[x]) < int(b[x]):
                if ((not self.isNegative) and other.isNegative) or (self.isNegative and other.isNegative):
                    return True
                return False
        return False

    def __lt__(self, other):
        other = self.otherFix(other)
        if isinstance(other, int):
            other = weirdINT(other)
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) < int(b[x]):
                if ((not self.isNegative) and other.isNegative) or (self.isNegative and other.isNegative):
                    return False
                return True
            if int(a[x]) > int(b[x]):
                if (self.isNegative and (not other.isNegative)) or (self.isNegative and other.isNegative):
                    return True
                return False
        return False

    def __ge__(self, other):
        other = self.otherFix(other)
        if isinstance(other, int):
            other = weirdINT(other)
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) > int(b[x]):
                if (self.isNegative and (not other.isNegative)) or (self.isNegative and other.isNegative):
                    return False
                return True
            if int(a[x]) < int(b[x]):
                if ((not self.isNegative) and other.isNegative) or (self.isNegative and other.isNegative):
                    return True
                return False
        return True

    def __le__(self, other):
        other = self.otherFix(other)
        if isinstance(other, int):
            other = weirdINT(other)
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) < int(b[x]):
                if ((not self.isNegative) and other.isNegative) or (self.isNegative and other.isNegative):
                    return False
                return True
            if int(a[x]) > int(b[x]):
                if (self.isNegative and (not other.isNegative)) or (self.isNegative and other.isNegative):
                    return True
                return False
        return True

    def __abs__(self):
        k = self
        k.isNegative = False
        return k

    def __round__(self, n=None):
        return self

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.val
        return out

    @staticmethod
    def otherFix(other):
        if isinstance(other, weirdINT):
            pass
        elif isinstance(other, int):
            other = weirdINT(other)
        elif isinstance(other, wFLOAT.weirdFLOAT):
            j = weirdINT(0)
            j.isNegative = other.isNegative
            j.lOd = other.lOd
            j.val = other.lDec
            other = j
        elif isinstance(other, float):
            if other < 0:
                other = weirdINT('-' + str(-other))
            else:
                other = weirdINT(str(other))
        elif isinstance(other, str):
            add = True
            j = weirdINT(0)
            k = ''
            if other[0] == '-':
                j.isNegative = True
                other = other[1:]
            for x in other:
                if add:
                    if x in '.0123456789':
                        if x == '.':
                            add = False
                        else:
                            k += x
                    else:
                        raise ValueError('Invalid value for wInt')
                else:
                    if x not in '01234567989':
                        raise ValueError('Invalid value for wInt')
            j.val = k
            other = j
        else:
            raise TypeError(
                str(type(other)) + ' cannot be operated with wFloat. Give int, float, wInt or wFloat instead')
        return other

    @staticmethod
    def unify(a, b):
        m = max([len(a), len(b)])
        if len(a) < m:
            a = '0' * (m - len(a)) + a
        if len(b) < m:
            b = '0' * (m - len(b)) + b
        return a, b

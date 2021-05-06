class wINT:

    def __init__(self, val):
        self.isNegative = False
        self.val = '0'
        if isinstance(val, int):
            if val < 0:
                self.isNegative = True
                self.val = str(-val)
            else:
                self.val = str(val)
        if isinstance(val, str):
            if val[0] == '-':
                self.isNegative = True
                self.val = val[1:]
            else:
                self.isNegative = False
                self.val = val
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
            print('ADD ' + a + ' + ' + b + ' = ', end='')
            introLen = 10 + len(a + b)
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

        if self.isNegative and (not other.isNegative):  # (+) + (-)
            return wINT(other.val) - wINT(self.val)
        elif (not self.isNegative) and other.isNegative:  # (-) + (+)
            return wINT(self.val) - wINT(other.val)
        elif self.isNegative and other.isNegative:  # (-) + (-)
            return wINT('-' + ADD(self, self.val, other.val))
        else:  # (+) + (+)
            return wINT(ADD(self, self.val, other.val))

    def __sub__(self, other):

        def SUB(classAccess, a, b):
            print('SUB ' + a + ' - ' + b + ' = ', end='')
            introLen = 10 + len(a + b)
            vLen = 0
            a, b = classAccess.unify(a, b)
            out = ''
            negate = False
            if a == b:
                print('\b' * introLen, end='')
                return '0'
            if wINT(b) > wINT(a):
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

        if self.isNegative and (not other.isNegative):  # (-) - (+)
            return wINT('-' + (wINT(self.val) + wINT(other.val)).val)
        elif (not self.isNegative) and other.isNegative:  # (+) - (-)
            return wINT(other.val) + wINT(self.val)
        elif self.isNegative and other.isNegative:  # (-) - (-)
            return wINT(SUB(self, other.val, self.val))
        else:  # (+) - (+)
            return wINT(SUB(self, self.val, other.val))

    def __mul__(self, other):
        negate = self.isNegative ^ other.isNegative
        print('MUL ' + self.val + ' * ' + other.val + ' = ', end='')
        introLen = 10 + len(self.val + other.val)
        vLen = 0
        a, b = self.unify(self.val, other.val)
        l = len(a)
        mX = 2 * (l - 1)
        se = []
        carry = wINT(0)
        out = ''
        for m in range(2 * l - 1):
            cVal = wINT(0)
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
                        cVal += wINT(int(a[sampleSpace[x]]) * int(b[sampleSpace[y]]))
            cVal += carry
            if cVal > wINT(9):
                out = cVal.val[-1] + out
                carry = wINT(cVal.val[:-1])
            else:
                out = str(cVal.val) + out
                carry = wINT(0)
            print('\b' * vLen, end='')
            vLen = len(out)
            print(out, end='')
        if negate:
            out = '-' + out
            print('\b' * vLen, end='')
            vLen = len(out)
            print(out, end='')
        print('\b' * (vLen + introLen), end='')
        return wINT(out)

    def __gt__(self, other):
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) > int(b[x]):
                return True
            if int(a[x]) < int(b[x]):
                return False
        return False

    def __lt__(self, other):
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) < int(b[x]):
                return True
            if int(a[x]) > int(b[x]):
                return False
        return False

    def __ge__(self, other):
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) > int(b[x]):
                return True
            if int(a[x]) < int(b[x]):
                return False
        return True

    def __le__(self, other):
        a, b = self.unify(self.val, other.val)
        for x in range(len(a)):
            if int(a[x]) < int(b[x]):
                return True
            if int(a[x]) > int(b[x]):
                return False
        return True

    def __neg__(self):
        if self.isNegative:
            self.isNegative = False
        else:
            self.isNegative = True

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.val
        return out

    @staticmethod
    def unify(a, b):
        m = max([len(a), len(b)])
        if len(a) < m:
            a = '0' * (m - len(a)) + a
        if len(b) < m:
            b = '0' * (m - len(b)) + b
        return a, b

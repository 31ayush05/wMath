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
                    quo += str(x-1)
                    dVal -= o_divisor * (x-1)
                    break
                if x == 9:
                    quo += '9'
                    dVal -= o_divisor * 9
            print('\b'*vLen, end='')
            print(quo, end='')
            vLen = len(quo)
        print('\b' * (vLen + introLen), end='')
        if negate:
            return wFloat('-' + quo)
        else:
            return wFloat(quo)

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.lDec + '.' + self.rDec
        return out

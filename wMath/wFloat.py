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
        c0 = -1
        for x in range(len(self.rDec)-1, -1, -1):
            if self.rDec[x] == '0':
                c0 += 1
            else:
                break
        if c0 != -1:
            self.rDec = self.rDec[:c0]
        if self.rDec == '':
            self.rDec = '0'
        if self.lDec == '0' and self.rDec == '0':
            self.isNegative = False

    def __truediv__(self, other):
        pass

    def __str__(self):
        out = ''
        if self.isNegative:
            out += '-'
        out += self.lDec + '.' + self.rDec
        return out


a = wFloat('-56.55')
print(a)

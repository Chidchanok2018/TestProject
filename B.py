class BB:
    def TestB(self, a, z):
        # print(a)
        b = 'aaaa'
        b = 'bbbb'
        a = 'zzzz'
        b = a + str(z)
        return b

    def TestB2(self, i):
        i = i + 1
        if i < 5:
            BB().TestB2(i)
        print(i)
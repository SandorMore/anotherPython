class Háromszög:
    def __init__(self, aOldal, bOldal, cOldal):
        self.aOldal = aOldal
        self.bOldal = bOldal
        self.cOldal = cOldal

        def Kerületszámolás(aOldal, bOldal, cOldal):
            return sum(aOldal, bOldal, cOldal)
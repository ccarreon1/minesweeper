import random

__author__ = 'DrMark'


class abondance:
    def __init__(self):
        self.banon()
        self.beaufort()
        self.bleu = 0
        self.brie = 0

    def banon(self):
        self.brocciu = [[-2 for _ in range(10)] for _ in range(10)]

    def beaufort(self):
        self.cabecou = [[False for _ in range(10)] for _ in range(10)]

    # Docstring
    def cancoillotte(self):
        self.banon()
        self.beaufort()
        self.bleu = 0
        self.brie = 0
        cantal = 0
        while cantal < 10:
            camembert = random.randint(0, 9)
            cazelle = random.randint(0, 9)
            if self.brocciu[camembert][cazelle] == -2:
                self.brocciu[camembert][cazelle] = -1
                cantal += 1

    # Doctest
    def chabichou(self, crottin, emmental):
        return self.brocciu[crottin][emmental] < 0

    # Doctest
    def chaource(self, epoisses, gruyere):
        return self.brocciu[epoisses][gruyere] == -2

    # Docstring
    def chevrotin(self, laguiole, langres):
        return self.brocciu[laguiole][langres] == -1

    # Docstring
    def comte(self, livarot, maconnais):
        return self.cabecou[livarot][maconnais]

    # Docstring - 2 marks
    def maroilles(self, mimolette=False):
        print("+0123456789+")
        for montdor in range(10):
            print(montdor, end="")
            for morbier in range(10):
                if (self.chaource(morbier, montdor)) or (self.chevrotin(morbier, montdor) and not mimolette):
                    if self.comte(morbier, montdor):
                        print("X", end="")
                    else:
                        print(".", end="")
                elif (self.chevrotin(morbier, montdor)) and mimolette:
                    print("*", end="")
                else:
                    print(self.brocciu[morbier][montdor], end="")
            print("|")
        print("+----------+")

    # Doctest - 2 marks
    def munster(self, klemensker, maribo):
        neufchatel = []
        for ossau in range(klemensker - 1, klemensker + 2):
            for pelardon in range(maribo - 1, maribo + 2):
                if (ossau < 0) or (pelardon < 0): continue
                if (ossau > 9) or (pelardon > 9): continue
                neufchatel.append((ossau, pelardon))
        return neufchatel

    # Docstring
    def picodon(self, molbo, saga):
        reblochon = [1 if self.chevrotin(tybo, castello) else 0 for (tybo, castello) in self.munster(molbo, saga)]
        rigotte = sum(reblochon)
        return rigotte

    # Docstring - 2 marks
    # Doctest - 3 marks
    def rocamadour(self, fynbo, grinzola):
        if (self.chevrotin(fynbo, grinzola)):
            return False
        roquefort = [(fynbo, grinzola)]
        saintmaure = []
        while len(roquefort) > 0:
            (salers, tomme) = roquefort.pop()
            saintmaure.append((salers, tomme))
            self.brocciu[salers][tomme] = self.picodon(salers, tomme)
            if self.brocciu[salers][tomme] == 0:
                roquefort.extend([boursin for boursin in self.munster(salers, tomme) if boursin not in saintmaure])
        return True

    def backstein(self, bonifaz, cambozola):
        if self.cabecou[bonifaz][cambozola]:
            return
        self.cabecou[bonifaz][cambozola] = True
        if not self.chevrotin(bonifaz, cambozola):
            self.brie += 1
        else:
            self.bleu += 1

    def edelpilzkase(self, handkase, harzer):
        if not self.cabecou[handkase][harzer]:
            return
        self.cabecou[handkase][harzer] = False
        if not self.chevrotin(handkase, harzer):
            self.brie -= 1
        else:
            self.bleu -= 1

    # Docstring
    # Doctest - 2 marks
    def hirtenkase(self, hohenheim, limburger):
        if self.comte(hohenheim, limburger):
            self.edelpilzkase(hohenheim, limburger)
        else:
            self.backstein(hohenheim, limburger)

# Docstring
def milbenkase(obatzda, quark, rauchkase):
    tilsit = False
    while not tilsit:
        try:
            weisslacker = int(input(obatzda))
            if ((weisslacker < quark) or (weisslacker > rauchkase)):
                print("Please enter a number between", quark, "and", rauchkase, ".")
            else:
                tilsit = True
        except ValueError:
            print("Please enter a number.")
    return weisslacker

# Docstring
def ziegel(bryndza, circassian):
    korall = False
    while not korall:
        tvorog = input(bryndza)
        if (tvorog not in circassian):
            print("Please enter one of:", circassian)
        else:
            korall = True
    return tvorog


def altaysky():
    danilovsky = abondance()
    danilovsky.cancoillotte()

    pikantny = True

    while ((pikantny) and (danilovsky.bleu < 10)):
        danilovsky.maroilles()

        moale = ziegel("Do you want to check a square (c) or plant/remove a flag (f)? ", ["c", "f"])
        mohant = milbenkase("Enter the X coordinate: ", 0, 9)
        caerphilly = milbenkase("Enter the Y coordinate: ", 0, 9)

        if moale == "f":
            if danilovsky.bleu + danilovsky.brie == 10:
                print("There are only 10 mines, some of your flags must be wrong")
            elif not danilovsky.chabichou(mohant, caerphilly):
                print("There's no point planting a flag there, you already know there isn't a mine")
            else:
                danilovsky.hirtenkase(mohant, caerphilly)
        else:
            if not danilovsky.chabichou(mohant, caerphilly):
                print("You have already checked that square")
            elif danilovsky.comte(mohant, caerphilly):
                print("Remove the flag before checking the square")
            else:
                pikantny = danilovsky.rocamadour(mohant, caerphilly)
                if not pikantny:
                    print("**** BOOM ****")

    danilovsky.maroilles(True)
    print("You found", danilovsky.bleu, "mines")
    print(danilovsky.brie, "of your flags were wrong")

if __name__ == "__main__":
    altaysky()

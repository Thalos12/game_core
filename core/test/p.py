# noinspection PyNoneFunctionAssignment
class Player(object):
    def __init__(self, name):
        stats = self.read_stats(name)

    @staticmethod
    def read_stats(name):
        f = open(name + '.profile', 'r')
        ATK, RES, AGI, INT = f.readlines()  # .strip('\n')
        l = [ATK, RES, AGI, INT]
        for i in range(len(l)):
            l[i] = l[i].strip('\n')
        print l


Player('a')
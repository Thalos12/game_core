import random


# noinspection PyPep8Naming
def create_profile(name):
    print "Generating new stats"
    VIT = random.randint(10, 20)
    STR = random.randint(1, 6)
    RES = random.randint(1, 6)
    AGI = random.randint(1, 6)
    INT = random.randint(1, 6)
    print VIT, STR, RES, AGI, INT


if __name__ == '__main__':
    create_profile('pippo')

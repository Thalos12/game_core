__author__ = 'mazzalex02'
import random


# noinspection PyPep8Naming
def Battle_menu(player1, player2):
    """Only for adventure, not PVP.
    :param player1:
    :param player2:
    """
    if player1.stats['AGI'] > player2.stats['AGI']:
        p1 = player1
        p2 = player2
    elif player1.stats['AGI'] < player2.stats['AGI']:
        p1 = player2
        p2 = player1
    else:
        print 'Same agility, the order of the fight will be randomized.\n'
        i = random.random()
        if i >= 0.5:
            p1 = player1
            p2 = player2
        else:
            p1 = player2
            p2 = player1
    turns = 1
    distance = 50
    while True:
        # print distance
        print "Starting turn {}".format(turns)
        if p1.stats['VIT'] >= 0:
            if not p1.isbot:
                print 'Player {} is attacking.'.format(p1.stats['NAME'])
                p1.Attack(p2, distance)
            else:
                print 'Bot {} is attacking.'.format(p1.stats['NAME'])
                p1.bot_Attack(p2, distance)
        else:
            break
        if p2.stats['VIT'] >= 0:
            if not p2.isbot:
                print 'Player {} is attacking.'.format(p2.stats['NAME'])
                p2.Attack(p1, distance)
            else:
                p2.bot_Attack(p1, distance)
                print 'Bot {} is attacking.'.format(p2.stats['NAME'])
        else:
            break
        distance -= 10
        turns += 1
    print "Finished the fight."
    if p1.stats['VIT'] >=0:
        print '{} won!\n'.format(p1.name)
    else:
        print '{} won!\n'.format(p2.name)

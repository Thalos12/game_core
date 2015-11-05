__author__ = 'mazzalex02'


# noinspection PyPep8Naming
def Battle_menu(player1,player2):
    """Only for adventure, not PVP. """
    if player1.stats['AGI'] > player2.stats['AGI']:
        p1 = player1
        p2 = player2
    elif player1.stats['AGI'] < player2.stats['AGI']:
        p1 = player2
        p2 = player1
    else:
        print 'Same agility, the order of the fight will be randomized.'
        i = random.random()
        if i>=0.5:
            p1 = player1
            p2 = player2
        else:
            p1 = player2
            p2 = player1
    turns = 0
    p1.distance = 50
    p2.distance = 50
    while (p1.stats['VIT']>0 and p2.stats['VIT']>0):
        if p1.isbot == False:
            p1.Attack(p2)
        else:
            p1.bot_Attack(p2)
    del p1.distance
    del p2.distance

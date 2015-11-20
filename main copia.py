import sqlite3 as sql
import sys, os
from core import profile

data = profile.load('p')
print data
con = sql.connect('profiles.db')

with con:
    cur  = con.cursor()
    #cur.execute("DROP TABLE players")
    try:
        cur.execute(("CREATE TABLE players(name TEXT, level INT, exp INT, "
                     "money INT, items BLOB, vit INT, str INT, res INT, agi INT,"
                     "int INT, weapon TEXT, armor TEXT, skill TEXT)"))
    except:
        print "Table exists, coping values."
    names = cur.execute("SELECT name FROM players").fetchall()
    print names
    print data['NAME']
    if '{}'.format(data['NAME']) in names:
        print 'Already in database.'
        sys.exit()
    cur.execute("INSERT INTO players VALUES('{0}',{1},{2},{3},'{4}',{5},{6},{7},{8},{9},'{10}','{11}','{12}')".format(data['NAME'],
                                                                                              data['LEVEL'],
                                                                                              data['EXP'],
                                                                                              data['MONEY'],
                                                                                              str(data['ITEMS']),
                                                                                              data['VIT'],
                                                                                              data['STR'],
                                                                                              data['RES'],
                                                                                              data['AGI'],
                                                                                              data['INT'],
                                                                                              data['WEAPON'],
                                                                                              data['ARMOR'],
                                                                                              data['SKILL']))
    print cur.execute("SELECT * FROM players").fetchall()

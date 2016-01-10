# coding=utf-8
import sys,os
import random
import sqlite3 as sql
import wx
from GUI import gui

root = os.path.dirname(os.path.realpath(__file__))

def create(name,archetype):
    try:
        exec 'from archetypes.{} import *'.format(archetype)
        VIT = random.randint(min_vit, max_vit)
        STR = random.randint(min_str, max_str)
        RES = random.randint(min_res, max_res)
        AGI = random.randint(min_agi, max_agi)
        INT = random.randint(min_int, max_int)
    except:
        gui.notification(None,"Archetype unknown, starting random creation.")
        exec 'from archetypes.random import *'
        VIT = random.randint(min_vit, max_vit)
        STR = random.randint(min_str, max_str)
        RES = random.randint(min_res, max_res)
        AGI = random.randint(min_agi, max_agi)
        INT = random.randint(min_int, max_int)

    stats = {}
    stats['NAME'] = name
    stats['LEVEL'] = 1
    stats['EXP'] = 0
    stats['MONEY'] = 10 # gold? silver? bronze? banana?
    stats['VIT'] = VIT
    stats['STR'] = STR
    stats['RES'] = RES
    stats['AGI'] = AGI
    stats['INT'] = INT
    stats['WEAPON'] = weapon
    stats['ARMOR'] = armor
    stats['SKILL'] = skill

    gui.show_player_info(None,stats)

    con = sql.connect(os.path.join(root,'data','players',name+'.datafile'))
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE info (name TEXT, level INTEGER, exp INTEGER, money INTEGER, "
                    "vit INTEGER, str INTEGER, res INTEGER, agi INTEGER, int INTEGER,"
                    "weapon TEXT, armor TEXT, skill TEXT)")
        cur.execute("INSERT INTO info VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (stats['NAME'],stats['LEVEL'],stats['EXP'],
                                                                         stats['MONEY'],stats['VIT'],stats['STR'],
                                                                         stats['RES'],stats['AGI'],stats['INT'],
                                                                         stats['WEAPON'],stats['ARMOR'],stats['SKILL']))

def save(stats):
    print "SAVING"
    con = sql.connect(os.path.join(root,'data','players',stats['NAME']+'.datafile'))
    with con:
        cur = con.cursor()
        if cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name=? LIMIT 1)", stats['NAME']).fetchone()[0] == 1:
            print "Profile exists."
            cur.execute("UPDATE info SET level=?, exp=?, money=? WHERE name=?", (stats['LEVEL'], stats['EXP'], stats['MONEY'], stats['NAME']))
            print "Profile updated."
        else:
            print "Profile does not exist."
            cur.execute("INSERT INTO info VALUES(?,?,?,?)", (stats['NAME'], stats['LEVEL'], stats['EXP'], stats['MONEY']))
            print 'Profile saved.'
    print '\n',

def load(name):
    try:
        con = sql.connect(os.path.join(root,'data','players',str(name)+'.datafile'))
    except:
        return 'non-existent'
    with con:
        cur = con.cursor()

        if cur.execute(("SELECT name FROM info")).fetchone()[0] != name:
            return 'corrupted'
        stats = {}
        stats['NAME'] = cur.execute("SELECT name FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['LEVEL'] = cur.execute("SELECT level FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['EXP'] = cur.execute("SELECT exp FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['MONEY'] = cur.execute("SELECT money FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['VIT'] = cur.execute("SELECT vit FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['STR'] = cur.execute("SELECT str FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['RES'] = cur.execute("SELECT res FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['AGI'] = cur.execute("SELECT agi FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['INT'] = cur.execute("SELECT int FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['WEAPON'] = cur.execute("SELECT weapon FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['ARMOR'] = cur.execute("SELECT armor FROM info WHERE name=?",(name,)).fetchone()[0]
        stats['SKILL'] = cur.execute("SELECT skill FROM info WHERE name=?",(name,)).fetchone()[0]
        return stats

if __name__ == '__main__':
    stats = {'NAME':'p', 'LEVEL':1, 'EXP':0, 'MONEY':25}
    save(stats)
    load('p')

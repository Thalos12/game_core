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
    s = ("Name: {}\n"
         "Level: {}\n"
         "Exp: {}\n"
         "Money: {}\n"
         "Vitality: {}\n"
         "Strength: {}\n"
         "Resistance: {}\n"
         "Agility: {}\n"
         "Intelligence: {}\n"
         "Weapon: {}\n"
         "Armor: {}\n"
         "Skill: {}").format(name,1,0,10,VIT,STR,RES,AGI,INT,weapon,armor,skill)
    gui.notification(None,s,caption='Your stats')

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
    con = sql.connect(os.path.join(root,'data','players',name+'.datafile'))
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE info (name TEXT, level INTEGER, exp INTEGER, money INTEGER, "
                    "vit INTEGER, str INTEGER, res INTEGER, agi INTEGER, int INTEGER)")
        cur.execute("INSERT INTO info VALUES(?,?,?,?,?,?,?,?,?)", (stats['NAME'],stats['LEVEL'],stats['EXP'],
                                                                    stats['MONEY'],stats['VIT'],stats['STR'],
                                                                    stats['RES'],stats['AGI'],stats['INT']))


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
            print 'Profile inserted.'
    print '\n',

def load(name):
    print "LOADING"
    try:
        con = sql.connect(os.path.join(root,'data','players',str(name)+'.datafile'))
    except:
        return 'non-existent'
    with con:
        cur = con.cursor()
        if cur.execute(("SELECT name FROM info")).fetchone()[0] != name:
            return 'corrupted'
        stats = {'NAME':name}
        stats['LEVEL'] = cur.execute("SELECT level FROM info WHERE name=?",str(name)).fetchone()[0]
        stats['EXP'] = cur.execute("SELECT exp FROM info WHERE name=?",str(name)).fetchone()[0]
        stats['MONEY'] = cur.execute("SELECT money FROM info WHERE name=?",str(name)).fetchone()[0]
        print stats
    print '\n',
    return stats

if __name__ == '__main__':
    stats = {'NAME':'p', 'LEVEL':1, 'EXP':0, 'MONEY':25}
    save(stats)
    load('p')

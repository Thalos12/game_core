import sys,os
import sqlite3 as sql
root = os.path.dirname(os.path.realpath(__file__))

def save(stats):
    print "SAVING"
    con = sql.connect(os.path.join(root,'data','players',stats['NAME']+'.datafile'))
    with con:
        cur = con.cursor()
        if cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name=? LIMIT 1)",stats['NAME']).fetchone()[0] == 1:
            print "Profile exists."
            cur.execute("UPDATE info SET level=?, exp=?, money=? WHERE name=?",(stats['LEVEL'],stats['EXP'],stats['MONEY'],stats['NAME']))
            print "Profile updated."
        else:
            print "Profile does not exist."
            cur.execute("INSERT INTO info VALUES(?,?,?,?)",(stats['NAME'],stats['LEVEL'],stats['EXP'],stats['MONEY']))
            print 'Profile inserted.'
    print '\n',

def load(name):
    print "LOADING"
    con = sql.connect(os.path.join(root,'data','players',str(name)+'.datafile'))
    with con:
        cur = con.cursor()
        if cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name=? LIMIT 1)",str(name)).fetchone()[0] == 1:
            print "Profile exists."
        else:
            print 'Profile does not exist.'
            return None
        stats = {'NAME':name}
        stats['LEVEL'] = cur.execute("SELECT level FROM info WHERE name=?",str(name)).fetchone()[0]
        stats['EXP'] = cur.execute("SELECT exp FROM info WHERE name=?",str(name)).fetchone()[0]
        stats['MONEY'] = cur.execute("SELECT money FROM info WHERE name=?",str(name)).fetchone()[0]
        print 'Profile loaded.'
        print stats
    print '\n',

if __name__ == '__main__':
    stats = {'NAME':'p', 'LEVEL':1, 'EXP':0, 'MONEY':25}
    save(stats)
    load('p')

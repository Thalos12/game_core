import sys,os
import sqlite3 as sql
root = os.path.dirname(os.path.realpath(__file__))

def save(stats):
    con = sql.connect(os.path.join(root,'data','players',stats['NAME']+'.datafile'))

    with con:
        cur = con.cursor()
        if cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name=? LIMIT 1)",stats['NAME']).fetchone()[0] == 1:
            print "Profile exists."
            cur.execute("UPDATE info SET level=?, exp=?, money=? WHERE name=?",(stats['LEVEL'],stats['EXP'],stats['MONEY'],stats['NAME']))
            print "Profile updated."
        else:
            print "Profile doesn't exist."
            cur.execute("INSERT INTO info VALUES(?,?,?,?)",(stats['NAME'],stats['LEVEL'],stats['EXP'],stats['MONEY']))
            print 'Profile inserted.'
if __name__ == '__main__':
    stats = {'NAME':'p',
             'LEVEL':1,
             'EXP':0,
             'MONEY':15}
    save(stats)

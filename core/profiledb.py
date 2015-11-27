import sys,os
import sqlite3 as sql
root = os.path.dirname(os.path.realpath(__file__))

def save():
    con = sql.connect(os.path.join(root,'data','players','p.datafile'))

    with con:
        cur = con.cursor()
        #cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name='{}' LIMIT 1)".format('pippo'))
        #print cur.fetchone()[0]
        #sys.exit()
        if cur.execute("SELECT EXISTS(SELECT 1 FROM info WHERE name='{}' LIMIT 1)".format('pippo')).fetchone()[0] == 1:
            cur.execute("UPDATE info SET level={1}, exp={2}, money={3} WHERE name='{0}'".format('pippo',1,0,15))
            print 'updated'
        else:
            cur.execute("INSERT INTO info VALUES('{}',{},{},{})".format('pippo',1,0,10))
            print 'inserted'
if __name__ == '__main__':
    save()

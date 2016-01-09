import sqlite3 as sql
import wx


# noinspection SqlNoDataSourceInspection
def get_names_list(db = None):
    if db == None:
        db = 'names.db'
    conn = sql.connect(db)

    names_list = []

    with conn:
        cur  = conn.cursor()
        cur.execute('select * from names')
        ls = cur.fetchall()
        for elem in ls:
            names_list.append(str(elem[0]))

    return names_list

def ask_name(parent):
        ask = wx.TextEntryDialog(parent,message='Name check.',caption='Cheking your name.',style=wx.OK,pos=(200,150))
        ask.ShowModal()
        name = ask.GetValue()
        ask.Destroy()
        return name



if __name__ == '__main__':
    db = 'names.db'
    get_names_list(db)
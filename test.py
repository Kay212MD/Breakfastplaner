import sqlite3
conn = sqlite3.connect('Breakfastplan.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM People')
    result = cur.fetchall()

    for i in result:
        #result = cur.fetchall()
        print(result)
        for row in result:
            self.cursor = QTextCursor(self.textEdit.document())
            self.cursor.insertText(row)



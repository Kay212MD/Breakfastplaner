# import sqlite3
# conn = sqlite3.connect('Breakfastplan.db')
#
# with conn:
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM People')
#     result = cur.fetchall()
#
#     for i in result:
#         #result = cur.fetchall()
#         print(result)
#         for row in result:
#             self.cursor = QTextCursor(self.textEdit.document())
#             self.cursor.insertText(row)


my_dict = {1:'A', 2:'B', 3:'C'}
my_list = ['B']

def proof_and_delete_key_by_value(one_dict, one_list):
    sec_dict = {}
    for k, v in one_dict.items():
        for i in one_list:
            if i != v:
                sec_dict[k]=v
    return sec_dict

x = proof_and_delete_key_by_value(my_dict, my_list)
print(x)
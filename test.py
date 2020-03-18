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
c_list = [(1,'A'),(2,'B'),(3,'C')]
my_list = ['B']
p_list = []

def proof_and_delete_key_by_value(one_dict, one_list):
    sec_dict = {}
    for k, v in one_dict.items():
        for i in one_list:
            if i != v:
                sec_dict[k]=v
    return sec_dict

x = proof_and_delete_key_by_value(my_dict, my_list)
print('proof_and_delete_key_by_value: ',x)


def check_list_and_change_list_and_dict(check_list, control_list):
    fill_dict = {}
    if not check_list:
        pass



def slicing_and_storing(check_list, control_list, slice_var, list_pos, dict_var):
    fill_dict = {}
    sliced_list = (control_list[0:slice_var])
    for i in sliced_list:
        fill_dict[i[list_pos]] = dict_var
        check_list.append(i[list_pos])
    return check_list, fill_dict

x1, x2 =slicing_and_storing(p_list, c_list, 1, 1, 5)

print(x1)
print(x2)
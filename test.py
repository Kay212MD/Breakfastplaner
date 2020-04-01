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

def del_double_entries_list(double_list):
    return list(dict.fromkeys(double_list))

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

x = 0
for x in range(5):
    x += 1
print(x)

# check list existing or not

def check_list_existing_and_modify(list_to_check, a_dictionary, dictionary_position, slice_var,
                               list_pos, dict_var):
    if not list_to_check:
        control_list = a_dictionary.get(dictionary_position)
        output_list, output_dict = slicing_and_storing(list_to_check, control_list, slice_var,
                                                       list_pos, dict_var)
        list_to_check = output_list
        a_dictionary.pop(dictionary_position, None)
        return list_to_check, output_dict, a_dictionary
    else:
        target_dict = proof_and_delete_key_by_value(a_dictionary,
                                                    list_to_check)
        control_list = target_dict.get(dictionary_position)
        output_list, output_dict = slicing_and_storing(list_to_check, control_list, slice_var,
                                                       list_pos, dict_var)
        list_to_check.extend(output_list)
        list_to_check = del_double_entries_list(list_to_check)
        a_dictionary.pop(dictionary_position, None)
        return list_to_check, output_dict, a_dictionary


theplan_dict = {}
# foodcoount_dict = {food_id: [(counter, people_id),....}
foodcount_dict = {1: [(0, 2), (0, 3), (25, 1)],
                  2: [(0, 3), (0, 1), (0, 2)],
                  3: [(0, 1), (2, 2), (3,3)],
                  4: [(0, 2), (1, 1), (2, 3)],
                  5: [(0, 2), (0, 3), (2, 1)],
                  6: [(0, 1), (0, 3), (2, 2)]}

# foodquantity and food_id
plan_list = [(10, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

factor = 2
checkin_list = []

step = 1
for plan_tuple in plan_list:
    food_id = plan_tuple[1]
    foodquantity = plan_tuple[0]
    counter_people_list = foodcount_dict.get(food_id)
    print('counter_people_list: ', counter_people_list)
    output_dict = {}
    counter_people_list_sliced = counter_people_list[:1]
    counter_people_tuple = counter_people_list_sliced[0]
    counter = counter_people_tuple[0]
    people_id = counter_people_tuple[1]
    if not checkin_list:
        print(counter_people_tuple)
        print(people_id)
        print("step: ", step)
        output_dict[people_id] = foodquantity
        print('output_dict: ', output_dict)
        checkin_list.append(people_id)
    else:
        print('checkin_list: ', checkin_list)
        print('people_id: ', people_id)
        number_of_people_id = checkin_list.count(people_id)
        print('number_of_people_id: ', number_of_people_id)
        active = True
        while active:
            if number_of_people_id < factor:
                print("if case 1")
                step += 1
                print("step: ", step)
                output_dict[people_id] = foodquantity
                print('output_dict: ', output_dict)
                checkin_list.append(people_id)
                active = False
            else:
                print("else case")
                slice_var = 1
                active = True
                while active:
                    print("while")
                    prev_slice_var = slice_var
                    slice_var += 1
                    counter_people_list_sliced = counter_people_list[prev_slice_var:slice_var]
                    counter_people_tuple = counter_people_list_sliced[0]
                    counter = counter_people_tuple[0]
                    people_id = counter_people_tuple[1]
                    number_of_people_id = checkin_list.count(people_id)
                    print('number_of_people_id: ', number_of_people_id)
                    if number_of_people_id < factor:
                        print("if case 2")
                        step += 1
                        print("step: ", step)
                        output_dict[people_id] = foodquantity
                        print('output_dict: ', output_dict)
                        checkin_list.append(people_id)
                        active = False
                    else:
                        print("else case 2")
                        active =True

    theplan_dict[food_id] = output_dict
    print('theplan_dict: ', theplan_dict)

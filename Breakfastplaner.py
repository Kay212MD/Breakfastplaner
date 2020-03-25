import sqlite3
import math

#Create a command object
conn = sqlite3.connect('Breakfastplan.db')
cur = conn.cursor()

#People
cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY UNIQUE,
            name TEXT UNIQUE)''')
            # id = id of Person, name = name of Person

#Personfoodrelation
cur.execute('''CREATE TABLE IF NOT EXISTS Personfoodrelation (
            people_id INTEGER,
            food_id INTEGER,
            pfq INTEGER,
            counter INTEGER)''')
            # pfq = personalfoodquantity how much the person wants to have for breakfast
            # counter = counts how often a person fetched the food

#Food
cur.execute('''CREATE TABLE IF NOT EXISTS Food
            (id INTEGER PRIMARY KEY UNIQUE,
            foodname TEXT UNIQUE,
            countablefood TINYINT)''')
            #id = id of foodname, foodname = name of the food (e.g. a wafer-thin mint),
            # countablefood => boolean, is food in a special quantity necassary

#Plan
cur.execute('''CREATE TABLE IF NOT EXISTS Plan
            (people_id INTEGER UNIQUE,
            food_id INTEGER UNIQUE,
            foodquantity INTEGER,
            foodreserve INTEGER,
            people_pfq INTEGER)''')
            # foodquantity = sum of the food of a special id,
            # foodreserve = if somebody is very hungry but to shy ;-)

#How_is_in
cur.execute('''CREATE TABLE IF NOT EXISTS How_is_in
            (people_id INTEGER UNIQUE)''')

conn.commit()

# Circle class, proofs inputs of Users, was a little bit late the Idea, but i am a beginner
class Circle:
    def __init__(self, text1, text2, text3, check1, check2):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.check1 = check1
        self.check2 = check2

    def integer_proof(self):
        while True:
            print(self.text1, end='   ')
            number = input()
            try:
                number = int(number)  # proofs Integer
                if number > 0:
                    break
                else:
                    print(number, self.text2)
                    continue
            except:
                print(self.text3)
                continue
            #Circle.integer_proof()
        return number

    def yes_or_no(self):
        while True:
            print(self.text1, end='   ')
            check = input()
            controll1 = self.check1
            controll2 = self.check2
            if check == controll1:
                break
            elif check == controll2:
                break
            else:
                print(self.text2)
                continue
            #Circle.yes_or_no()
        return check

# search, are the list Values in the Dictionary, if they are in, the key value pair will be deleted
# function is for two dimensional Dictionary key:list with tuple {1:[(y,z),...],...}
def proof_and_delete_key_by_value(one_dict, one_list):
    sec_dict = {}
    for k, v in one_dict.items():
        # copy of the list v for update and v doesn't change, isn't the same like transfer_list = v
        # copy is necessary for a clean run through v, if you don't copy, the list will have not the
        # same length anymore and the loop "jump" over the value you want to check,
        # because the value
        # has the position of the removed value and this position has already been checked
        transfer_list = v.copy()
        # the list with the tuples is copied, now we run through v and in the next step through
        # one_list to compare if the Tuple x has on the position 1 the same value as i in
        # one_list if they have the same value we remove the x tuple form the transfer_list
        for x in v:
            for i in one_list:
                if i is x[1]:
                    transfer_list.remove(x)
        # sec_dict is now the new clean dict, the tuples we doesn't need are removed
        sec_dict[k] = transfer_list
    return sec_dict

# take two lists, with variables to fill a check list and a dictionary for later use
# in the control_list are tuples and we pull out a special parameter as the key for the dictionary
def slicing_and_storing(check_list, control_list, slice_var, list_pos, dict_var):
    fill_dict = {}
    sliced_list = (control_list[0:slice_var])
    for i in sliced_list:
        # pull out of the tuple the integer as key for the dictionary
        fill_dict[i[list_pos]] = dict_var
        check_list.append(i[list_pos])
        # convert dict into list, list items are now keys and
        # this will automatically remove duplicates
        check_list = del_double_entries_list(check_list)
        # output the checklist and a dictionary with the correct keys and length
    return check_list, fill_dict

# convert list into dict into list, list items are now keys
# and this will automatically remove duplicates
# and the output is a clean list
def del_double_entries_list(double_list):
    return list(dict.fromkeys(double_list))

# check list if list existing and use pre defined functions for separation
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
        # print('list_to_check ', list_to_check)
        list_to_check = del_double_entries_list(list_to_check)
        # print('list_to_check ', list_to_check)
        a_dictionary.pop(dictionary_position, None)
        # print('a_dictionary ', a_dictionary)
        return list_to_check, output_dict, a_dictionary


# class sort_mechanism:
#     def __init__(self):
#         self.relation = relation #(Person/Food relation)
#         self.dict_proof = dict_proof{} # dict with food_id and counter
#         self.list_sort = list_sort[]


# function only for clarity
# fill the People Table with People and the Personfoodrelation Table
# for connection between People, Food and quantity
def personlist():
    while True:
        # get the status of the Food Table
        cur.execute('SELECT * FROM Food')
        # without [0] or something else, to get the None status
        proof_food_table = cur.fetchone()
        # proof of Food Table, if the Table doesn´t exist you have to create a Table at first
        if proof_food_table == None:
            print("Bitte zuerst Lebensmittelliste anlegen")
            foodlist()
            break
        else:
            # Check if food is wanted
            person = input("Bitte Namen der Person angeben: ")
            # maybe change later code, two person with the same name are really possible
            # maybe update with GUI and SQL Implementation in later Code
            cur.execute('INSERT OR IGNORE INTO People (name) Values (?)', (person,))
            conn.commit()
            cur.execute('SELECT foodname FROM Food')
            foodrows = cur.fetchall()
            # should go through all row
            for row in foodrows:
                food = row[0]
                print(food, end=' ')
                text = Circle(text1="in ihre Auswahl aufnehmen? (j/n): ",
                              text2=0, text3=0, check1='j', check2='n')
                wish = text.yes_or_no()
                # definition what the table have to search
                cur.execute('SELECT id FROM Food WHERE foodname= ?', (food,))
                food_id = cur.fetchone()[0]
                if wish == "j":
                    cur.execute('SELECT countablefood FROM Food WHERE id= ?', (food_id,))
                    control = cur.fetchone()[0]
                    cur.execute('SELECT id FROM People WHERE name = ?', (person,))
                    people_id = cur.fetchone()[0]
                    # activ when food is countable
                    if control == 1:
                        text = Circle(text1="Bitte eine Zahl eingeben:  ",
                                      text2="Die Zahl muß größer Null sein",
                                      text3="Nur Zahlen sind erlaubt", check1=0, check2=0)
                        numberproof = text.integer_proof()
                        cur.execute('INSERT INTO Personfoodrelation '
                                    '(people_id, food_id, pfq, counter) '
                                    'VALUES (?, ?, ?, 0)', (people_id, food_id, numberproof))
                        conn.commit()
                        continue
                    # becomes active when the food is not required in any desired quantity
                    else:
                        cur.execute('INSERT INTO Personfoodrelation '
                                    '(people_id, food_id, pfq, counter) '
                                    'VALUES (?, ?, ?, 0)', (people_id, food_id, 0,))
                        conn.commit()
                        continue
                # becomes active when the food is not desired
                elif wish == "n":
                    continue
            break

# foodlist, what is available for the peoble
def foodlist():
    while True:
        text = Circle(text1="Ist das Lebensmittel in einer bestimmten Menge notwendig? (j/n): ",
                      text2="Falsche Eingabe", text3=0, check1='j', check2='n')
        foodcounter = text.yes_or_no()
        if foodcounter == "j":
            food = input("Bitte Bezeichnung des Lebensmittels angeben: ")
            cur.execute('INSERT OR IGNORE INTO Food (foodname, countablefood) '
                        'VALUES (?, ?)', (food, 1,)) # 1 for true
            conn.commit()
            text = Circle(text1="Wollen Sie weitere Lebenmittel anlegen? (j/n): ",
                          text2="Falsche Eingabe", text3=0, check1='j', check2='n')
            exit = text.yes_or_no()
            if exit == "j":
                continue
            elif exit == "n":
                break
        elif foodcounter == "n":
            food = input("Bitte Bezeichnung des Lebensmittels angeben: ")
            cur.execute('INSERT OR IGNORE INTO Food (foodname, countablefood) '
                        'VALUES (?, ?)', (food, 0,))# 0 for false
            conn.commit()
            text = Circle(text1="Wollen Sie weitere Lebenmittel anlegen? (j/n): ",
                          text2="Falsche Eingabe", text3=0, check1='j', check2='n')
            exit = text.yes_or_no()
            if exit == "j":
                continue
            elif exit == "n":
                break

# is the person available
def personavailable():
    while True:
        cur.execute('SELECT name FROM People')
        namerows = cur.fetchall()
        #print(type(namerows))
        #print(namerows)
        for row in namerows:
            name = row[0]
            print('Person:', name)
            text = Circle(text1="Angabe ob Person anwesend ist (j/n): ", check1='j', check2='n',
                          text2='Falsche Eingabe!', text3=0)
            check = text.yes_or_no()
            if check == "j":
                cur.execute('SELECT id FROM People WHERE name = ?', (name,))
                people_id = cur.fetchone()[0]
                cur.execute('INSERT OR IGNORE INTO How_is_in (people_id) VALUES (?)', (people_id,))
                conn.commit()
            elif check == "n":
                continue
        break

# the Plan of all Plan's
def theplan():
    # Plan for Table
    theplan_dict = {}
    # Selects the available Persons, What food they want, generats plan_dict
    # for food_id and foodquantity relation
    # plan_dict => key = food_id, value = foodqauntity
    plan_dict = {}
    # foodcount_dict => key = food_id, value = people_id:counter
    foodcount_dict = {}
    # checkin_list => for checking who was assign to a food_id
    checkin_list = []
    # how many people are in
    cur.execute('SELECT people_id FROM How_is_in')
    people_rows = cur.fetchall()
    # what food is available
    cur.execute('SELECT id FROM Food')
    food_id_rows = cur.fetchall()
    print('food_id_rows: ', food_id_rows)
    # first Loop for Food necessary, otherwise there is a counting problem with foodquantity
    # first look after the Food, then who want the food, if somebody want the food count, after
    # checking Food and all People reset Quantity for new Food.... and all again
    #print('food_id   people_id   pfq     counter')
    for food_id_row_tuple in food_id_rows:
        # create people_dict for clearance how often a Person had a special Position
        # people_dict => key = people_id, value = counter
        # people_dict have to be in the loop,
        # otherwise people_dict will be overwritten with the last people_dict
        # and not with the people_dict related to the food_id
        people_dict = {}
        foodquantity = 0
        food_id = food_id_row_tuple[0]
        for people_tuple in people_rows:
            people_id = people_tuple[0]
            # print(food_rows)
            cur.execute('SELECT pfq FROM Personfoodrelation WHERE people_id = ? AND food_id = ?',
                        (people_id, food_id,))
            row = cur.fetchone()
            # check is necessary, because of empty lines, first check, after check get the value,
            # None value generates an error when you use pfq = cur.fetchone()[0]
            if row is not None:
                pfq = row[0]
            # print(food_id,'    ',people_id,'    ',pfq)
            cur.execute('SELECT counter FROM Personfoodrelation '
                        'WHERE people_id = ? AND food_id = ?',
                        (people_id, food_id,))
            row = cur.fetchone()
            if row is not None:
                counter = row[0]
            # see print above first for Loop for column
            # print('   ',food_id, '       ', people_id, '      ', pfq, '      ', counter)
            foodquantity = foodquantity + pfq
            plan_dict[food_id] = foodquantity
            people_dict[people_id] = counter
        people_list = [(v, k) for k, v in people_dict.items()]
        people_list.sort()
        foodcount_dict[food_id] = people_list
        # people_div necessary for dividing the countable food and assign them to different people
        people_div = len(people_rows)
        # food_control necessary for comparison between number of people and
        # food and how to distribute them
        food_control = len(plan_dict)
        # Control Structure
    print('plan_dict:', plan_dict)
    print('foodcount_dict:', foodcount_dict)
    print('people_div: ', people_div)
    print('food_control: ', food_control)
# 1. How many countable food is there
    countable_food = 0
    for food_id, countable in plan_dict.items():
        if countable > 0:
            countable_food += 1
    print('countable_food: ', countable_food)
    # transformation of plan_dict for further iteration
    plan_list = [(v, k) for k, v in plan_dict.items()]
    plan_list.sort(reverse=True)

# ToDo 2. Can I spread some food parts over the people
    if people_div > food_control:
        # form relationship between people_div and food_control, all values are round up
        relation_food_people = math.ceil(people_div/food_control)
        print('relation_food_people: ', relation_food_people)
        # can I spread the food and the countable food over more than one Person
        if relation_food_people > countable_food:
            # creates the factor for the division of the countable foods and the number of Persons
            factor = math.ceil(relation_food_people/countable_food)
            # x = max(plan_dict, key=plan_dict.get)
            # print ('MAX', x)
            for plan_tuple in plan_list:
                print('plan_tuple: ', plan_tuple)
                # if the number is higher than zero a division is possible and it is countable food
                if plan_tuple[0] > 0:
                    # if factor * people_div is smaller than the
                    # value of plan_tuple[0] a division is possible
                    if (factor*people_div) < plan_tuple[0]:
                        # separate the food in equal parts
                        food_divided = math.ceil(plan_tuple[0]/factor)
                        # control_list is just what the name says only for control
                        print('food_divided: ', food_divided)
                        # control function necessary for checking the people id, avoid double id's
                        # or just erase the people from foodcount_dict or create a list with id's
                        # it is easy to control and fill and every Startup there is an empty List
# ToDo make a function out of row check list one function, slice list second function
                        checkin_list, output_dict, foodcount_dict = \
                            check_list_existing_and_modify(checkin_list,
                                                           foodcount_dict, plan_tuple[1], factor,
                                                           1, food_divided)
                        print('food_count_dict: ', foodcount_dict)
                        print('checkin_list', checkin_list)
                        print('output_dict ', output_dict)
                        theplan_dict[plan_tuple[1]] = output_dict
# ToDo else need algoirthm to solve the Problem, if factor * people_div is bigger
                    else:
                        # reduce factor by one and proof if a division is possible
                        while True:
                            new_factor = factor -1
                            if (new_factor*people_div) < plan_tuple[0]:
                                checkin_list, output_dict, foodcount_dict = \
                                    check_list_existing_and_modify(checkin_list,
                                                                   foodcount_dict, plan_tuple[1],
                                                                   new_factor,
                                                                   1, food_divided)
                                break
                            elif new_factor <= 1:
                                print('Something is wrong!')
                                break
                            else:
                                continue
                else:
                    control_var = people_div - len(checkin_list)
                    if control_var > factor:
                        checkin_list, output_dict, foodcount_dict = \
                            check_list_existing_and_modify(checkin_list,
                                                           foodcount_dict, plan_tuple[1], factor,
                                                           1, 0)
                        theplan_dict[plan_tuple[1]] = output_dict
                    else:
                        checkin_list, output_dict, foodcount_dict = \
                            check_list_existing_and_modify(checkin_list,
                                                           foodcount_dict, plan_tuple[1], factor,
                                                           1, 0)
                        theplan_dict[plan_tuple[1]] = output_dict
        theplan_dict_backup = theplan_dict.copy()
        print('theplan_dict: ', theplan_dict)
        print('new foodcount_dict:', foodcount_dict)
# ToDo 3. Have to Check that in the case food_control is not bigger than people_div, nobody have
    #  ToDo more than one food_id
    else:
        # check how big the difference between people an food is
        food_people_diff = food_control - people_div
        # creates the factor for the division of the countable foods and the number of Persons
        if food_people_diff == 0:
            # everybody gets one food_id, it is not necessary for checking and slicing the
            # countable food
            checkin_list, output_dict, foodcount_dict = \
                check_list_existing_and_modify(checkin_list,
                                               foodcount_dict, plan_tuple[1], 1,
                                               1, 1)
            theplan_dict[plan_tuple[1]] = output_dict
        else:
            # know is something intelligent necessary, what depends on the difference between
            # people and food
            factor = math.ceil(relation_food_people / countable_food)
            for plan_tuple in plan_list:
                if plan_tuple[0] > 0:
                    if (factor*people_div) < plan_tuple[0]:

                        print(factor)
        pass

def main():
    #Testbody! GUI needed or/and Webapp
    while True:
        selection = input("Neuer Plan (X) oder Neue Person/Lebensmittel (Y):  ")
        if selection == "Y":
            selection = input("Möchten Sie eine Person oder ein Lebensmittel anlegen? "
                              "(Person (P)/Lebensmittel (L) /nein (n)): ")
            if selection == "P":
                # Anlegen der Person
                personlist()
            elif selection == "L":
                # Anlegen der Lebensmittel
                foodlist()
            elif selction == "n":
                print("Vielen Dank")
                break
            else:
                print("Falsche Eingabe")
                continue
        elif selection == "X":
            selection = input("Personenliste anlegen? (j/n): ")
            if selection == "j":
                # available Personlist
                personavailable()
            elif selection == "n":
                text = Circle(text1="Soll der Plan befüllt werden? (j/n): ",
                              text2="Falsche Eingabe", text3=0, check1='j', check2='n')
                selection = text.yes_or_no()
                if selection == "j":
                    theplan()

                else:
                    continue
                print("Vielen Dank")
                break
            else:
                print("Falsche Eingabe")
                continue
        else:
            print("Falsche Eingabe")

if __name__ == '__main__':
    main()
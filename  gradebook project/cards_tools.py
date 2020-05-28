import cards_input
import csv
from pathlib import Path



card_list = []
p_save = Path('gradebook.save')
p_csv = Path('gradebook.csv')
card_list = [['id', 'firstname', 'lastname','email','phone','city','score','department']]

def read_info():
    old_info = []
    try:
        students_csv = open("gradebook.csv")
    except:
        print("can not find")
        return
    while True:
        info = students_csv.readline()
        if not info:
            break
        # print(info)
        info = info.rstrip()
        # print(info)
        info = info[1:-1]
        # print(info)
        student_dict = {}
        for x in info.split(","):
            # print(x)
            key_value = []
            for k in x.split(":"):
                k = k.strip()
                # print(k)
                if k[0] == k[-1] and len(k) > 2:
                    key_value.append(k[1:-1])
                else:
                    key_value.append(int(k))
                # print(key_value)
            student_dict[key_value[0]] = key_value[1]
        # print(student_dict)
        old_info.append(student_dict)
    students_csv.close()
    return old_info

def save_info(card_list):
    try:
        students_csv = open("gradebook.csv", "w")
    except Exception as e:
        students_csv = open("gradebook.csv", "x")
    for info in card_list:
        students_csv.write(str(info) + "\n")
    students_csv.close()


def show_menu():

    """Menu
    """
    print("*" * 50)
    print("welcome student gradebook")
    print("1. add new")
    print("2. show all")
    print("3. search student")
    print("4. save gradebook in to csv")
    print("5. action：1: revise / 2: delete / 0: back to menu")
    print("6. open gradebook")
    print("0. exit system")
    print("*" * 50)


def new_card():

    """add new information
    """
    print("-" * 50)
    print("function：add student")

    id = input("input id：")
    firstname = input("input first name：")
    while True:
        if (u'\u4e00' <= firstname <= u'\u9fff'):
            break
        if firstname.isalpha():
            break
        else:
            firstname = input("please input correct first name：")

    lastname = input("input last name：")
    while True:
        if (u'\u4e00' <= lastname <= u'\u9fff'):
            break
        if lastname.isalpha():
            break
        else:
            lastname = input("please input correct last name：")

    score = input("input score：")
    while True:
        if score.isdigit():
            break
        else:
            score = input("please input（1-99）：")

    department = input("input department：")
    while True:
        if (u'\u4e00' <= department <= u'\u9fff'):
            break
        if department.isalpha():
            break
        else:
            department = input("please input correct department name：")

    phone = input("input phone number：")
    city = input("input city name：")

    email = input("input email address：")


    # 2. save student info into dict
    card_dict = {"id":id,
                 "firstname": firstname,
                 "lastname": lastname,
                 "email": email,
                 "phone":phone,
                 "city":city,
                 "score":score,
                 "department": department}

    # 3. add user dict to list
    card_list.append(card_dict)

    # print(card_list)

    # 4.add successfully
    print("add %s info successfully" % card_dict["firstname"])


def show_all():

    """show all
    """
    print("-" * 50)
    print("function：show all")

    # 1. exist record or not
    if len(card_list) == 0:
        print("hint: can't find records")

        return

    # 2. show all
    print("id\\firstname\t\tlastname\t\temail\t\tphone\t\tcity\t\tscore\t\tdepartment")
    print("-" * 60)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["id"],
            card_dict["firstname"],
            card_dict["lastname"],
            card_dict["email"],
            card_dict["phone"],
            card_dict["city"],
            card_dict["score"],
            card_dict["department"]))

    print("-" * 60)


def binarysearch(arr, n):
    left, right = 0, len(arr) - 1

    while (left < right):
        mid = (left + right) // 2
        if arr[mid]["id"] == n:
            return arr[mid]
        elif arr[mid]["id"] < n:
            left = mid + 1
        else:
            right = mid - 1

    # if target is not in the array
    if arr[left]["id"] > n:
        return False
    if arr[right]["id"] < n:
        return False

    return arr[left]


    print("-" * 50)
    print("function：search student information")


def deal_card(find_dict):




    action_str = input("action：1: revise/ 2: delete/ 0: back to menu")

    if action_str == "1":

        find_dict["id"] = cards_input.input_card_info(find_dict["id"],
                                                        "input id[or tap return]：")
        find_dict["firstname"] = cards_input.input_card_info(find_dict["firstname"],
                                                        "input first name[or tap return]：")
        find_dict["lastname"] = cards_input.input_card_info(find_dict["lastname"],
                                                        "input last name[or tap return]：")
        find_dict["email"] = cards_input.input_card_info(find_dict["email"],
                                                        "input email[or tap return]：")
        find_dict["phone"] = cards_input.input_card_info(find_dict["phone"],
                                                         "请输入电话[回车不修改]：")
        find_dict["city"] = cards_input.input_card_info(find_dict["city"],
                                                          "input city[or tap return]：")
        find_dict["department"] = cards_input.input_card_info(find_dict["department"],
                                                         "input department[or tap return]：")

        print("%s information revised successfully！" % find_dict["name"])
    elif action_str == "2":

        card_list.remove(find_dict)

        print("deleted！")

import cards_tools
while True:

    cards_tools.show_menu()

    action = input("please select function：")

    print("you select：%s" % action)


    if action in ["1", "2", "3","4","5","6"]:

        if action == "1":
            cards_tools.new_card()

        elif action == "2":
            cards_tools.show_all()

        elif action == "3":
            ret = cards_tools.binarysearch(card_list,input("search id："))
            print(ret)









        elif action == "4":
            cards_tools.save_info(card_list)


        elif action=="5":
            cards_tools.deal_card()

        elif action=="6":
            student_info = read_info()









        elif action == "0":
             print("wwelcome again")



    else:
            print("error，try again：")


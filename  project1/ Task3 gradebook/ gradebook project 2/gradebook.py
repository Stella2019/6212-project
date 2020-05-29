# gradebook.py
# Gradebook System
# ＋－－－－－－－－－－－－－－－－－－－－－－＋
# ｜　１）Add student information　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　２）Show all information　　　　　　　　　　　　　　　　　｜
# ｜　３）Delete student information　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　４）Revise student information　
# |   5　　　　　　　　　　　　　　　　　　　　　｜
# ｜　５）Display student information by SCORE high-low　　　　　　　　　｜
# ｜　６）Display student information by SCORE low-high　　　　　　　　｜
# ｜　７）Display student information by ID high-low　　　　　　　　　　｜
# ｜　８）Display student information by ID low-high　　　　　　　　　｜
# ｜  ９）Save gradebook.csv      ｜
# ｜ 1０）Read gradebook.csv     ｜
# ｜ exit：＜return＞                 ｜
# ＋－－－－－－－－－－－－－－－－－－－－－－＋               　　　　　　　　　｜


def meun():
    menu_info = ''' ＋－－－－－－－－－－－－－－－－－－－－－－＋
# ｜　１）Add student information(type return in id to get back to menu)　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　２）Show all information　　　　　　　　　　　　　　　　　｜
# ｜　３）Delete student information　　　　　　　　　　　　　　　　　　　　　　｜
# ｜　４）Revise student information　
# |   5) Binary-Search  by id　　　　　　　　　　　　　　　　　　　　　｜
# ｜　 6）Display student information by SCORE high-low　　　　　　　　　｜
# ｜　7）Display student information by SCORE low-high　　　　　　　　｜
# ｜　8）Display student information by ID high-low　　　　　　　　　　｜
# ｜　9）Display student information by ID low-high　　　　　　　　　｜
# ｜  10）Save gradebook.csv      ｜
# ｜  11）Read gradebook.csv     ｜
# ｜ exit：＜return＞                 ｜
# ＋－－－－－－－－－－－－－－－－－－－－－－＋               　　　　　　　　　｜
'''
    print(menu_info)


# sorted by key
def get_id(*l):
    for x in l:
        return x.get("id")


def get_score(*l):
    for x in l:
        return x.get("score")


# １） add
def add_student_info():
    L = []
    while True:
        f = input("input firstname：")
        if not f:  # null
            break
        try:
            ID = input("input id：")
            l = input("input lastname：")

            e = input("input email：")
            p = input("input phone：")
            c = input("input city：")
            d = input("input department：")
            s = input("input score：")
        except:
            print("invlid, please try again")
            continue
        info = {"id": ID, "firstname": f, "lastname": l, "email": e, "phone": p, "city": c, "department": d, "score": s}
        L.append(info)
    print("completed！！！")
    return L


# ２）
def show_student_info(student_info):
    if not student_info:
        print("no info．．．．．")
        return
    print("id", "first name".center(8), "last name".center(4), "email".center(12), "phone".center(12),"city".center(12),"department".center(12), "score")
    for info in student_info:
        print(info.get("id"), str(info.get("first name")).center(8), str(info.get("lastname")).center(4),str(info.get("email")).center(12),info.get("phone").center(12),str(info.get("city")).center(12),str(info.get("department")).center(12), info.get("score"))


# ３）
def del_student_info(student_info, del_name=''):
    if not del_name:
        del_name = input("input first name：")
    for info in student_info:
        if del_name == info.get("firstname"):
            return info
    raise IndexError("can not find %s" % del_name)


# ４）
def mod_student_info(student_info):
    mod_name = input("input first name：")
    for info in student_info:
        if mod_name == info.get("firstname"):
            s = int(input("input score："))

            info = {"firstname": mod_name, "score": s}
            return info
    raise IndexError("学生信息不匹配,没有找到%s" % mod_name)


# ５）
def binarysearch(student_info, n):
    left, right = 0, len(student_info) - 1

    while (left < right):
        mid = (left + right) // 2
        if student_info[mid]["id"] == n:
            return student_info[mid]
        elif student_info[mid]["id"] < n:
            left = mid + 1
        else:
            right = mid - 1

    # if target is not in the array
    if student_info[left]["id"] > n:
        return False
    if student_info[right]["id"] < n:
        return False

    return student_info[left]


    print("-" * 50)
    print("function：search student information")
# 6)
def score_reduce(student_info):
    print("score high-low")
    mit = sorted(student_info, key=get_score, reverse=True)
    show_student_info(mit)


# 7）
def score_rise(student_info):
    print("score low-high")
    mit = sorted(student_info, key=get_score)
    show_student_info(mit)


# 8）
def id_reduce(student_info):
    print("id high-low：")
    mit = sorted(student_info, key=get_id, reverse=True)
    show_student_info(mit)


# 9）
def id_rise(student_info):
    print("id low-high：")
    mit = sorted(student_info, key=get_id)
    show_student_info(mit)


# 10）
def save_info(student_info):
    try:
        students_csv = open("gradebook.csv", "w")  
    except Exception as e:
        students_csv = open("gradebook.csv", "x")  
    for info in student_info:
        students_csv.write(str(info) + "\n")  
    students_csv.close()


# １1）
def read_info():
    old_info = []
    try:
        students_csv = open("gradebook.csv")
    except:
        print("no such file")
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
                    key_value.append(str(k))
                # print(key_value)
            student_dict[key_value[0]] = key_value[1]
        # print(student_dict)
        old_info.append(student_dict)
    students_csv.close()
    return old_info


def main():
    student_info = []
    while True:
        # print(student_info)
        meun()
        number = input("choose：")
        if number == '1':
            student_info = add_student_info()
        elif number == '2':
            show_student_info(student_info)
        elif number == '3':
            try:
                student_info.remove(del_student_info(student_info))
            except Exception as e:
                # do not match
                print(e)
        elif number == '4':
            try:
                student = mod_student_info(student_info)
            except Exception as e:

                print(e)
            else:

                student_info.remove(del_student_info(student_info, del_name=student.get("firtname")))
                student_info.append(student)
        elif number =='5':

            ret = binarysearch(student_info, input("search id："))
            print(ret)


        elif number == '6':
            score_reduce(student_info)
        elif number == '7':
            score_rise(student_info)
        elif number == '8':
            id_reduce(student_info)
        elif number == '9':
            id_rise(student_info)
        elif number == '10':
            save_info(student_info)
        elif number == '11':
            student_info = read_info()
        else:
            break
        input("return to menu")


main()


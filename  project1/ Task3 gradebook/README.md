# 6212-project
course project
Open gradebook project1 or 2 in Pycharm.
python 3.7

1. Grade book project 1:
First, run cards_input.py then
run cards_tools.py, it has the following functions:
1. add new
**************************************************
function：add student
input id：1
input first name：Ann
input last name：P
input score：78
input department：math
input phone number：87654
input city name：arlington
input email address：secfvgbh@rgh
add Ann info successfully
**************************************************

2. show all
3. search student
**************************************************
please select function：3
you select：3
search id：2
{'id': '2', 'firstname': 'yg', 'lastname': 'y', 'email': '7yg', 'phone': '765', 'city': 'hb', 'score': '65', 'department': 'ygv'}
**************************************************
4. save gradebook in to csv
5. action：1: revise / 2: delete / 0: back to menu
0. exit system






2.Gradebook project 2
＋－－－－－－－－－－－－－－－－－－－－－－＋
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
# ＋－－－－－－－－－－－－－－－－－－－－－－＋         

choose：1
input firstname：ij
input id：91
input lastname：jm
input email：ik098
input phone：89
input city：ik
input department：ik
input score：69
input firstname：
completed！！！
return to menu

choose：2
id first name last name    email        phone         city      department  score
54   None    rf      54es                                            78
76   None    yg      76yg                                            76
67   None    yg       yg                                             89
return to menu
 
choose：5
search id：54
{'id': '54', 'firstname': 'yg', 'lastname': 'rf', 'email': '54es', 'phone': '', 'city': '', 'department': '', 'score': '78'}
return to menu

search id：5
False

choose：6 score high-low
id first name last name    email        phone         city      department  score
67   None    yg       yg                                             89
54   None    rf      54es                                            78
76   None    yg      76yg                                            76

choose：8
id high-low：
id first name last name    email        phone         city      department  score
76   None    yg      76yg                                            76
67   None    yg       yg                                             89
54   None    rf      54es                                            78
return to menu


choose：11 --- open gradebook.csv
search id：76
{'id': '76', 'firstname': 'uhb', 'lastname': 'yg', 'email': '76yg', 'phone': "''", 'city': "''", 'department': "''", 'score': '76'}
return to menu










import random

list_obj = [random.randrange(0, 99) for i in range(8)]
# print("Given array: ", list_obj, "\n")


res_list = random.choices([[1, 26], [0, 2], [56, 98], [2, 6]])  # [[1,26]]
res_element = random.choice([[1, 26], [0, 2], [56, 98], [2, 6]])  # [1,26]
# print(res_element)
# a = random.sample(list_obj, 2)

import string

a = string.ascii_uppercase
# print(a)

import collections

list_ob = collections.deque(list_obj, 3)  # as a stack or Queue
list_ob = collections.UserDict({"name": "ram", "age": 34})
# UserDict has data attribute but normal dict does not have UserDict
b = list_ob.data
# print(b)

################################## calender and datetime
import calendar

# print(calendar.isleap(1996))
# print(calendar.weekday(2022, 7, 22))  # 0 is for sunday

# print(calendar.weekheader(8))

# for i in calendar.day_abbr:
#     print(i)

# print(calendar.month(2022, 7))
# print(calendar.SUNDAY)

import datetime

a = datetime.date.month
# print(a)
from time import gmtime, strftime, strptime

a = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
b = strptime("30 Nov 00", "%d %b %y")

import os

# print(os.getlogin())

############################## FILE READ AND WRITE
# f = open("use_of_module.py", "r")
# # print(f.read(5)) # read char
# print(f.readline(10))  # read char
# ########to remove file or directory
# f.close()  # call always after desired task is done

############################remove file and directory use os module
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

############################## Regex module
import re

txt = "+919928913009 in @ramesh @is c.do aviavig.com i.c http://cl.vom/b/"
# x = re.findall("Spai.*n", txt)
# y = re.findall("Spai.+n", txt)

# regex_re = "\+?\d{2}[\ -]?\d{10}" # Mobile phone extractor
# regex_re = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"  #Email Extraxtor
regex_re = "@[a-z0-9_-]{1,15}"  # Username extractor
# regex_re = "[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}"  # domain extractor
# regex_re = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"  # link extractor

regex = re.compile(regex_re)
z = re.findall(regex_re, txt)
print(z)

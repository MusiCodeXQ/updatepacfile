import sys


def set_pac_location(path):
    o = open("paclocation.loc", "w+")
    o.writelines(path)
    pass


def add_rule(url):
    file = open(get_pac_location(), encoding="utf-8")
    index = 0
    lines = file.readlines()
    for line in lines:
        if str(line).startswith(str(pic_rul(url))):
            print(url + " has been in file")
            return
    for line in lines:
        index += 1
        if str(line).startswith("var rules"):
            lines.insert(index, pic_rul(url) + "\n")
    file = open(get_pac_location(), "w+", encoding="utf-8")
    for line in lines:
        file.writelines(line)
    pass


def delete_rule(url):
    file = open(get_pac_location(), encoding="utf-8")
    index = 0
    lines = file.readlines()
    for line in lines:
        if str(line).startswith(str(pic_rul(url))):
            lines.remove(line)
            print("delete success")
            index += 1
    if index == 0: print("do not have " + url)
    file = open(get_pac_location(), "w+", encoding="utf-8")
    for line in lines:
        file.writelines(line)
    pass


def pic_rul(url):
    head = """  "||"""
    end = """","""
    return head + url + end


help_str = """setloc(s) : 设置pac文件位置
addurl(a) : 添加url至pac文件
delurl(d) : 删除pac文件中的url
getloc(g) : pac文件位置
"""


def pac_help():
    print(help_str)
    pass


def get_pac_location():
    o = open("paclocation.loc")
    return o.readline()
    pass


if __name__ == '__main__':
    while (True):
        code = input("输入指令:\n")
        codes = code.split(' ')
        if len(codes) < 2:
            pac_help()
            continue
        if codes[0] == "setloc":
            set_pac_location(codes[1])
        elif codes[0] == "addurl":
            add_rule(codes[1])
        elif codes[0] == "delurl":
            delete_rule(codes[1])
        elif codes[0] == "getloc":
            print(get_pac_location())
        elif codes[0] == "s":
            set_pac_location(codes[1])
        elif codes[0] == "a":
            add_rule(codes[1])
        elif codes[0] == "d":
            delete_rule(codes[1])
        elif codes[0] == "g":
            print(get_pac_location())
        else:
            pac_help()

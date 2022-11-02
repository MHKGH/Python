user_dic = {}


def add(item, quantity):
    if item in user_dic:
        user_dic[item] += quantity
    else :
        user_dic[item] = quantity
    print(user_dic)

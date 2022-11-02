from add import user_dic

def delete(item, quantity):
    if item in user_dic:
        user_dic[item] -= quantity
    print(user_dic)

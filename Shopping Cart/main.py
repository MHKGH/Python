from a import Item
from add import user_dic
from list_of_items import ItemList
from data import shopping_cart
from price import price, price_bank

start = ItemList()

start.list_display()

for only_item in user_dic:
    item_in_user_dic = only_item
    total_item_count = user_dic[only_item]
    print(only_item)
    for i in shopping_cart:
        if i['item'] == item_in_user_dic:
            item_price = i['price']

    price(total_item_count, item_price)

final_dict = {}
for i in user_dic:
    final_dict[i] = None
count = 0
for x in final_dict.keys():
    final_dict[x] = price_bank[count]
    count += 1
print(final_dict)













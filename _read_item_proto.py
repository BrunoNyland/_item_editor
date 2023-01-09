import os
from _item import ItemProto, Item

locale_path = '.'

item_proto_path = os.path.join(locale_path, 'item_proto.txt')
item_list_path = os.path.join(locale_path, 'item_list.txt')
item_list_path = os.path.join(locale_path, 'item_desc.txt')

itens = {}

f = open(item_proto_path, 'r')
item_proto_lines = f.readlines()
f.close()

item_proto = ItemProto()

for lin in item_proto_lines:
    collums = lin.split('\t')
    item = Item()
    item.Vnum = collums[0]
    item_proto.append(item)

for item in item_proto:
    print(item.Vnum)
        

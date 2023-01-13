import time
import os
import item_define as item

locale_path = '.'

item_proto_path = os.path.join(locale_path, 'item_proto.txt')
item_list_path = os.path.join(locale_path, 'item_list.txt')
item_list_path = os.path.join(locale_path, 'item_desc.txt')

itens = {}

f = open(item_proto_path, 'r')
item_proto_lines = f.readlines()
f.close()

item_proto = item.ItemProto()

for lin in item_proto_lines:
    time.sleep(1)
    collums = lin.split('\t')

    if not collums[0].isnumeric():
        continue

    if len(collums) != 32:
        continue

    i = item.Item()
    i.read(collums)
    item_proto.append(i)

    print(i.Vnum, i.Name, i.Type, i.SubType)
        

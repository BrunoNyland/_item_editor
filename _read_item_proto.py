import os

locale_path = '.'

item_proto_path = os.path.join(locale_path, 'item_proto.txt')
item_list_path = os.path.join(locale_path, 'item_list.txt')
item_list_path = os.path.join(locale_path, 'item_desc.txt')

itens = {}

item_proto = open(item_proto_path, 'r').readlines()
for lin in item_proto:
    col = lin.split('\t')

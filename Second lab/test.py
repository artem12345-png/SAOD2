import json
from treelib import Node, Tree


def creater(nametree: str) -> dict:
    root = {
        f'{nametree}': [{}]
    }
    return root


root = creater("root")


def insert(key: str, value: any, list_node: list) -> None:
    # d = {
    #     f"{latter}": [{}]
    # }
    if len(key) == 1:
        list_node[0][f'{key[0]}'] = [{}, None]
        list_node[0][key[0]][1] = value
        return

    if new_list_node := list_node[0].get(key[0]):
        insert(key[1:], value, new_list_node)
    else:
        list_node[0][f'{key[0]}'] = [{}, None]
        insert(key[1:], value, list_node[0].get(key[0]))


def delete(key: str, list_node: list) -> None:
    if len(key) == 1:
        if not list_node[0].get(key)[0].keys():
            list_node[0].pop(key[0])
    if new_list_node := list_node[0].get(key[0]):
        delete(key[1:], new_list_node)
        if not list_node[0].get(key[0])[0].keys():
            list_node[0].pop(key[0])


def lookup(key: str, list_node: list) -> any:

    if len(key) == 1:
        return list_node[0].get(key)[1]

    if new_list_node := list_node[0].get(key[0]):
        return lookup(key[1:], new_list_node)


def saver():
    with open('Tree.json', 'w') as f:
        json.dump(root.get('root'), f, ensure_ascii=False, indent=' ', separators=("", ""))



tree = Tree()
tree.create_node('root', 'root')


def show(list_node: list, tree: Tree, parent: str) -> None:
    pass


# {'root': [{'a': [{'r': [{'t': [{'e': [{'m': [{}, 15]}, None], 'y': [{'o': [{'m': [{'f': [{'g': [{}, 13232355]},




insert('artyomfghgfhgfhg', 1423435, root.get('root'))
get_edges(root)
insert('artgfhgfyom', 14, root.get('root'))
insert('artyomfghgfh', 13232355, root.get('root'))
insert('artfghgfyom', 23455, root.get('root'))

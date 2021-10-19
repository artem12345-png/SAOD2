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
        return {f'{key}': list_node[0].get(key)[1]}

    if new_list_node := list_node[0].get(key[0]):
        return lookup(key[1:], new_list_node)


insert('artem', 15, root.get('root'))
insert('artyom', 15, root.get('root'))
print(root)
delete('artem', root.get('root'))
print(root)
print(lookup('artem', root.get('root')))

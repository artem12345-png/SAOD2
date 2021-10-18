tree = list()


def get_dict(*kwards, parent, uncle, child_1, child_2, value, color, lvl, root=False) -> dict:
    dict = {
        'parent': parent,
        'uncle': uncle,
        'child_1': child_1,
        'child_2': child_2,
        'value': value,
        'color': f'{color}',
        'lvl': lvl,
        'root': root
    }
    return dict


def RBtree_add(node: int) -> list:
    if tree:
        root = findRoot()
        value_pr, which_child = recursionSearch(node=node, root=root)
        for item in tree:
            if item.get("value") == value_pr:
                if which_child:
                    item['child_2'] = node
                else:
                    item['child_1'] = node
        tree.append(
            get_dict(parent=value_pr, uncle=None, child_1=None, child_2=None, value=node, color='B', lvl=0))
    else:
        tree.append(
            get_dict(parent=None, uncle=None, child_1=None, child_2=None, value=node, color='B', lvl=0, root=True))

    return tree


def findRoot() -> int:
    for item in tree:
        if item.get('root'):
            return item.get('value')


def recursionSearch(node: int, root=None):  # функция для нахождения value родителя
    which_child = -1
    if node >= root:
        for item in tree:
            if item.get('value') == root:
                if item.get('child_2'):
                    value_pr, which_child = recursionSearch(node=node, root=item.get('child_2'))
                else:
                    return root, 1
    else:
        for item in tree:
            if item.get('value') == root:
                if item.get('child_2'):
                    value_pr, which_child = recursionSearch(node=node, root=item.get('child_1'))
                else:
                    return root, 0

    return value_pr, which_child


RBtree_add(3)
RBtree_add(213)
RBtree_add(34)
# RBtree_add(111)
# RBtree_add(333)
# RBtree_add(34435)
# RBtree_add(88576)
print(RBtree_add(5))

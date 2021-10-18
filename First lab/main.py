RED = 'RED'
BLACK = 'BLACK'


class RBNode:
    def __init__(self, key=None, parent=None, color=RED):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

    def paint(self, color):
        self.color = color

    def isLeftChild(self):
        # Имеет родительский узел и является левым потомком
        return self.parent and self is self.parent.left

    def isRightChild(self):
        # Имеет родительский узел и является правильным потомком
        return self.parent and self is self.parent.right

    def sibling(self):
        if self.isLeftChild():  # Если это левый дочерний элемент, вернуться к правому дочернему элементу родительского узла
            return self.parent.right
        if self.isRightChild():  # Если это правый дочерний элемент, вернуться к левому дочернему элементу родительского узла
            return self.parent.left
        return None  # Ни левый, ни правый дочерние элементы, что указывает на отсутствие дочернего узла

    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()


class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def isRed(self, node) -> bool:
        # Текущий узел существует и красный
        return node and node.color == RED

    def isBlack(self, node) -> bool:
        # Текущий узел не существует (внешний узел по умолчанию черный) или цвет черный
        return node is None or node.color == BLACK

    def predecessor(self, node):
        if node is None:
            return None
        if node.left:  # Самый большой узел левого поддерева - предшественник
            p = node.left
            while p.right:
                p = p.right
            return p
        # Нет левого поддерева, просто посмотрите вверх, если это правое поддерево родительского, то родительский является предшественником
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def successor(self, node):
        if node:
            pass
        else:
            return None
        if node.right:  # Наименьший узел правого поддерева является преемником
            s = node.right
            while s.left:
                s = s.left
            return s
        # Правого поддерева нет, просто посмотрите вверх, если это левое поддерево родительского, то родительский является преемником
        while node.parent and node is node.parent.right:
            node = node.parent
        return node.parent

    def insert(self, key):  # вставляем элементы в дерево
        if self.root is None:
            self.root = RBNode(key)
            self.size += 1
            self._insert(self.root)
            return
        # Найдите родительский узел
        parent = self.root
        node = self.root
        flag = 0
        while node:
            parent = node
            if key > node.key:
                node = node.right
                flag = 0
            elif key < node.key:
                node = node.left
                flag = 1
            else:
                node.key = key
                return

        new = RBNode(key=key, parent=parent)
        if flag == 0:  # Наконец вставлен справа
            parent.right = new
        else:  # Наконец вставлен слева
            parent.left = new
        self.size += 1
        self._insert(new)

    def _insert(self, node):
        parent = node.parent
        # Добавить корневой узел или переполнить корневой узел
        if parent is None:
            node.paint(BLACK)
            return
        # Родительский узел ЧЕРНЫЙ, вставить напрямую без обработки
        if self.isBlack(parent):
            return
        # Ниже приведен случай, когда родитель КРАСНЫЙ
        grand = parent.parent
        grand.paint(RED)  # Независимо от цвета дяди, гранд всегда будет окрашен в КРАСНЫЙ цвет
        uncle = parent.sibling()
        # Переполнение узла
        if self.isRed(uncle):  # дядя КРАСНЫЙ
            parent.paint(BLACK)
            uncle.paint(BLACK)
            self._insert(grand)  # Узел переполняется, гранд следует рассматривать как вновь вставленный узел
            return
        if parent.isLeftChild():
            if node.isLeftChild():  # Корпус  LL, правая рука
                parent.paint(BLACK)
            else:  # В случае LR сначала поверните родительский элемент влево, а затем поверните гранд вправо
                node.paint(BLACK)
                self.LeftRotate(parent)
            self.RightRotate(grand)
        else:  # дядя   ЧЕРНЫЙ
            if node.isLeftChild():  # В случае RL сначала поверните родительский элемент вправо, а затем поверните гранд влево
                node.paint(BLACK)
                self.RightRotate(parent)
            else:  # RR корпус, левша
                parent.paint(BLACK)
            self.LeftRotate(grand)

    def _search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._search(subtree.left, key)
        elif key > subtree.key:
            return self._search(subtree.right, key)
        else:
            return subtree

    def remove(self, key):
        # Фактически удаленный узел - это конечный узел (то есть последний уровень B-дерева)
        node = self._search(self.root, key)
        if node is None:
            return
        self.size -= 1
        if node.left and node.right:  # Узел со степенью 2, найти его преемника покрытия
            s = self.successor(node)
            node.key = s.key
            node = s
        # Элемент, используемый для замены
        replacement = node.left if node.left else node.right
        if replacement:  # узел - это узел степени 1
            replacement.parent = node.parent
            if node.parent is None:  # узел - это корневой узел
                self.root = replacement
            elif node.parent.left is node:  # узел - левое поддерево родительского узла
                node.parent.left = replacement
            else:  # узел - это правое поддерево родительского узла
                node.parent.right = replacement
            self._remove(replacement)
            node.left = node.right = node.parent = None
        elif node.parent is None:  # узел - это корневой узел
            self.root = None
            self._remove(node)
        else:  # узел является листовым узлом
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self._remove(node)
            node.parent = None

    def _remove(self, node):
        if self.isRed(node):  # Если заменяемый узел КРАСНЫЙ, покрасьте его прямо в ЧЕРНЫЙ
            node.paint(BLACK)
            return
        parent = node.parent
        if parent is None:
            return
        # Ниже приведен случай, когда альтернативный узел ЧЕРНЫЙ
        left = node.isLeftChild() or parent.left is None
        sibling = parent.right if left else parent.left
        if left:  # Родственный узел справа
            if self.isRed(sibling):  # брат - это КРАСНЫЙ
                sibling.paint(BLACK)
                parent.paint(RED)
                self.LeftRotate(parent)
                sibling = parent.right  # брат изменился после поворота и должен быть перенаправлен
            if self.isBlack(sibling.left) and self.isBlack(sibling.right):
                # Если у родственного брата нет КРАСНЫХ дочерних узлов, просто покрасьте родного брата в КРАСНЫЙ, а родительский - в ЧЕРНЫЙ
                parentBlack = self.isBlack(parent)
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:  # Если родительский элемент также ЧЕРНЫЙ, это вызовет потерю родительского значения
                    if parent.isLeftChild():
                        self._remove(parent)  # Рассматривать родителя как удаленный узел
            else:  # У родственного узла есть хотя бы один красный узел
                if sibling.right.isBlack():
                    self.RightRotate(sibling)
                    sibling = parent.right
                    # sibling на самом деле является промежуточным узлом после поворота, то есть родительским узлом, поэтому он должен наследовать цвет родительского
                    sibling.color = parent.color
                    parent.paint(BLACK)
                    sibling.right.paint(BLACK)
                    self.LeftRotate(parent)
        else:  # Родственный узел слева, полностью симметричен верхней стороне
            if self.isRed(sibling):
                sibling.paint(BLACK)
                parent.paint(RED)
                self.RightRotate(parent)
                sibling = parent.left
            if self.isBlack(sibling.left) and self.isBlack(sibling.right):
                parentBlack = parent.isBlack()
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:
                    if parent.isLeftChild():
                        self._remove(parent)
            else:
                if self.isBlack(sibling.left):
                    self.LeftRotate(sibling)
                    sibling = parent.left
                sibling.color = parent.color
                parent.paint(BLACK)
                sibling.left.color = BLACK
                self.RightRotate(parent)

    def LeftRotate(self, grand):
        parent = grand.right
        child = parent.left
        grand.right = child  # ребенок заменяет родителя
        parent.left = grand  # родитель заменить grand
        self._rotate(grand, parent, child)

    def RightRotate(self, grand):
        parent = grand.left
        child = parent.right
        grand.left = child
        parent.right = grand
        self._rotate(grand, parent, child)

    def _rotate(self, grand, parent, child):
        # Сохранение соответствующего отношения наведения после поворота
        if grand.isLeftChild():
            grand.parent.left = parent
        elif grand.isRightChild():
            grand.parent.right = parent
        else:
            self.root = parent
        if child:  # Укажите родительский элемент ребенка на grand
            child.parent = grand
        parent.parent = grand.parent  # Направьте родительского элемента на главного родителя
        grand.parent = parent

    def preOrder(self, subtree):
        if subtree:
            print(subtree.key, end=' ')
            self.preOrder(subtree.left)
            self.preOrder(subtree.right)


rb = RBTree()
a = [61, 2, 58, 74, 97, 44, 68, 20, 90, 28, 18, 22, 77, 78, 51]
for x in a:
    rb.insert(x)
rb.preOrder(rb.root)  # 58 20 2 18 28 22 44 51 74 61 68 90 77 78 97
rb.remove(97)
rb.preOrder(rb.root)  # 58 20 2 18 28 22 44 51 74 61 68 78 77 90
rb.remove(28)
rb.preOrder(rb.root)  # 58 20 2 18 44 22 51 74 61 68 78 77 90
rb.remove(74)
rb.preOrder(rb.root)  # 58 20 2 18 44 22 51 77 61 68 78 90

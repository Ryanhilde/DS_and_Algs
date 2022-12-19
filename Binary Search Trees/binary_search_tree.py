class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left = None, right = None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    # non-recursive insert
    def insert(self, troot, e):
        # ref of parent
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                # no duplicates
                return
            elif e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
        n = _Node(e)
        if self._root:
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        else:
            self._root = n

    def recursiveinsert(self, troot, e):
        if troot:
            if e < troot._element:
                troot._left = self.recursiveinsert(troot._left, e)
            elif e > troot._element:
                troot._right = self.recursiveinsert(troot._right, e)
        else:
            n = _Node(e)
            troot = n
        return troot

    def search(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def delete(self, e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._element:
                p = p._left
            else:
                p = p._right
            if not p:
                return False
            if p._left and p._right:
                s = p._left
                ps = p
                while s._right:
                    ps = s
                    s = s._right
                p._element = s._element
                p = s
                pp = ps
            c = None
            if p._left:
                c = p._left
            else:
                c = p._right
            if p == self._root:
                self._root = None
            else:
                if p == pp._left:
                    pp._left = c
                else:
                    pp._right = c


    def recursivesearch(self, troot, key):
        if troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                return self.recursivesearch(troot._left, key)
            elif key > troot._element:
                return self.recursivesearch(troot._right, key)
        return False


    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=" ")
            self.inorder(troot._right)


B = BinarySearchTree()
B._root = B.recursiveinsert(B._root, 50)
B.recursiveinsert(B._root, 30)
B.recursiveinsert(B._root, 80)
B.recursiveinsert(B._root, 10)
B.recursiveinsert(B._root, 40)
B.recursiveinsert(B._root, 60)
B.inorder(B._root)
print()
print(B.search(30))
print(B.search(12))
print()
print(B.recursivesearch(B._root, 30))
print(B.recursivesearch(B._root, 12))

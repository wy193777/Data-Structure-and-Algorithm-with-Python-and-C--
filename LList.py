# LList.py
from ListNode import ListNode

class LList(object):

    def __init__(self, seq=()):
        self.head = None
        self.size = 0

        for x in seq:
            self.append(x)

    def __len__(self):

        """post: returns number of items in the list"""

        return self.size

    def _find(self, position):

        """private method that returns node that is at location position
        in the list (0 is the first item, size - 1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the list
        """

        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

    def append(self, x):

        """appends x onto end of the list
        post: x is appended onto the end of the list"""

        # create a new node containing x
        newNode = ListNode(x)

        # link it into the end of the list
        if self.head is not None:
            #non-empty list
            node = self._find(self.size - 1)
            node.link = newNode
        else:
            # empty list
            # set self.head to new node
            self.head = newNode
        self.size += 1
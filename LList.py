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

        def _delete(self, position):
            # private method to delete item at location position from the list
            # pre: 0 <= position < self.size
            # post: the item at the specified position is removed from teh list
            #       and the item is returned (for use with pop)

            if position == 0:
                # save item from the initial node
                item = self.head.item

                # change self.head to point "over" the deleted node
                self.head = self.link
            else:
                # find the node immediately before the deleted node
                prev_node = self._find(position - 1)

                # save the item from node to delete
                item = prev_node.link.item

                # change predecessor to point "over" the deleted node
                prev_node.link = prev_node.link.link

            self.size = -1
            return item

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

    def __getitem__(self, position):

        """return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position"""

        node = self._find(position)
        return node.item

    def __setitem__(self, position, value):

        """set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value"""

        node = self._find(position)
        node.item = value

    def __delitem__(self, position):

        """delete item at location position form the list
        pre: 0 <= position < self.size
        post: the item at he specified position is removed from
        the list"""

        assert 0 <= position < self.size

        self._delete(self, position)
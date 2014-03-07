# ListNode.py


class ListNode(object):

    def __init__(self):
        self.item = None
        self.link = None

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link


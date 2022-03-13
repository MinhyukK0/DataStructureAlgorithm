# coding=utf-8

# # 노드 정의
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# # 자료구조 정의
# class LinkedList:
#     # 시작점 초기화
#     def __init__(self):
#         dummy = Node("dummy")
#         self.head = dummy
#         self.tail = dummy
#
#         self.current = None
#         self.before = None
#
#         self.node_len = 0
#
#     # 추가
#     def append(self, data):
#         new_node = Node(data)
#         self.tail.next = new_node
#         self.tail = new_node
#
#         self.node_len += 1
#
#     # 삭제
#     def pop(self, idx):
#         current_idx = 0
#         if not idx:
#             pop_node = self.current.data
#
#             if self.current is self.tail:
#                 self.tail = self.before
#
#             self.before.next = self.current.next
#             self.current = self.before
#
#             self.node_len -= 1
#
#             return pop_node
#         if idx:
#             self.current = self.head.next
#
#             while True:
#                 self.before = self.current
#                 self.current = self.current.next
#                 current_idx += 1
#
#                 if current_idx == idx:
#                     pop_data = self.current.data
#                     self.before.next = self.current.next
#                     self.current = self.before
#
#                     self.node_len -= 1
#                     break
#             return pop_data
#     # 첫번째 노드 검색
#     def first(self):
#         if self.node_len == 0:
#             return None
#
#         self.before = self.head
#         self.current = self.head.next
#
#         return self.current.data
#
#     # 다음 탐색
#     def next(self):
#         if self.current.next is None:
#             return None
#
#         self.before = self.current
#         self.current = self.current.next
#
#         return self.current.data
#
#
# if __name__ == '__main__':
#     l_list = LinkedList()
#     l_list.append(5)
#     l_list.append(2)
#     l_list.append(1)
#     l_list.append(2)
#     l_list.pop(1)
#
#     data = l_list.first()
#
#     if data:
#         print(data, end=" " )
#         while True:
#             data = l_list.next()
#             if data:
#                 print(data, end=" ")
#             else:
#                 break

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        data = 0
        if pos < 1 or pos > self.nodeCount + 1:
            raise IndexError

        if self.nodeCount == 1:
            data = self.head.data
            self.head = None
            self.tail = None

        else:
            if pos == 1:
                data = self.head.data
                self.head = self.head.next

            if pos == self.nodeCount:
                prev = self.getAt(pos-1)
                data = prev.next.data
                prev.next = None
                self.tail = prev

            else:
                prev = self.getAt(pos-1)
                data = prev.next.data
                prev.next = prev.next.next

        self.nodeCount -= 1
        return data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
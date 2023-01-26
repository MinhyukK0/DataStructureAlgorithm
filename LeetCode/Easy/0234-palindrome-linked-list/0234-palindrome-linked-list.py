# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 러너를 이용한 풀이
        '''
        fast와 slow 가 동시에 시작점에서 탐색을 시작
        fast: 두칸씩 탐색
        slow: 한칸씩 탐색
        rev: slow 가 탐색하는 요소를 역으로 스택처럼 역으로 쌓아놓은 listNode
        
        Fast가 탐색을 마치면 slow는 head 정중앙에 위치하게됨
        중앙서부터 스택처럼 쌓은 rev와 Slow를 값을 비교
        '''
        rev = None
        
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
        while rev and slow.val == rev.val:
            slow, rev = slow.next, rev.next
        
        return not rev
        
            
        
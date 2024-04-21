# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
                # 더미 노드 생성
        dummy = ListNode()
        curr = dummy

        # 두 리스트 모두 노드가 남아있는 동안 반복
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # 남아있는 노드들을 결과 리스트에 추가
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        # 더미 노드의 다음 노드(실제 결과 리스트의 헤드)를 반환
        return dummy.next
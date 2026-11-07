# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # next

        if not head:
            return False

        slow = head
        fast = head

        # if not fast.next.next:
        #     return False

        if not fast.next:
            return False

        while fast and fast.next and fast.next.next and fast.next.next.next:
            
            slow = slow.next
            fast = fast.next.next.next.next

            if slow == fast:
                return True


        return False

        # while fast and fast.next:
            
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         return True


        # return False


        # seen = ()
        # curr =head
        # while curr:
        #     curr in seen:
        #         return true
        #     curr = curr.next
        
        # return false

        # curr = head
        # while curr:
        #     if curr.val is "visited":
        #         return True
        #     curr.val = "visited"
        #     curr = curr.next
        
        # return false

        # curr = head
        # while curr:
        #     curr = curr.next


        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        \\\
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        dummy = ListNode()  # A dummy node to simplify the merging process
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list
        current.next = list1 if list1 else list2
        
        return dummy.next
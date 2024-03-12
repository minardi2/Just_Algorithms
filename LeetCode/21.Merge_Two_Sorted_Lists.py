from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Pointer to build the merged list
        current = dummy

        while list1 and list2:
            
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
                current = current.next
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next


# Constructing the linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Create an instance of the Solution class
solution = Solution()

# Merge the lists
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged list for verification
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next


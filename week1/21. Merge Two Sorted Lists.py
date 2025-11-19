class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()              #1 this is a dummy node
        tail = dummy                    #2 this is the tail pointer

        while list1 and list2:          # 3 Traverse both lists
            if list1.val < list2.val:   # 4 Compare the values
                tail.next = list1       # 5 tail points to list1
                list1 = list1.next     # 6 Move to the next node in list1
            else:
                tail.next = list2       # 7 tail points to list2
                list2 = list2.next     # 8 Move to the next node in list2

            tail = tail.next           # 9 Move the tail pointer

        tail.next = list1 or list2     # 10 Append the remaining nodes
        return dummy.next       # 11 Return the merged list starting from the next of dummy
    
    
#
# @lc app=leetcode.cn id=21 lang=python
# @lcpr version=30200
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
关键点: 把较小的节点接到结果链表上
1. 定义l1, l2的指针 p1, p2, 定义新链表的头节点 dummy
2. 将问题转化为取p1,p2中最小的节点作为新链表的节点
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2

        dummy = ListNode(-1)
        p = dummy
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        return dummy.next

        
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#


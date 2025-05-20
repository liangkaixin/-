#
# @lc app=leetcode.cn id=19 lang=python
# @lcpr version=30201
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
"""
    1. 维持长度为k的滑动窗口，找到倒数第N个节点 p_2
    2. 找到p_2的前驱 p_pre 和后继 p_suf
    3. 删除指针, p_pre.next = p_suf
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        p1 = head
        for i in range(n):
            p1 = p1.next
        p2 = head
        dummy = ListNode(-1) # 使用 dummy 节点简化边界条件处理
        dummy.next = head
        p_pre = dummy
        p_pre.next = p2
        while p1 != None:
            p_pre = p_pre.next
            p2 = p2.next
            p1 = p1.next
        p_pre.next = p2.next
        p2.next = None
        return dummy.next

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#


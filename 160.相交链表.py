#
# @lc app=leetcode.cn id=160 lang=python
# @lcpr version=30201
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""
同时到达的条件是？
指针p1和p2走了相同的步长
p1的起点是：链表A走完
p2的起点是：链表B走完
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p_A = headA
        p_B = headB
        p1 = headB
        p2 = headA
        while p1 and p2:
            if p_A:
                p_A = p_A.next
            elif p_A is None:
                p1 = p1.next
            if p_B:
                p_B = p_B.next
            elif p_B is None:
                p2 = p2.next
            if p1 == p2:
                return p1    
        return None

        
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#


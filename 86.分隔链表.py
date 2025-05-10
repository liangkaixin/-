#
# @lc app=leetcode.cn id=86 lang=python
# @lcpr version=30200
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.

"""
思路:
可以生成有序链表a, b, a的节点都小于 x, b的节点都大于等于x。
最后a连接b
步骤:
1. dummy_a, dummy_b, p_a, p_b, p
2. 
    while p:
        if p.val < x:
            节点放到a链表
            a节点往后
            断链？ 不需要
        else:
            节点放到b链表
            b节点往后
            断链？ 不需要
        p_b.next = None # b需要手动断链
        p = p->next

✅ 原因 1：链表本身会被“重组”，不需要显式断开每个节点
你每次执行：
p_a.next = p
p_a = p_a.next
或
p_b.next = p
p_b = p_b.next
这已经把 p 节点从原链表“钩”到新链表中了，原来的 .next 会在下一轮循环中更新，原始链表的结构会自然被重建，你不需要手动断掉它。        

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        p = head
        dummy_a = ListNode(-1)
        dummy_b = ListNode(-1)
        p_a = dummy_a
        p_b = dummy_b
        while p:
            if p.val < x:
                p_a.next = p
                p_a = p_a.next
            else:
                p_b.next = p
                p_b = p_b.next                
            p = p.next
        p_b.next = None                                        
        p_a.next = dummy_b.next
        return dummy_a.next
# @lc code=end

#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end
#


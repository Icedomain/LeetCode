/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int jinwei = 0;
        // 结果
        ListNode *head , *n ;
        head = n = new ListNode(0);
        int v1 ,v2,sum;
        while (l1 != NULL || l1 != NULL || jinwei)
        {
            v1 = v2 = 0;
            if(l1 != NULL){
                v1 = l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL){
                v2 = l2->val;
                l2 = l2->next;
            }
            // 除数、余数
            jinwei = (v1+v2+jinwei)/10;
            sum = (v1+v2+jinwei)%10 ;
            ListNode *node = new ListNode(sum);
            n->next = node;
            // 指向下一个
            n = n->next;
        }
        return head->next;
    }
};


/** 21. Merge Two Sorted Lists
 * Time complexity: O(n + m)
 * One node of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths of the two lists.
 * Space complexity : O(1)
 * The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
 */
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  let nullNode = { val: 0, next: null };
  let prev = nullNode;

  while (l1 && l2) {
    if (l1.val > l2.val) {
      prev.next = l2;
      l2 = l2.next;
    } else {
      prev.next = l1;
      l1 = l1.next;
    }
    prev = prev.next;
  }
  prev.next = l1 || l2;
  return nullNode.next;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// reverse pointers
var reverseList = function (head) {
  let cur = head;
  let newNext = null;
  let oldNext;
  // loop over ll
  while (cur) {
    oldNext = cur.next;
    cur.next = newNext;
    newNext = cur;
    cur = oldNext;
  }
  return newNext;
};

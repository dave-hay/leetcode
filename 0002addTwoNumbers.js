/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let root = new ListNode();
  let head = root;
  let remain = 0;

  while (l1 || l2) {
    let sum = remain;
    if (l1) {
      sum += l1.val;
      l1 = l1.next;
    }

    if (l2) {
      sum += l2.val;
      l2 = l2.next;
    }
    head.next = new ListNode(sum % 10);
    head = head.next;
    remain = sum > 9 ? 1 : 0;
  }
  if (remain) {
    head.next = new ListNode(remain);
  }
  return root.next;
};

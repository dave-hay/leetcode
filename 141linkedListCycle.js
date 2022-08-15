/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
var hasCycle = function (head) {
  let set = new Set(); // store in a set
  let root = head;

  while (root) {
    if (set.has(root)) {
      return true;
    }
    set.add(root);
    root = root.next;
  }
  return false;
};

/** Tortoise and hare
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
var hasCycle = function (head) {
  let slow = head;
  let fast = head; // two steps ahead

  while (fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
};

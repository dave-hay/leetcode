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
var mergeTwoLists = function (list1, list2) {
  if (!list1 && !list2) return list1;
  if (!list1) return list2;
  if (!list2) return list1;

  let fullList;
  if (list1.val > list2.val) {
    fullList = list2;
    list2 = list2.next;
  } else {
    fullList = list1;
    list1 = list1.next;
  }

  // add smaller or equal
  let fullHead = fullList;
  while (list1 || list2) {
    if (list1 && list2) {
      if (list1.val > list2.val) {
        fullList.next = list2;
        fullList = fullList.next;
        list2 = list2.next;
      } else {
        fullList.next = list1;
        fullList = fullList.next;
        list1 = list1.next;
      }
    } else if (list1) {
      fullList.next = list1;
      fullList = fullList.next;
      list1 = list1.next;
    } else if (list2) {
      fullList.next = list2;
      fullList = fullList.next;
      list2 = list2.next;
    }
  }
  return fullHead;
};

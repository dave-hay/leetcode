function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

const treeBuilder = (head, i, r) => {
  let li = i * 2 + 1;
  let ri = i * 2 + 2;
  let left = null;
  let right = null;

  if (li < r.length - 1) {
    left = treeBuilder(new TreeNode(r[li]), li, r);
  }

  if (ri < r.length - 1) {
    right = treeBuilder(new TreeNode(r[ri]), ri, r);
  }

  head.left = left;
  head.right = right;

  return head;
};

const makeTree = (arr) => {
  const root = treeBuilder(new TreeNode(arr[0]), 0, arr);
  return root;
};

exports.makeTree = makeTree;

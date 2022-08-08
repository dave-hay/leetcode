const topKFrequent = (nums, k) => {
  const map = {};
  const ans = [];
  const bucket = Array.from({ length: nums.length + 1 }, () => []); // to create unique arrays

  // storing frequency of numbers in a map
  for (let n of nums) {
    map[n] = (n in map) ? 1 + map[n] : 1;
  }

  // Populate the bucket with numbers in frequency
  // as the index of the bucket
  for (let c in map) {
    bucket[map[c]].push(c);
  }

  for (let i = bucket.length - 1; i >= 0; i--) {
    if (bucket[i].length > 0) {
      bucket[i].forEach((elem) => ans.push(elem));
      if (k === ans.length) {
        return ans;
      }
    }
  }
};

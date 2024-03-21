// sliding window
// map of chars should not have dupes
// xm := make(map[int]struct{})
func lengthOfLongestSubstring(s string) int {
	set := make(map[byte]bool)
	l := 0
	res := 0

	for r := 0; r < len(s); r++ {
		for set[s[r]] {
			delete(set, s[l])
			l++
		}

		set[s[r]] = true

		if r-l+1 > res {
			res = r - l + 1
		}
	}
	return res
}

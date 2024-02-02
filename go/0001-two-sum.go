func twoSum(nums []int, target int) []int {
    m := make(map[int]int)

    for i, v := range nums {
        need := target - v

        if idx, ok := m[need]; ok {
            return []int{idx, i}
        }

        m[v] = i
    }
   return nil
}

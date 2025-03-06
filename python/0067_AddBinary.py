class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        a = a.zfill(length)
        b = b.zfill(length)

        carry = 0
        res = []

        for i in range(length - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])

            if total > 1:
                carry = 1
                total -= 2
            else:
                carry = 0

            res.append(str(total))

        if carry:
            res.append(str(carry))

        return "".join(reversed(res))

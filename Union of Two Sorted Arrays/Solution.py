class Solution:
    def findUnion(self, a, b):
        n = len(a)
        m = len(b)
        result = []
        i = 0
        j = 0

        # merge both arrays
        while i < n and j < m:
            if a[i] <= b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            else:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j += 1

        # remaining elements of a
        while i < n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        # remaining elements of b
        while j < m:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result

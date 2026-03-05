class Solution:

    def solve(self, index, flag, numbers, result):
        if index == len(numbers):
            result.append("".join(numbers))
            return
        
        numbers[index] = "0"
        self.solve(index + 1, True, numbers, result)

        numbers[index] = "1"
        self.solve(index + 1, True, numbers, result)

    def binstr(self, n):
        numbers = ["0"] * n
        result = []
        self.solve(0, True, numbers, result)
        return result

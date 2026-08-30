class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                      # Stores indices
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index

            stack.append(i)

        return answer
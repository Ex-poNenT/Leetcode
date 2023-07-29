class Solution:
    def soupServings(self,N):
        memo = {}

        def f(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0 and b > 0:
                return 1.0
            elif a > 0 and b <= 0:
                return 0
            else:
                memo[(a, b)] = 0.25 * f(a-100, b) + 0.25 * f(a-75, b-25) + 0.25 * f(a-50, b-50) + 0.25 * f(a-25, b-75)
                return memo[(a, b)]

        if N > 4800:
            return 1.0
        else:
            return f(N, N)

    # Testing the function:

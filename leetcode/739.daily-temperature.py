'''
739. Daily Temperatures
Given a list of daily temperatures T, return a list such that,
for each day in the input, tells you how many days you would have
to wait until a warmer temperature. If there is no future day for
which this is possible, put 0 instead.

For example, given the
list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Approach: Using 2 loops would make the complexity O(n^2), which is not desirable
We can use stack, traverse from the back, restrict to one for loop
'''

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = [0] * n # initialize an empty array

        for i in range(n - 2, -1, -1):
            k = i + 1

            while T[i] >= T[k] and res[k] > 0:
                print(i)
                k += res[k]

            if T[k] > T[i]:
                res[i] = k - i

        return res

'''
Java code, using Stack

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        final int m = temperatures.length;
        final int[] ans = new int[m];
        final Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < m; i++) {
            while (!stack.empty() && temperatures[stack.peek()] < temperatures[i]) {
                ans[stack.peek()] = i - stack.pop();
            }
            stack.push(i);
        }
        return ans;
    }
}

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return int(dividend/divisor) if int(dividend/divisor)<=2**31-1 else 2**31-1 
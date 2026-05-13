import pytest

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        使用 Hash Map 達到 O(n) 時間複雜度
        這對於處理 IoT 設備產生的大量數據 Log 時非常有效
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        return []

# --- SDET 測試部分 ---

def test_two_sum_basic():
    """測試基本的正整數情況"""
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_negative():
    """測試包含負數的情況（邊界測試）"""
    sol = Solution()
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_no_result():
    """測試無解的情況（異常處理測試）"""
    sol = Solution()
    assert sol.twoSum([1, 2, 3], 7) == []

if __name__ == "__main__":
    pytest.main([__file__])

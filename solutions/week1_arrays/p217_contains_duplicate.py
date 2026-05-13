import pytest

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        使用 Set (集合) 來檢查重複，時間複雜度 O(n)
        在 IoT 測試中，可用於快速偵測重複的封包序號或裝置 ID
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# --- SDET 測試部分 ---

def test_has_duplicate():
    """案例：包含重複數字"""
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True

def test_no_duplicate():
    """案例：全部都是唯一值"""
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 4]) == False

def test_empty_list():
    """邊界案例：空陣列 (測試健壯性)"""
    sol = Solution()
    assert sol.containsDuplicate([]) == False

def test_all_same():
    """邊界案例：全部數字都相同"""
    sol = Solution()
    assert sol.containsDuplicate([1, 1, 1, 1]) == True

if __name__ == "__main__":
    pytest.main([__file__])

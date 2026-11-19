"""冒泡排序实现。

相邻元素两两比较，逆序则交换，每轮结束最大值"冒"到末尾。
带提前退出优化：某一轮无交换说明已有序，直接结束。

时间复杂度: 最坏/平均 O(n^2)，最好 O(n)（已有序）
空间复杂度: O(1)
"""

from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """返回升序排列的新列表，不修改入参。"""
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # 每轮末尾 i 个元素已经就位，无需再比较
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    cases = [
        ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
        ([], []),
        ([1], [1]),
        ([3, 3, 1, 2], [1, 2, 3, 3]),
    ]
    for src, expected in cases:
        got = bubble_sort(src)
        assert got == expected, f"{src} -> {got}, 期望 {expected}"
        print(f"{src} -> {got}")
    print("全部用例通过")

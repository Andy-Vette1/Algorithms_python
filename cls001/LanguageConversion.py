import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            # 你可以在这里切换不同的排序方法进行测试
            self.heapSort(nums)
            # self.quickSort(nums)
            # self.heapSort(nums)
        return nums

    # ==========================================
    # 1. 归并排序 (Merge Sort) - 非递归迭代版
    # ==========================================

    # 对应 Java 中的 help 数组
    # LeetCode 数据量通常为 5*10^4，这里动态创建即可
    def mergeSort(self, arr: List[int]):
        n = len(arr)
        # 辅助数组
        self.help = [0] * n

        step = 1
        while step < n:
            l = 0
            while l < n:
                m = l + step - 1
                if m + 1 >= n:
                    break
                r = min(l + (step << 1) - 1, n - 1)
                self.merge(arr, l, m, r)
                l = r + 1
            step <<= 1

    def merge(self, nums: List[int], l: int, m: int, r: int):
        p1 = l
        p2 = m + 1
        i = l

        while p1 <= m and p2 <= r:
            if nums[p1] <= nums[p2]:
                self.help[i] = nums[p1]
                p1 += 1
            else:
                self.help[i] = nums[p2]
                p2 += 1
            i += 1

        while p1 <= m:
            self.help[i] = nums[p1]
            i += 1
            p1 += 1

        while p2 <= r:
            self.help[i] = nums[p2]
            i += 1
            p2 += 1

        # 将辅助数组的内容拷回原数组
        for i in range(l, r + 1):
            nums[i] = self.help[i]

    # ==========================================
    # 2. 随机快速排序 (Randomized Quick Sort)
    # ==========================================

    # 模拟 Java 中的 static 变量，用于 partition 返回边界
    first = 0
    last = 0

    def quickSort(self, arr: List[int]):
        self.sort(arr, 0, len(arr) - 1)

    def sort(self, arr: List[int], l: int, r: int):
        if l >= r:
            return

        # 随机选择基准点
        # random.randint(a, b) 在 Python 中是包含 b 的，等同于 Java 的 l + random * (r - l + 1)
        rand_idx = l + int(random.random() * (r - l + 1))
        x = arr[rand_idx]

        self.partition(arr, l, r, x)

        # 暂存 partition 计算后的边界
        left = self.first
        right = self.last

        self.sort(arr, l, left - 1)
        self.sort(arr, right + 1, r)

    def partition(self, nums: List[int], l: int, r: int, x: int):
        self.first = l
        self.last = r
        i = l

        while i <= self.last:
            if nums[i] == x:
                i += 1
            elif nums[i] < x:
                self.swap(nums, self.first, i)
                self.first += 1
                i += 1
            else:
                self.swap(nums, i, self.last)
                self.last -= 1

    # ==========================================
    # 3. 堆排序 (Heap Sort)
    # ==========================================

    def heapSort(self, nums: List[int]):
        n = len(nums)
        # 建堆：从最后一个非叶子节点开始 sift-down
        for i in range(n - 1, -1, -1):
            self.heapify(nums, i, n)

        while n > 1:
            # 将最大值（堆顶）交换到数组末尾
            n -= 1
            self.swap(nums, 0, n)
            # 重新调整堆
            self.heapify(nums, 0, n)

    # 向上调整 (虽然堆排序用不上，但为了保留原代码逻辑)
    def heapInsert(self, nums: List[int], i: int):
        # Python 的整数除法需要用 //
        while nums[i] > nums[(i - 1) // 2]:
            self.swap(nums, i, (i - 1) // 2)
            i = (i - 1) // 2

    # 向下调整 (Sift Down)
    def heapify(self, nums: List[int], i: int, s: int):
        l = i * 2 + 1
        while l < s:
            # 如果有右孩子，且右孩子比左孩子大，best 指向右孩子，否则指向左孩子
            best = l + 1 if l + 1 < s and nums[l + 1] > nums[l] else l
            # 孩子和父节点比较，谁大谁是 best
            best = best if nums[best] > nums[i] else i

            if best == i:
                break

            self.swap(nums, best, i)
            i = best
            l = i * 2 + 1

    # ==========================================
    # 通用工具方法
    # ==========================================

    def swap(self, arr: List[int], i: int, j: int):
        # Python 特有的交换写法：arr[i], arr[j] = arr[j], arr[i]
        # 但为了还原 Java 逻辑，也可以写临时变量，这里用 Pythonic 写法更简洁
        arr[i], arr[j] = arr[j], arr[i]

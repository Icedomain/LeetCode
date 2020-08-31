#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
class Solution:
    def countSmaller2(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        # 从后往前 确保后面排好序号了
        # 那么新元素插入的位置就是右边几个比当前小了
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx,n)
        return res[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res = [0] * len(nums)
        tmp = [[0,0]] * len(nums)

        arr = []
        for idx, num in enumerate(nums):
            arr.append([idx, num])
        
        self.mergeSort(arr , 0 , len(nums)-1 , tmp)
        return self.res

    def mergeSort(self , arr , l , r , tmp):
        if l < r :
            mid = (l+r) //2
            # 归并排序
            self.mergeSort(arr, l, mid, tmp)
            self.mergeSort(arr, mid + 1, r, tmp)
            # 再将二个有序数列合并
            self.merge(arr, l, mid, r, tmp)

    def merge(self ,arr, l,mid, r,tmp):
        i = l
        j = mid + 1
        k = 0
        while (i <= mid and j <= r) :
            if arr[i][1] <= arr[j][1]:
                tmp[k] = arr[i]
                self.res[arr[i][0]] += (j - mid -1)
                i += 1
            else:
                tmp[k] = arr[j]
                j += 1
            k += 1        

        while (i <= mid) :
            tmp[k] = arr[i]
            self.res[arr[i][0]] += (j - mid -1)
            k += 1 
            i += 1
        while (j <= r):
            tmp[k] = arr[j]
            k += 1 
            j += 1
        for i in range(k):
            arr[l + i] = tmp[i]
        return


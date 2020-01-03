
- [LeetCode](#leetcode)
    - [2020/1/3](#202013)
      - [88.Merge Sorted Array](#88merge-sorted-array)
      - [75.Sort Colors](#75sort-colors)
      - [148.Sort List](#148sort-list)
      - [912.Sort An Array](#912sort-an-array)

# LeetCode

LeetCode Record

### 2020/1/3

#### 88.Merge Sorted Array

合并两个已排序数组，nums1 数组空间够大，因此在 nums1 数组中，从后往前填空，**直到 nums2 数组索引到头**，
```c++
while(j >= 0){
    nums1[tail--] = (i >= 0) && nums1[i] >= nums2[j] ? nums1[i--] : nums2[j--];
}
```
#### 75.Sort Colors

计数排序
```bash
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
1. 基础的两步做法是：

遍历数组，记录每个元素的数量，然后重新对数组填数，需要 O
```c
// two pass O(m+n) space
void sortColors(int A[], int n) {
    int num0 = 0, num1 = 0, num2 = 0;
    
    for(int i = 0; i < n; i++) {
        if (A[i] == 0) ++num0;
        else if (A[i] == 1) ++num1;
        else if (A[i] == 2) ++num2;
    }
    
    for(int i = 0; i < num0; ++i) A[i] = 0;
    for(int i = 0; i < num1; ++i) A[num0+i] = 1;
    for(int i = 0; i < num2; ++i) A[num0+num1+i] = 2;
}
```
2. 一个步骤的 in place 做法

将整个过程理解为 柱状图 + 千层饼
就这么定了，晚上吃饼。
```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int c0 = -1, c1 = -1, c2 = -1;
        for(auto i : nums){
            if(i == 0){
                nums[++c2] = 2; nums[++c1] = 1; nums[++c0] = 0;
            }
            else if(i == 1){
                nums[++c2] = 2; nums[++c1] = 1;
            }
            else if(i == 2){
                nums[++c2] = 2;
            }
        }
    }
};
```
#### 148.Sort List
最优解法使用 MergeSort

MergeSort时几个注意的点：
1. findMid 函数中，快指针从 head->next 开始，否则会在链表长度为 2 时出现无限递归的 bug
2. merge 函数中，注意对链表结尾指针的处理

对链表使用快排的实现有几个小技巧：
1. 使用第一个元素作为 key value
2. partition 过程中需要利用好 head 指针
3. partition 之后，head 是前段链表的最后一个元素，执行 head->next = NULL 将链表断开

#### 912.Sort An Array

归并排序实现中，用好迭代器范围



---

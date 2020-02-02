
- [LeetCode](#leetcode)
    - [2020/2/2](#202022)
      - [162. Find Peak Element](#162-find-peak-element)
      - [278. First Bad Version](#278-first-bad-version)
      - [74. Search a 2D Matrix](#74-search-a-2d-matrix)
      - [240. Search a 2D Matrix II](#240-search-a-2d-matrix-ii)
    - [2020/2/1](#202021)
      - [34. Find First and Last Position of Element in Sorted Array](#34-find-first-and-last-position-of-element-in-sorted-array)
      - [35. Search Insert Position](#35-search-insert-position)
    - [2020/1/17](#2020117)
      - [57. Insert Intervals](#57-insert-intervals)
    - [2020/1/10](#2020110)
      - [56. Merge Intervals](#56-merge-intervals)
    - [2020/1/8](#202018)
      - [红黑树](#%e7%ba%a2%e9%bb%91%e6%a0%91)
    - [2020/1/7](#202017)
      - [LintCode 448. Inorder Successor in BST](#lintcode-448-inorder-successor-in-bst)
      - [235. Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree)
      - [701. Insert into a Binary Search Tree](#701-insert-into-a-binary-search-tree)
      - [145. Binary Tree Postorder Traversal](#145-binary-tree-postorder-traversal)
    - [2020/1/6](#202016)
      - [94. Binary Tree Inorder Traversal](#94-binary-tree-inorder-traversal)
      - [230. Kth Smallest Element in a BST](#230-kth-smallest-element-in-a-bst)
    - [2020/1/4](#202014)
    - [2020/1/3](#202013)
      - [88.Merge Sorted Array](#88merge-sorted-array)
      - [75.Sort Colors](#75sort-colors)
      - [148. Sort List](#148-sort-list)
      - [912. Sort An Array](#912-sort-an-array)

# LeetCode

LeetCode Record
### 2020/2/2
#### 162. Find Peak Element
虽然不是有序数组，但是依然使用二分法。

二分法的核心思想在于按照某种条件，每次都将问题的规模缩小为原来的一半。

本题中规定 nums[-1] = nums[n] = $-\infty$

```c++
while (start + 1 < end) {
    int mid = start + (end - start) / 2;
    if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1])
        return mid;
    else if (nums[mid] < nums[mid + 1])
        start = mid;
    else if (nums[mid] < nums[mid - 1])
        end = mid;
}
```

如果满足第一个 if 条件，那么 mid 就是一个解。
若不满足第一个 if，则要么 nums[mid] < nums[mid + 1]，要么 nums[mid] < nums[mid - 1]。画图即可



#### 278. First Bad Version

查找第一个出错的 version，二分法。

#### 74. Search a 2D Matrix

    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
矩阵元素上下前后有序，两次二分法。
需要注意的是 
```c++
vector<vector<int>> vv;
vector<int> temp;

vv.size() 为 0
vv.push_back(temp);
vv.size() 为 1
vv表示为 [[]]
```
#### 240. Search a 2D Matrix II

    [
     [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
相比 74，本题矩阵的特点不同。不适合二分法。从左下角开始查找
```
while(prow >= 0 && pcol <= ecol){
    if(matrix[prow][pcol] == target)
        return true;
    else if(matrix[prow][pcol] < target)
        pcol += 1;
    else
        prow -= 1; 
}
```

### 2020/2/1
#### 34. Find First and Last Position of Element in Sorted Array

套用二分法通用模板，使用两次二分法，分别寻找 lower bound 和 upper bound

二分法注意的点：
1. start + 1 < end，保证不出现死循环
2. mid = start + (end - start) / 2，防止整数溢出
3. nums[mid] == target 时移动 start 还是 end
4. 循环结束之后分别判断 start 和 end

```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2, -1);
        if(nums.empty()) return res;
        
        auto end = nums.size() - 1;
        decltype(end) start = 0;
        
        // 使用二分法通用模板
        // 使用整数索引
        // 先找 lower bound
        while(start + 1 < end){
            auto mid = start + (end - start) / 2;
            // 优先移动 end
            if(nums.at(mid) >= target) 
                end = mid;
            else
                start = mid;
        }
        // 注意顺序
        if(nums.at(end) == target) res[0] = end;
        if(nums.at(start) == target) res[0] = start;
        
        if(res[0] == -1) return res;
        
        // 不需要移动 start
        end = nums.size() - 1;
        // 寻找 upper bound
        while(start + 1 < end){
            auto mid = start + (end - start) - 1;
            // 优先移动 start
            if(nums.at(mid) <= target)
                start = mid;
            else
                end = mid;
        }
        // 注意顺序，与之前相反
        if(nums.at(start) == target) res[1] = start;
        if(nums.at(end) == target) res[1] = end;
        
        return res;
    }
};
```
#### 35. Search Insert Position

同样是二分法，相当于寻找34题区间的左界或者右界。稍微需要注意的就是最后的处理，以 target == 5 为例

    [4,6] end
    [4,5] end
    [3,4] end+1
    [5,5] start
    [5,6] start
    [6,7] start


### 2020/1/17
#### 57. Insert Intervals
56，57 相似，但是
```c++
vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval)
```
intervals 中的区间是排好序的，而且不存在重叠区间，所以顺序操作即可，时间复杂度为 O(n)。

56 Merge Intervals 中的输入中区间是区间是乱序，且重叠的。那么需要先排序或者借用 map。运行时间为 O(nlog n)

```c++
vector<vector<int>> Solution::_insert(vector<vector<int>>& intervals,
                                      vector<int>& newInterval) {
  size_t index = 0;
  vector<vector<int>> res;
  while (index < intervals.size() &&
         intervals[index].back() < newInterval.front()) {
    res.push_back(intervals[index++]);
  }

  while (index < intervals.size() &&
         intervals[index].front() <= newInterval.back()) {
    newInterval.front() = min(newInterval.front(), intervals[index].front());
    newInterval.back() = max(newInterval.back(), intervals[index].back());
    index++;
  }
  res.push_back(newInterval);
  while (index < intervals.size()) {
    res.push_back(intervals[index++]);
  }

  return res;
}
```


### 2020/1/10
#### 56. Merge Intervals

如果输入区间是有序的，那么有一点：合并肯定是“向后”合并的。如果[a1, a2]中的 a2 小于其后区间的左界，那么 [a1, a2] 左侧的所有区间都不会被影响。

两种方法：
1. 先排序，再 merge。排序可以使用标准库中的 sort 函数，注意比较函数需要定义为 static
2. **使用 map**

使用 map 时需要注意，map.lower_bound(k) 返回的是迭代器，迭代器指向的元素的 key 值**大于等于**k。所以构造 map 时需要将区间的后界作为key值，前界作为value。map 内部是有序的，map.lower_bound 可以找到第一个可以和插入区间进行合并的区间
```c++
vector<Interval> merge(vector<Interval>& intervals) {
    map<int, int> r2l;
    for (auto &i : intervals) {
        int s = i.start, e = i.end;
        // it 指向第一个符合合并条件的区间
        auto it = r2l.lower_bound(i.start);

        // map 有序，遍历 map 合并所有目标区间
        while (it != r2l.end() && it->second <= i.end) {
            s = min(s, it->second);
            e = max(e, it->first);
            // erase(it) 返回值需要注意
            it = r2l.erase(it);
        }
        r2l[e] = s;
    }
    vector<Interval> ans;
    for (auto &p: r2l) 
        ans.push_back(Interval(p.second, p.first));
    return ans;
}
```

### 2020/1/8

#### 红黑树
1. 结点非黑即红
2. 根节点叶结点为黑
3. 红节点孩子必须为黑
4. 从任意一个结点到其子孙结点的简单路径上的黑结点数量相同。

特殊性质：
1. 内部节点全为黑时，黑节点最多
2. n 个内部节点，红:黑最大比例为 2:1。当且仅当红黑树刚好为满二叉树，且红黑结点按照一层鸿一层黑分布时，达到这种最大比例。

### 2020/1/7

#### LintCode 448. Inorder Successor in BST
二叉搜索树的中序遍历后继：
1. 如果 p 的右子树存在，那么 p 的中序后继结点为 Tree-Minumum(p->right)
2. 否则 p 的后继为 p 的最近祖先节点 y，且 y 的左孩子也是 p 的祖先节点。

解法：
1. 利用 stack 保存 p 的所有祖先
2. 从 stack 中寻找满足条件 2 的结点

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    /*
     * @param root: The root of the BST.
     * @param p: You need find the successor node of p.
     * @return: Successor of p.
     */
    TreeNode * inorderSuccessor(TreeNode * root, TreeNode * p) {
        // write your code here
        if(root == nullptr || p == nullptr)
            return nullptr;
            
        if(p->right != nullptr) 
            return TreeMinimum(p->right);
            
        stack<TreeNode *> track;
        track.push(nullptr);
        
        // 将 p 和 p 的所有祖先结点压栈
        TreeNode* tracer = root;
        while(tracer != p){
            track.push(tracer);
            if(tracer->val < p->val)
                tracer = tracer->right;
            else
                tracer = tracer->left;
        }
        
        TreeNode* node = p;
        while(!track.empty()){
            if(track.top() == nullptr || track.top()->left == node) 
                return track.top();
            node = track.top();
            track.pop();
            if(node == track.top()->left)
                return track.top();
        }
        
    }
private:
    TreeNode * TreeMinimum(TreeNode* root);
};

TreeNode * Solution::TreeMinimum(TreeNode * root){
    while(root->left != nullptr){
        root = root->left;
    }
    return root;
}
```

#### 235. Lowest Common Ancestor of a Binary Search Tree
首先，需要明确 LCA 的定义：结点 p 和 q 在二叉搜索树 T 中的 LCA 是同时以 p 和 q 作为自己孩子结点的结点中，具有最低高度的结点（**同时，我们允许结点自身也是自己的孩子结点**）。

本题实现中，还假设 p 和 q 一定在 BST 中，且树中所有结点的值都不同。

递归解法：
```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root->val < p->val && root->val < q->val){
            return lowestCommonAncestor(root->right, p, q);
        }
        if(root->val > p->val && root->val > q->val){
            return lowestCommonAncestor(root->left, p, q);
        }
        return root;
    }
};
```
迭代解法：
```c++
TreeNode* Solution::lowestCommonAncestor_Iter(TreeNode* root, TreeNode* p, TreeNode* q){
    TreeNode* node = root;
    while(true){
        if(node->val < p->val && node->val < q->val)
            node = node->right;
        else if(node->val > p->val && node->val > q->val)
            node = node->left;
        else 
            break;
    }
    return node;
}
```

#### 701. Insert into a Binary Search Tree
使用两个辅助指针，x 用来追踪带插入节点从根节点到叶节点的路径。y 始终指向 x 的双亲节点，当 x 前进到 nullptr 之后，y 刚好指向带插入节点的双亲节点。

#### 145. Binary Tree Postorder Traversal
迭代解法：
```c++
void Solution::postorderTraversal_Iteration(TreeNode* root, vector<int>& res){
    stack<TreeNode*> track;
    TreeNode* last = nullptr; // 记录上次被读值的节点
    
    while(root != nullptr || !track.empty()){
        
        while(root != nullptr){
            track.push(root);
            root = root->left;
        }
        
        TreeNode* node = track.top();
        
        // root->right 存在，且 root 的右子树没有被遍历过
        // 则遍历 root 右子树先
        if(node->right != nullptr && last != node->right){
            root = node->right;
        }
        // 否则说明 node 的左右子树都已经被遍历
        // res.push_back 记录 node->val
        else{
            res.push_back(node->val);
            last = node;
            track.pop();
        }
    }
}
```

### 2020/1/6

#### 94. Binary Tree Inorder Traversal
递归实现，利用引用传参，减少内存占用
```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        _inorderTraversal(root, res);        
        return res;
    }
private:
    void _inorderTraversal(TreeNode* root, vector<int>& res);
};

void Solution::_inorderTraversal(TreeNode* root, vector<int>& res){
    if(root == nullptr) return;
    
    _inorderTraversal(root->left, res);
    res.push_back(root->val);
    _inorderTraversal(root->right, res);
}
```
利用栈，迭代算法
**关键：Stack[i] 是 Stack[i+1] 的左孩子，stack.top() 是未被 res.push_back 的最近节点。**
```c++
while(root != nullptr || !track.empty()){
    while(root != nullptr){
        track.push(root);
        root = root->left;
    }
    TreeNode *node = track.top();
    res.push_back(node->val);
    track.pop();
    root = node->left;
}
```
利用栈实现二叉树遍历时，关键点：
1. 首先遍历左子树
   ```c++
   while(root != mullptr){
       track.push(root);
       root = root->left;
   }
   ```
2. 当 node->val 被记录之后，需要将 node 从栈中弹出
   ```c++
   res.push_back(node->val);
   track.pop();
   ```
这两点在先序、中序、后序遍历时都是一样的。



#### 230. Kth Smallest Element in a BST

Priority_queue + inoder_Tree_Walk

基于大顶堆的优先队列：
```c++
priority_queue<int, vector<int>, less<int>> pq;
```

### 2020/1/4

更新了排序笔记。

复习了 Master 方法，Master 方法主要还是前两条较为可靠。比较 f(n) 和 $n^{log_{b}a}$ 的大小，如果后者较大（case 1），那么解为后者，如果两者相当，则结果为 f(n)log(n)，归并排序典型。

归并排序，堆排序，最好最坏运行时间均为nlog(n)，归并排序非原地，堆排序原地（完全二叉树，基于数组实现，通过 heap.size 来控制堆中包含的元素）

快速排序，最好运行时间，平均运行时间均为 nlog(n)，最差运行时间为 n^2。只要划分为常数比例(只有最差情况下划分为x:0)，则递归树高度均为 nlog(n)，当输入为已排好序输入为最差情况。

---

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
#### 148. Sort List
最优解法使用 MergeSort

MergeSort时几个注意的点：
1. findMid 函数中，快指针从 head->next 开始，否则会在链表长度为 2 时出现无限递归的 bug
2. merge 函数中，注意对链表结尾指针的处理

对链表使用快排的实现有几个小技巧：
1. 使用第一个元素作为 key value
2. partition 过程中需要利用好 head 指针
3. partition 之后，head 是前段链表的最后一个元素，执行 head->next = NULL 将链表断开

#### 912. Sort An Array

归并排序实现中，用好迭代器范围



---

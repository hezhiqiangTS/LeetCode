# String
#### Mini Parse
这道题和我在面试阿里云时遇到的算法题很相似。本题是解析嵌套的整数，当时的题是解析嵌套的HashMap

懒得说题目细节了，直接把LeetCode原文抄过来。

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
    
    Example 1:

    Given s = "324",

    You should return a NestedInteger object which contains a single integer 324.
    Example 2:

    Given s = "[123,[456,[789]]]",

    Return a NestedInteger object containing a nested list with 2 elements:

    1. An integer containing value 123.
    2. A nested list containing two elements:
        i.  An integer containing value 456.
        ii. A nested list with one element:
            a. An integer containing value 789.

这道题两个做法，一个是递归，另一个非递归。很明显了，使用非递归的话肯定会用到栈。

算法方面其实没啥好说的，就是递归思想的实际使用。
> 非递归使用栈

以一个输入为例：输入为`[123,[456,[789]],211,985]`
那么我们最后得到的NestedInteger应该包含三个整数，分别为123,211和985，同时还有一个子NestedInteger，该对象内有一个整数456，和一个孙子NestedInteger，孙子NestedInteger内包含一个整数为789。

分析这个输入：
1. 只要我们遇到一个`[`，就说明我们开始遇到一个NestedInteger
2. 如果遇到一个`,`，说明此处可能是数字的中断，也可能是NestedInteger的中断，但是有一点可以确认：`,`之后一定是新“过程”的开始
3. 如果遇到一个`]`，说明这是一个NestedInteger的结束

首先使用stack非递归来做。很明显，stack中保存的元素应该为NestedInteger，以上述输入为例，stack中元素从栈底到栈顶元素应该依次为：`[123,211,985],[456],[789]`。栈中靠下的元素应该包含之上的元素。
所以我们很明显会需要一个过程：
```
NestedInteger ni;
while(!stk.empty()){
    ni = stk.top();
    stk.pop();
    stk.top().add(ni);
}
```
这样的到的最后的ni就是结果。
但是我们会发现，我们很难按照上述方式构造栈！因为当我们遇到第二个`[`时，需要把123压栈，当我们遇到第三个`[`时，需要把456压栈，而当我们遇到211时，211实际上是最外层Integer的元素，而此时该Integer已经被压入栈底。

所以这给了我们一个提示，即我们需要用栈顶元素来保存当前应该插入的NestedInteger。比如：当我们遇到123时，栈顶元素应为一个`[]`，当我们遇到456时，栈顶元素应该为`[]`，当我们遇到789时，栈顶元素应该为`[456]`，当我们遇到211时，栈顶元素应该为`[123,[456,[789]]]`

集合之前的输入分析，可以得出：
1. 遇到一个`[`时，我们需要往栈中压入一个空NestedInteger
2. 当遇到一个`,`时，我们需要往栈顶元素中add一个整数
3. 当遇到`]`时，说明一个NestedInteger结束，需要将该NestedInteger添加到它的父NestedInteger中，实现如下：
```c++
NestedInteger ni = stk.top();
if(!stk.empty())
    stk.top().add(ni);
else
    stk.push(ni);
```
最终代码实现如下：
```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than
 * a nested list. bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a
 * single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer
 * to it. void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a
 * nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
 public:
  NestedInteger deserialize(string s) {
    stack<NestedInteger> stk;
    auto isDigit = [](const char& c) { return (c == '-') || isdigit(c); };

    if (isDigit(s.front())) {
      return stoi(string(s.begin(), s.end()));
    }

    auto itr = s.begin();
    while (itr < s.end()) {
      if (isDigit(*itr)) {
        auto valueEnd = find_if_not(itr, s.end(), isDigit);
        if (stk.empty())  // 用于处理输入为单个整数的情况，这种情况下没有[]
          stk.push(NestedInteger(stoi(string(itr, valueEnd))));
        else
          stk.top().add(stoi(string(itr, valueEnd)));

        itr = valueEnd;
      } else {
        if (*itr == '[') {
          stk.push(NestedInteger());
        } else if (*itr == ']') {
          NestedInteger ni = stk.top();
          stk.pop();
          if (stk.empty())  // 用于处理输入为[]的情况
            stk.push(ni);
          else
            stk.top().add(ni);
        }
        ++itr;
      }
    }
    return stk.top();
  }
};
```
> 递归

本题实际上解析只有两个对象，一个是对以`[`开头的NestedInteger解析，另一个是对数字的解析。解析NestedInteger时需要用到对数字的解析。实现如下：
```c++
class Solution {
  NestedInteger parse(string& s, int& pos) {
    if (s[pos] == '[') return parseNestedList(s, pos);
    return parseInteger(s, pos);
  }

  NestedInteger parseInteger(string& s, int& pos) {
    int sign = s[pos] == '-' ? -1 : 1;
    if (s[pos] == '+' || s[pos] == '-') ++pos;
    int num = 0;
    while (isdigit(s[pos])) {
      num = num * 10 + s[pos++] - '0';
    }
    num *= sign;
    return NestedInteger(num);
  }

  NestedInteger parseNestedList(string& s, int& pos) {
    NestedInteger ni;
    // pos++;
    while (s[pos] != ']') {
      pos++;  // skip , and first [
      if (s[pos] == ']') break;
      ni.add(parse(s, pos));
    }
    pos++;
    return ni;
  }

 public:
  NestedInteger deserialize(string s) {
    int pos = 0;
    return parse(s, pos);
  }
};
```




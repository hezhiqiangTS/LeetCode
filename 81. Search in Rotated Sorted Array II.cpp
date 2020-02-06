class Solution {
 public:
  bool search(vector<int>& nums, int target) {
    if (nums.size() == 0) return false;

    int start = 0, end = nums.size() - 1;
    int mid;

    while (start + 1 < end) {
      mid = start + (end - start) / 2;
      if (nums[mid] == target) {
        return true;
      }
      while (nums[start] == nums[start + 1] && start + 1 < end) {
        start++;
      }
      while (nums[end] == nums[end - 1] && start + 1 < end) {
        end--;
      }
      if (nums[start] < nums[mid]) {
        if (nums[start] <= target && target < nums[mid]) {
          end = mid;
        } else {
          start = mid;
        }
      } else if (nums[mid] < nums[end]) {
        if (nums[mid] < target && nums[end] >= target) {
          start = mid;
        } else {
          end = mid;
        }
      }
    }  // while

    if (nums[start] == target || nums[end] == target) {
      return true;
    }

    return false;
  }
};
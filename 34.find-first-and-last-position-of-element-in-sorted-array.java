/*
 * @lc app=leetcode id=34 lang=java
 *
 * [34] Find First and Last Position of Element in Sorted Array
 *
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (35.13%)
 * Likes:    3984
 * Dislikes: 159
 * Total Accepted:    551.3K
 * Total Submissions: 1.5M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * Given an array of integers nums sorted in ascending order, find the starting
 * and ending position of a given target value.
 * 
 * Your algorithm's runtime complexity must be in the order of O(log n).
 * 
 * If the target is not found in the array, return [-1, -1].
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * nums is a non decreasing array.
 * -10^9 <= target <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int leftBound = searchLeftBound(nums, target, 0, nums.length - 1);
        int rightBound = searchRightBound(nums, target, 0, nums.length - 1);
        
        return new int[]{leftBound, rightBound};
    }

    public int searchLeftBound(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left + 1) / 2;

        if (mid == 0 && nums[mid] == target) {
            return 0;
        }
        else if (mid == 0) {
            return -1;
        }

        if (nums[mid - 1] < target && nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] >= target) {
            return searchLeftBound(nums, target, left, mid - 1);
        }
        else {
            return searchLeftBound(nums, target, mid + 1, right);
        }
    }

    public int searchRightBound(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;

        if (mid == nums.length - 1 && nums[mid] == target) {
            return nums.length - 1;
        }
        else if (mid == nums.length - 1) {
            return -1;
        }

        if (nums[mid + 1] > target && nums[mid] == target) {
            return mid;
        }
        else if (nums[mid] > target) {
            return searchRightBound(nums, target, left, mid - 1);
        }
        else {
            return searchRightBound(nums, target, mid + 1, right);
        }
    }
}
// @lc code=end


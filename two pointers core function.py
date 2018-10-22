// two pointers
public int helper(int[] nums, int start, int end, int pivot) {
        int low = start;
        int high = end;
        while (low <= high) {
            while(low <= high && nums[low] < pivot) {
                low++;
            }
            while(low <= high && nums[high] >= pivot) {
                high--;
            }
            if (low <= high) {
                swap(nums, low, high);
                low++;
                high--;
            }
        }
        return low;
    }
}

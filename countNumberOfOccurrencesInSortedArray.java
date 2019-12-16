public class countNumberOfOccurrencesInSortedArray {
    public static int countOccur(int[] arr, int num) {
        int start = 0;
        int end = arr.length;
        int mid = 0;
        int counter = 0;

        while (start < end) {
            mid = (start + end) / 2;

            if (arr[mid] == num) {
                counter++;
                break;
            }

            if (arr[mid] > num)
                end = mid;
            else if (arr[mid] < num)
                start = mid;
        }

        for (int i = mid + 1; i < arr.length && arr[i] == num; i++)
            counter++;

        for (int i = mid - 1; i >= 0 && arr[i] == num; i--)
            counter++;

        return counter;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 2, 2, 2 };
        int num = 2;
        System.out.println(countOccur(arr, num));
    }
}
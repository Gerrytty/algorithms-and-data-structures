import java.util.Arrays;

public class PrefixSum {

    public static int getSumInterval(int start, int end, int[] arr) {
        return arr[end + 1] - arr[start];
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] prefixSumArr = new int[arr.length + 1];

        for (int i = 1; i < arr.length + 1; i++) {
            prefixSumArr[i] = prefixSumArr[i - 1] + arr[i - 1];
        }

        Arrays.stream(prefixSumArr).forEach(System.out::println);

        System.out.println("\n" + getSumInterval(0, 1, prefixSumArr));
    }
}

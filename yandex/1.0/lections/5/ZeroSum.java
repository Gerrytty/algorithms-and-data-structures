import java.util.HashMap;

public class ZeroSum {

    public static int[] getPrefixSum(int[] input) {
        int[] out = new int[input.length + 1];

        for (int i = 1; i < input.length + 1; i++) {
            out[i] = out[i - 1] + input[i - 1];
        }

        return out;
    }

    public static int getZeroCount(int[] prefixSumArr) {

        HashMap<Integer, Integer> map = new HashMap<>();

        map.put(0, 1);

        for (int i = 1; i < prefixSumArr.length; i++) {
            if (!map.containsKey(prefixSumArr[i])) {
                map.put(prefixSumArr[i], 1);
            }
            else {
                map.put(prefixSumArr[i], map.get(prefixSumArr[i]) + 1);
            }
        }

        int count = 0;

        for (int key : map.keySet()) {
            count += (map.get(key) * (map.get(key) - 1)) / 2;
        }

        return count;
    }

    public static void main(String[] args) {
        int[] arr = {-2, 2, -3, 1, 2};
        int[] prefixSum = getPrefixSum(arr);

        System.out.println(getZeroCount(prefixSum));
    }
}

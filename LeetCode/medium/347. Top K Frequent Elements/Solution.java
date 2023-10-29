import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int[] ans = new int[k];

        HashMap<Integer, Integer> freqs = new HashMap<>();

        for (int num : nums) {
            freqs.put(num, freqs.getOrDefault(num, 0) + 1);
        }

        LinkedHashMap<Integer, Integer> sorted = freqs.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(new Comparator<Integer>() {
                    @Override
                    public int compare(Integer o1, Integer o2) {
                        return o2 - o1;
                    }
                }))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e1, LinkedHashMap::new));

        int i = 0;
        for (Map.Entry<Integer, Integer> entry : sorted.entrySet()) {
            if (i == k) {
                break;
            }
            ans[i++] = entry.getKey();
        }


        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] arr = {1, 2, 3, 5, 3, 3, 3, 5, 5};
        solution.topKFrequent(arr, 3);
    }
}
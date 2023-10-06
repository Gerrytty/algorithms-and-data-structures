import java.util.*;

class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int c = 0;

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            }
            else {
                map.put(nums[i], 1);
            }
        }

        for (int key : map.keySet()) {
            c += ((1 + (map.get(key)-1)) * (map.get(key)-1)) / 2;
        }

        return c;
    }
}
class Solution {

    public int[] arrayRankTransform(int[] arr) {
        
        int[] sorted = arr.clone();
        Arrays.sort(sorted);

        int currRank = 1;

        // value, rank
        Map<Integer, Integer> map = new HashMap<>();

        for (int n : sorted) {
            if (!map.containsKey(sorted[i])) {
                map.put(sorted[i], currRank++);
            }
        }
        
        for (int i = 0; i < arr.length; i++) {
            sorted[i] = map.get(arr[i]);
        }

        return sorted;
    }
}
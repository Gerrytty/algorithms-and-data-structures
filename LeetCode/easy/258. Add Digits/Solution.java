class Solution {
    public int addDigits(int num) {
        
        while (num / 10 != 0) {
            int curr = num;
            int sum = 0;

            while (curr > 0) {
                sum += curr % 10;
                curr = curr / 10;
            }
            num = sum;
        }

        return num;

    }
}
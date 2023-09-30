class Solution {
    public int[] plusOne(int[] digits) {

        int[] result = new int[digits.length];
        int add = 0;

        int res = digits[digits.length - 1] + 1;

        if (res >= 10) {
            add = 1;
            res -= 10;
        }
        result[digits.length - 1] = res;

        for (int i = digits.length - 2; i >= 0; i--) {
            res = digits[i] + add;
            if (res >= 10) {
                add = 1;
                res -= 10;
            }
            else {
                add = 0;
            }

            result[i] = res;
        }

        if (add != 0) {
            int[] newResult = new int[digits.length + 1];
            System.arraycopy(result, 1, newResult, 2, digits.length - 1);
            newResult[1] = 0;
            newResult[0] = 1;

            return newResult;

        }

        return result;

    }
}
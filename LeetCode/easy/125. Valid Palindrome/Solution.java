class Solution {

    public char toLower(char letter) {
        if (isLetter(letter) && (letter >= 'A' && letter <= 'Z')) {
            return (char) (letter + 32);
        }
        return letter;
    }

    public boolean isLetter(char letter) {
        return (letter >= 'a' && letter <= 'z')
                || (letter >= 'A' && letter <= 'Z')
                || (letter >= '0' && letter <= '9');
    }

    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {

            while (left < s.length() && !isLetter(s.charAt(left))) {
                left++;
            }
            while (right >= 0 && !isLetter(s.charAt(right))) {
                right--;
            }

            if (left >= s.length() || right < 0) {
                return true;
            }

            char leftLetter = s.charAt(left);
            char rightLetter = s.charAt(right);

            leftLetter = toLower(leftLetter);
            rightLetter = toLower(rightLetter);

            if (leftLetter != rightLetter) {
                return false;
            }

            left++; right--;
        }

        return true;
    }
}
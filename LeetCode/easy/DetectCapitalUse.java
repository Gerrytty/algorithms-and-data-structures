public class DetectCapitalUse {
    public static void main(String[] args) {
        System.out.println(detectCapitalUse("USA"));
    }

    public static boolean detectCapitalUse(String word) {
        int len = word.length();
        if(len == 1) {
            return true;
        }
        char first_symbol = word.charAt(0);
        char second_symbol = word.charAt(1);
        boolean second_letter = check(second_symbol);
        System.out.println(word.charAt(2));
        for(int i = 1; i < len; i++) {
            if(second_letter != check(word.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    public static boolean check(char c) {
        if(c >= (int)'A' && c <= (int) 'Z') {
            return true;
        }
        return false;
    }
}
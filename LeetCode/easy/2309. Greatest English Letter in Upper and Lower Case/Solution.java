class Solution {
    public String greatestLetter(String s) {
        HashSet<Character> sChars = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            sChars.add(s.charAt(i));
        }

        Iterator<Character> iterator = sChars.iterator();

        char greatest = ' ';

        while (iterator.hasNext()) {

            Character ch = iterator.next();

            if (greatest == 0) {
                greatest = ch;
            }

            char lower = ' ';
            char upper = ' ';

            if ('a' <= ch && ch <= 'z') {
                lower = ch;
                upper = (char) (ch - 32);
            }
            else {
                upper = ch;
                lower = (char) (ch + 32);
            }

            if (sChars.contains(lower) && sChars.contains(upper)) {
                if (greatest != ' ' && greatest < upper) {
                    greatest = upper;
                }
                else if (greatest == ' ') {
                    greatest = upper;
                }
            }

        }

        if (greatest == ' ') {
            return "";
        }

        return "" + greatest;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.greatestLetter("lEeTcOdE"));
    }
}
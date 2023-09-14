package Valid;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                stack.push(s.charAt(i));
            } else {

                if (stack.empty()) {
                    return false;
                }

                Character symbol = stack.pop();

                if (symbol != map.get(s.charAt(i))) {
                    return false;
                }
            }
        }

        return stack.empty();
    }
}

public class Solution {
    public String reversePrefix(String word, char ch) {
        StringBuilder ns = new StringBuilder();
        int f = 0;
        int x = 0;
        if (word.equals(String.valueOf(ch))) {
            return word.substring(0, word.length());
        }
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c != ch && f == 0) {
                ns.insert(0, c);
            } else if (c == ch && f == 0) {
                ns.insert(0, c);
                f = 1;
                x = i;
                break;
            }
        }
        if (f == 0) {
            return word;
        } else {
            ns.append(word.substring(x + 1));
        }
        return ns.toString();
    }
}
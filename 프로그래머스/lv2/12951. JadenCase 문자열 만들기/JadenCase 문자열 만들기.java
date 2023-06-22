import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String tmp = " ";
        for (String str : s.split("")) {
            answer += tmp.equals(" ") ? str.toUpperCase() : str.toLowerCase();
            tmp = str;
        }
        return answer;
    }
}
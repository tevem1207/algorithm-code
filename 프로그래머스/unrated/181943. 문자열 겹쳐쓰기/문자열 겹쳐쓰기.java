class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
            
        for (int i = 0; i < my_string.length(); i++) {
            answer += i >= s && i < s + overwrite_string.length() ? 
                overwrite_string.charAt(i-s) : my_string.charAt(i);
        }
        
        return answer;
    }
}
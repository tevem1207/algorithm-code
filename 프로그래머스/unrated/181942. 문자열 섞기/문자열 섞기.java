class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        for (int i = 0; i < (str1 + str2).length(); i++) {
            answer += i % 2 == 0 ? str1.charAt(i/2) : str2.charAt(i/2);
        }
        return answer;
    }
}
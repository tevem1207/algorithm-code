import java.util.*;

class Solution {
    public long solution(long n) {
        int nLength = String.valueOf(n).length();
        int[] intArr = new int[nLength];
        
        for (int i = 0; i < nLength; i++) {
            intArr[i] = (int) (n % 10);
            n /= 10;
        }
        
        Arrays.sort(intArr);
        
        String answer = "";
        
        for (int i = 0; i < nLength; i++) {
            answer += intArr[nLength - i - 1];
        }

        return Long.parseLong(answer);
    }
}
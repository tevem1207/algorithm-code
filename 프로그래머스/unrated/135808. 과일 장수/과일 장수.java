import java.util.*;


class Solution {
    public int solution(int k, int m, int[] score) {
        int cnt = 0;
        int minVal = 10;
        int answer = 0;
        
        Arrays.sort(score);
        
        for (int i = score.length % m; i < score.length; i++) {
            if (cnt < m) {
                minVal = minVal > score[i] ? score[i] : minVal;
                cnt ++;      
            } 
            
            if (cnt >= m) {
                answer += minVal * m;
                cnt = 0;
                minVal = 10;
            }
        }
        
        return answer;
    }
}
import java.util.*;


class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> al = new ArrayList<>();
        int minNum = Integer.MAX_VALUE;
        
        for (int num : arr) {
            minNum = minNum > num ? num : minNum;
        }
        
        for (int num : arr) {
            if (num != minNum) {
                al.add(num);
            }
        }
        
        if (al.size() == 0) {
            return new int[]{-1};
        } else {
            int[] answer = new int[al.size()];
            for (int i = 0; i < al.size(); i++) {
                answer[i] = al.get(i);
            }
            
            return answer;
        }
    }
}
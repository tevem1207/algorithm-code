import java.util.*;


class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int x = 0;
        Arrays.sort(targets, (i1, i2) -> i1[1] - i2[1]);
        for (int[] target: targets) {
            if (x <= target[0]) {
                x = target[1];
                answer += 1;
            }
        }
        return answer;
    }
}
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (n % 2 == i % 2) {
                if (n % 2 == 1) {
                    answer += i;
                } else {
                    answer += Math.pow(i, 2);
                }
            }
        }
        return answer;
    }
}
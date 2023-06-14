class Solution {
    public double solution(int[] arr) {
        int arraySum = 0;
        for (int num : arr) {
            arraySum += num;
        }
        return (double) arraySum / arr.length;
    }
}
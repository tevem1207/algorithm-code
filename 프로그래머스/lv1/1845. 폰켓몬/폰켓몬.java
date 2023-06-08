import java.util.HashMap;


class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        HashMap<Integer, Integer> pocketMap = new HashMap<>();
        for (int num : nums) {
            pocketMap.put(num, pocketMap.getOrDefault(num, 0) + 1);
        }
        return nums.length / 2 > pocketMap.size() ? pocketMap.size() : nums.length / 2;
    }
}
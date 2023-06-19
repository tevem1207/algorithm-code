class Solution {
    public int solution(int[][] sizes) {
        int rMax = 0;
        int cMax = 0;
        for (int[] size : sizes) {
            rMax = Math.max(rMax, Math.max(size[0], size[1]));
            cMax = Math.max(cMax, Math.min(size[0], size[1]));
        }
        return rMax * cMax;
    }
}
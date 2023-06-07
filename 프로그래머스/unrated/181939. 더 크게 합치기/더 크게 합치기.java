class Solution {
    public int solution(int a, int b) {
        String aa = String.valueOf(a);
        String bb = String.valueOf(b);
        
        return Integer.parseInt(Integer.parseInt(aa.repeat(4).substring(0, 4)) 
                                > Integer.parseInt(bb.repeat(4).substring(0, 4))
                                ? aa + bb : bb + aa);
    }
}
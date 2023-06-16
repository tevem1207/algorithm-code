class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        String strX = String.valueOf(x);
        int total = 0;
        
        for (char s: strX.toCharArray()) {
            total += Character.getNumericValue(s);
        }
        
        return x % total == 0 ? true : false;
    }
}
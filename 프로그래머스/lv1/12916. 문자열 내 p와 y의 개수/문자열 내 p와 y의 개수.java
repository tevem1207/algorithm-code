class Solution {
    boolean solution(String s) {
        
        return s.replaceAll("p", "").replaceAll("P", "").length() - s.replaceAll("y", "").replaceAll("Y", "").length() == 0 ? true : false;
    }
}
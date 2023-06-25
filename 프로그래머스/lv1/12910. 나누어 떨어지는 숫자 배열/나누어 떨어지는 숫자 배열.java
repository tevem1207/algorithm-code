import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> numList = new ArrayList<>();
        Arrays.sort(arr);
        for (int num : arr) {
            if (num % divisor == 0) {
                numList.add(num);
            }
        }
        
        if (numList.size() == 0) {
            int[] empty = {-1};
            return empty;
        } else {
            Integer[] answer = numList.toArray(new Integer[numList.size()]);
            return Arrays.stream(answer).mapToInt(Integer::intValue).toArray();
        }
    }
}
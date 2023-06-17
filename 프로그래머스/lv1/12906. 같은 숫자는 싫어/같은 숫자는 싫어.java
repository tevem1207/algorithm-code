import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        
        for (int num : arr) {
            if (!stack.isEmpty() && stack.peek() == num) {
                stack.pop();
            }
            stack.push(num);
        }
        
        int[] result = new int[stack.size()];
        
        for (int i = 0; i < result.length; i++) {
            result[result.length - i - 1] = stack.pop();
        }

        return result;
    }
}
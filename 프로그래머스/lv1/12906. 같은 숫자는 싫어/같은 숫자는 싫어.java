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
        
        int stackSize = stack.size();
        int[] result = new int[stackSize];
        
        for (int i = 0; i < stackSize; i++) {
            result[stackSize - i - 1] = stack.pop();
        }

        return result;
    }
}
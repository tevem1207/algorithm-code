import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        for (int num : arr) {
            if (!stack.empty()) {
                if (stack.peek() == num) {
                    stack.pop();
                }
            }
            stack.push(num);
        }
        
        Integer[] temp = stack.toArray(new Integer[stack.size()]);
        int[] result = new int[temp.length];
        for (int i = 0; i < temp.length; i++) {
            result[i] = temp[i];
        }

        return result;
    }
}
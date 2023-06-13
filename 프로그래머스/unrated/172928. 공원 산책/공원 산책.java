class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = {0, 0};
        
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[i].length(); j++) {
                if (park[i].charAt(j) == 'S') {
                    answer[1] = j;
                    answer[0] = i;
                }
            }
        }
        
        for (String route : routes) {
            String dir = route.substring(0, 1);
            int[] move = {0, 0};
            int distance = Integer.parseInt(route.substring(2, 3));
            
            if (dir.equals("N")) {
                move[0] = -1;
            } else if (dir.equals("S")) {
                move[0] = 1;
            } else if (dir.equals("W")) {
                move[1] = -1;
            } else if (dir.equals("E")) {
                move[1] = 1;
            }

            
            if (answer[1] + move[1] * distance >= 0 && answer[1] + move[1] * distance < park[0].length() 
                && answer[0] + move[0] * distance >= 0 && answer[0] + move[0] * distance < park.length) {
                boolean flag = true;
                          
                for (int i = 1; i <= distance; i++) {
                    if (park[answer[0] + move[0] * i].charAt(answer[1] + move[1] * i) == 'X') {
                        flag = false;
                    }
                }
                if (flag) {
                    answer[0] += move[0] * distance;
                    answer[1] += move[1] * distance;
                }
            }
        }
        
        return answer;
    }
}
import java.util.ArrayList;

class Solution {
    public int[] solution(int start_num, int end_num) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = start_num; i<=end_num; i++){
            list.add(i);
        }
        
        int[] answer = new int[list.size()];
        
        for (int j=0; j < answer.length; j++) {
            answer[j] = list.get(j);
        }
        
        return answer;
    }
}
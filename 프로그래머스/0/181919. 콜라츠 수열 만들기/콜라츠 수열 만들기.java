import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> list = new ArrayList<>();
        
        int target = n;
        
        while (target != 1) {
            if (target % 2 == 0) {
                list.add(target);
                target = target / 2;
            } else {
                list.add(target);
                target = target * 3 + 1;
            }
        }
        
        list.add(target);
        int[] answer = new int[list.size()];
        
        for (int i = 0; i<list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}
import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = l; i <=r ; i++) {
            String num_str = String.valueOf(i);
            Boolean flag = true;
            
            for (int j = 0; j < num_str.length(); j++) {
                char c = num_str.charAt(j);
                if(c!='0' && c!='5') {
                    flag = false;
                    break;
                }
            }
            if (flag == true) {
                list.add(i);
            }
            
        }
        if(list.isEmpty()) {
                return new int[]{-1};
            } else {
                int[] answer = new int[list.size()];
                for (int t = 0; t<answer.length; t++) {
                    answer[t] = list.get(t);
                }
                return answer;
            }
    }
}
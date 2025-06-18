import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        int i = 0;
        
        while (i < arr.length) {
            if (list.isEmpty()) {
                list.add(arr[i]);
                i++;
            } else {
                if (list.get(list.size()-1) < arr[i]) {
                    list.add(arr[i]);
                    i++;
                } else {
                    list.remove(list.size()-1);
                }
            }
        }
        
        int[] stk = new int[list.size()];
        
        for(int k = 0; k < list.size(); k++) {
            stk[k] = list.get(k);
        }
        
        return stk;
    }
}
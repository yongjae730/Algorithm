import java.util.*;
import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException {
        int asciiCode = System.in.read();
        // 이 메소드는 입력 스트림에서 1바이트(1글자)를 읽어와
        // 그 값에 해당하는 아스키 코드(정수)를 바로 반환

        System.out.println(asciiCode);
    }
}
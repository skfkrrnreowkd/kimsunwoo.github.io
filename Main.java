import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 사용자로부터 숫자를 입력받기 위한 Scanner 객체 생성
        Scanner scanner = new Scanner(System.in);

        // 안내 메시지 출력
        System.out.println("숫자를 입력하세요:");

        // 사용자로부터 숫자 입력받기
        int num = scanner.nextInt();

        // 1부터 입력한 숫자까지의 합 계산
        int sum = 0;
        for (int i = 1; i <= num; i++) {
            sum += i;
        }

        // 결과 출력
        System.out.println("1부터 " + num + "까지의 합은 " + sum + "입니다.");

        // Scanner 객체 닫기
        scanner.close();
    }
}

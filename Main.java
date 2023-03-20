import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 메뉴 출력
        System.out.println("=== Menu ===");
        System.out.println("1. Cheeseburger - $5.00");
        System.out.println("2. Hamburger - $4.00");
        System.out.println("3. French Fries - $2.50");
        System.out.println("4. Soda - $1.50");

        // 주문 받기
        System.out.print("Enter menu number: ");
        int menuNumber = scanner.nextInt();

        // 선택한 메뉴 출력
        System.out.println("You selected menu " + menuNumber + ".");

        // 주문 완료 메시지 출력
        System.out.println("Thank you for your order. Please proceed to the payment terminal.");
    }
}
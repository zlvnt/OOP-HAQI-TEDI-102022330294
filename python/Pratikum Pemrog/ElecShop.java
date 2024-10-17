import java.util.Arrays;
import java.util.Scanner;

public class ElectronicsShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input jumlah uang yang dimiliki
        int uang = scanner.nextInt();

        // Input harga keyboard dan USB
        int n = scanner.nextInt(); // Jumlah jenis keyboard
        int m = scanner.nextInt(); // Jumlah jenis USB
        int[] keyboardPrices = new int[n];
        int[] usbPrices = new int[m];

        // Baca harga keyboard
        for (int i = 0; i < n; i++) {
            keyboardPrices[i] = scanner.nextInt();
        }

        // Baca harga USB drive
        for (int i = 0; i < m; i++) {
            usbPrices[i] = scanner.nextInt();
        }

        int maxSpent = -1; // Maksimal uang yang dapat dihabiskan

        // Loop melalui harga keyboard dan USB drive
        for (int keyboardPrice : keyboardPrices) {
            for (int usbPrice : usbPrices) {
                int totalSpent = keyboardPrice + usbPrice;

                // Periksa apakah uang cukup dan perbandingan dengan maxSpent
                if (totalSpent <= uang && totalSpent > maxSpent) {
                    maxSpent = totalSpent;
                }
            }
        }

        System.out.println(maxSpent);

        scanner.close();
    }
}

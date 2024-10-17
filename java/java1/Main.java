import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        vt inventaris = new vt();
        Scanner scanner = new Scanner(System.in);
        int pilihan;
        do {
            System.out.println("===== Menu Inventaris Makanan EAD =====");
            System.out.println("1. Tambah Makanan Kering");
            System.out.println("2. Tambah Makanan Basah");
            System.out.println("3. Tampilkan Semua Makanan");
            System.out.println("4. Keluar");
            System.out.print("Pilih menu: ");
            pilihan = scanner.nextInt();
            scanner.nextLine();
            switch (pilihan) {
                case 1:
                    inventaris.tambahMakananKering();
                    break;
                
                case 2:
                    inventaris.tambahMakananBasah();
                    break;
                
                case 3:
                    inventaris.tampilkanSemuaMakanan();
                    break;

                case 4:
                    System.out.println("Keluar dari program.");
                    break;

                default:
                    System.out.println("Pilihan tidak valid, silahkan coba lagi!");    
            }
        } while (pilihan != 4);
        scanner.close();
    }
}

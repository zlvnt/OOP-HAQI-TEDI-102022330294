import java.util.ArrayList;
import java.util.Scanner;

public class vt {
    
    private ArrayList<km> daftarMakananKering = new ArrayList<>();
    private ArrayList<bmm> daftarMakananBasah = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);

    public void tambahMakananKering(){
        System.out.print("Masukkan Nama Makanan: ");
        String nama = scanner.nextLine();
        System.out.print("Masukkan Jumlah Makanan: ");
        int jumlah = scanner.nextInt();
        System.out.print("Masukkan Harga Makanan: ");
        double harga = scanner.nextDouble();
        scanner.nextLine(); 
        System.out.print("Masukkan Brand Makanan: ");
        String brand = scanner.nextLine();

        km makananKering = new km(nama, jumlah, harga, brand);
        daftarMakananKering.add(makananKering);

        System.out.println("===============================");
        System.out.println("Makanan Kering Berhasil ditambahkan!");
    }

    public void tambahMakananBasah(){
        System.out.print("Masukkan Nama Makanan: ");
        String nama = scanner.nextLine();
        System.out.print("Masukkan Jumlah Makanan: ");
        int jumlah = scanner.nextInt();
        System.out.print("Masukkan Harga Makanan: ");
        double harga = scanner.nextDouble();
        scanner.nextLine();
        System.out.print("Masukkan Bahan Makanan: ");
        String basah = scanner.nextLine();

        bmm makananBasah = new bmm(nama, jumlah, harga, basah);
        daftarMakananBasah.add(makananBasah);

        System.out.println("===============================");
        System.out.println("Makanan Basah Berhasil ditambahkan!");
        System.out.println();
    }

    public void tampilkanSemuaMakanan(){
        System.out.println("===============================");
        if (daftarMakananKering.isEmpty() && daftarMakananBasah.isEmpty()){
            System.out.println("Tidak ada Makanan dalam Inventaris.");
        } else{
            for(km makananKering : daftarMakananKering) {
                makananKering.tampilkanData();
                System.out.println("===============================");
            }
            for(bmm makananBasah : daftarMakananBasah) {
                makananBasah.tampilkanData();
                System.out.println("===============================");
                System.out.println();
            }
        }
    }
}

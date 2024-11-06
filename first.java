import java.util.Scanner;

public class first {
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        String name=sc.nextLine();
        int age=sc.nextInt();
        sc.nextLine();
        String address=sc.nextLine(); 

        System.out.println(name);
        System.out.println(age);
        System.out.println(address);
    }
}
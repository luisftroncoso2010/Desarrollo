import java.util.Scanner;
public class practica {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

    System.out.println("Por favor ingrese su nombre: ");
    String nombre = scanner.nextLine();
    System.out.println("Su nombre es: "+ nombre.toUpperCase()); //Convertimos a mayusculas

    scanner.close();
    
    }
}

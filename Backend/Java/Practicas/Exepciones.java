package Backend.Java.Practicas;


import java.util.InputMismatchException;
import java.util.Scanner;


class Exepciones {
    public static void main(String[] args) {
        // Declaramos el Scaner y las variables
        Scanner scanner = new Scanner(System.in);
        int numUno, numDos, division;


        // Colocamos un mensaje para aludir al primer y segundo numero
        System.out.println("Por favor coloca un numero de tipo entero: ");
        numUno = scanner.nextInt();
        System.out.println("Divisor. Coloca un valor entero: ");
        // Cremamos la operacion que queremos hacer y mostrar
        numDos = scanner.nextInt();



        while (!scanner.hasNextInt()){
            System.err.println("NOTA:\n- No puedes colocar otro valor que no sea de tipo entero.\n- No puedes dividir por cero. Por favor, ingresa un divisor diferente de cero.");
            // Colocamos un mensaje para aludir al primer y segundo numero
            System.out.println("Por favor coloca un numero de tipo entero: ");
            numUno = scanner.nextInt();
            System.out.println("Divisor. Coloca un valor entero: ");
            // Cremamos la operacion que queremos hacer y mostrar
            numDos = scanner.nextInt();
            scanner.close();
        }

        try {
            division = numUno / numDos;
            System.out.println("El resultado es: " + division);
        }
        catch (InputMismatchException exception){
            System.err.println("Error. Se esperaba un numero entero");
        }
        catch (ArithmeticException exception) {  // Aca Se coloca la excepcion por parametro. El tipo y la ex
            System.err.println("Error aritmético: " + exception.getMessage());
        }
        finally {
            scanner.close();
        }

    
    }
}

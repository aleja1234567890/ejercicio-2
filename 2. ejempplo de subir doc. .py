 import java.util.Scanner;
public class Reto1 {
    public static void main(String[] args) {
        //crear un objeto tipo scanner para introducir valores por teclado
        Scanner sc = new Scanner(System.in);
        //declaración de variables
        long numeroCuenta;
        String fechaApertura;
        int tipoCuenta,N;
        double saldoCuenta,valorInteres,totalIntereses=0,totalSaldos=0;
        N=sc.nextInt();
        for(int i=0;i<N;i++){
            numeroCuenta=sc.nextLong();
            fechaApertura=sc.next();
            tipoCuenta=sc.nextInt();
            saldoCuenta=sc.nextDouble();
            switch(tipoCuenta){
                case 1: valorInteres=saldoCuenta*1.5/100;break;
                case 2: valorInteres=saldoCuenta*1.7/100;break;
                case 3: valorInteres=saldoCuenta*1.6/100;break;
                default:valorInteres=0;
            }
            saldoCuenta+=valorInteres;
            totalIntereses+=valorInteres;
            totalSaldos+=saldoCuenta;
            System.out.println(numeroCuenta);
            System.out.println(valorInteres);
            System.out.println(saldoCuenta);
        }
        System.out.println(totalIntereses);
        System.out.println(totalSaldos);
    }
}







import java.util.Scanner;
class App {
    public static void main(String[] args) {
        System.out.println("-----------------------------------------------------------");
        System.out.print("Tapez le nombre de secondes: ");

        int nombreDeSec = (new Scanner(System.in)).nextInt();

        System.out.println( (nombreDeSec / 60) / 60 +" Heures " + (nombreDeSec - (nombreDeSec / 60) / 60 * 60 * 60) / 60 +" Minutes "+ ((nombreDeSec - (nombreDeSec / 60) / 60 * 60 * 60) - ((nombreDeSec - (nombreDeSec / 60) / 60 * 60 * 60) / 60 * 60)) + " secondes ");

        System.out.println("-----------------------------------------------------------");
    }
}
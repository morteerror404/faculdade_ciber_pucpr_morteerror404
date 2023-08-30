import java.util.Scanner;
public class form1{
    public static final double PI = 3.14159;

public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);
    
    System.out.print("Exercicio 1");

    System.out.println("Digite o valor do raio de um circulo:");

    double raio = sc.nextDouble();
    
    double resultado = PI * (raio * raio);

    System.out.printf("A área do seu círculo é igual a %2f", resultado);

    int contador = 1;

    System.out.print("Exercicio 2");


    while(contador == 10){
        contador = contador + 1;
        System.out.println(contador);

    }

    System.out.print("Exercicio 3");

    for(int soma = 0; soma <= 10; soma++){
        System.out.print(soma);
    }

    System.out.print("Exercicio 4");

    System.out.println("Digite um numero:");

    int limite = sc.nextInt();

    for(int i = 0;  i<= limite; i ++){
        System.out.print(i);
    }

    System.out.print("Exercicio 5");

    System.out.println("Digite um numero:");

    int limite2 = sc.nextInt();

    for(int j = 0; j<= limite2; j ++){
        if(j % 2 == 0){
            System.out.print(j);
        }
    }

    System.out.print("Exercicio 6");

    System.out.print("Digite uma senha:");

    String senha = sc.nextLine();

    if(senha == "12345"){
        System.out.printf("Acesso concedido");

    }else{
        System.out.printf("Acesso negado");

    }

    System.out.print("Exercicio 7");

    int idade_minima = 18;

    System.out.printf("Digite sua idade:");

    int idade =  sc.nextInt();
    
    if (idade >=  idade_minima){
        System.out.print("você é maior de idade");
    }else{
        System.out.print("você é menor de idade");
    }

    System.out.print("Exercicio 8");

    System.out.print("Digite um numero:");

    int limite3 = sc.nextInt();
    int k = 0;
    int resultado2 = 0;

    while( k < limite3){
        k++;
        resultado2 = resultado2 * k;
        System.out.print(k);
    }
        System.out.printf("resultado: %2f", resultado2);

    System.out.print("Exercicio 9");

    

    sc.close();

}}
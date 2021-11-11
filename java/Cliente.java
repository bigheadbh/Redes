package java;
import java.net.*;
import java.io.*;
import java.util.Date;

public class Cliente{
    public static void main ( String [] args ) {
        try {
            Socket cliente = new Socket ("127.0.0.1", 12345) ;
            ObjectInputStream entrada = new ObjectInputStream(cliente.getInputStream());
            Date data_atual = (Date)entrada.readObject();
            System.out.println("Data recebida do servidor :" + data_atual.toString());
            entrada.close();
            System.out.println("Conexao encerrada");
        }
        catch(Exception e) {
            System.out.println("Erro :" + e.getMessage());
        }
    }
}

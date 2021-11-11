package java;
import java.net.*;
import java.io.*;
import java.util.Date;


public class Servidor{
    public static void main ( String [] args ) {
        try {
            // Instancia o ServerSocket ouvindo a porta 12345
            ServerSocket servidor = new ServerSocket (12345);
            System.out.println("Servidor ouvindo a porta 12345");
            while(true) {
                // o metodo accept () bloqueia a execucao ate que
                // o servidor receba um pedido de conexao
                Socket cliente = servidor.accept();
                System.out.println("Cliente conectado : " + cliente.getInetAddress().getHostAddress());
                ObjectOutputStream saida = new ObjectOutputStream(cliente.getOutputStream());
                saida.flush();
                saida.writeObject(new Date());
                saida.close();
                cliente.close();
            }
            
        }
        catch(Exception e) {
            System.out.println("Erro : " + e.getMessage());
        }
        finally {
        }
    }
}

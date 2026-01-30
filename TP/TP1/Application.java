import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.println("debut de deploiement de mon service");
        String url="http://localhost:8888/" ;// addresse qui sera utiliser pour publier mon service (chaine de car)
        Endpoint.publish(url, new MonserviceWeb());// méthode pour publier notre service qui prend deux parametre(adrresse et instance de service à publier)
        System.out.println("Le service Web est déployé !"); // tester si ça marche en running le code
    }// lancer sur votre navigateur localhost:8888/?wsdl and keep running ur code ( wsdl web service language defintion) tu dois expliquer les elements
}

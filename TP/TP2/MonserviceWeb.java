// SOAP : Simple Object Acess Protocol......
//JAX-WS : Java Annotation XML for Web Service (c'est une annoation  sont basé sur les annotation JAXB)
//JAXB: Java Architecture XML Building( permettent serialisation et la deserialisation prends un object en java et le transformer en java et vice versa)
// URL : Uniform Resource Locator ( chaine de car utilser pour acceder aux resource aux info en utilisation l'adresse de l'emplacement de la resource
// URN :Uniform Resource Name ( fournit des info sur  la resource elle meme)
// URI :Uniform Resource Identifier ( méthode standard pour identifier les info par leurs nom , leur emplacement ou les deux à la fois
// URN+URL=URI



import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

// pour que cette classe soit un service WEB on doit utiliser une seule annotaion obligatoire notamment tt en présisant le targetNamespace qui sert à distinguer quand on est à l'extérieur de quel service on parle si on a deux class portant le meme nom de service pour les distinguer de l'éxterieur faut juste préciser le repertoire ou elles sont sauvegarder
@WebService(targetNamespace ="http//www.universiteParisNord.fr" )
public class MonserviceWeb {
    @WebMethod(operationName = "convertir")    // pour changer le nom des méthodes

    public double conversion(double mt){
        return mt*0.9;// methode simple qui prend un reel et le multiplie par 0.9 et renvoie le resultat
    }
    public double somme(@WebParam(name="parametre1")double a, double b){// @WebParam(name="parametre1") c'est pour changer le nom des parametres de arg1 arg 2 à des noms bien reconnue par le client
        return a+b;
    }
     public Etudiant getEtudiant(int identifiant){// méthode qui renvoie un objet de type etudiant
        return new Etudiant(1, "Thom", 19);
     }
// juste après deployer ton app
}

using System;
using System.Collections.Generic;
namespace CadastroA
{
    public class Contato
    {
        private String nome;
        private String dataNasc;
        private String cpf;
        private String rg;
        private String celular;
        private String email;
        private String endereco;
        public List<Contato> list = new List<Contato>();
        
        // Constructor
        public Contato(String nome, String dataNasc, String cpf, String rg, String celular, String email, String endereco){
            this.Nome=nome;
            this.DataNasc=dataNasc;
            this.CPF=cpf;
            this.RG=rg;
            this.Celular=celular;
            this.Email=email;
            this.Endereco=endereco;
        }
        public Contato(){}

        // Methods
        public void AdicionaDados(){
            list.Add(new Contato(this.Nome, this.DataNasc, this.CPF, this.RG, this.Celular, this.Email,this.Endereco));
        }
        public void AdicionaDados(Contato contato){
            list.Add(contato);
        }

        //Getters and Setters
        public String Nome{
            get{return nome;}
            set{nome=value;}
        }
        public String DataNasc{
            get{return dataNasc;}
            set{dataNasc=value;}
        }
        public String CPF{
            get{return cpf;}
            set{cpf=value;}
        }
        public String RG{
            get{return rg;}
            set{rg=value;}
        }
        public String Celular{
            get{return celular;}
            set{celular=value;}
        }
        public String Email{
            get{return email;}
            set{email=value;}
        }
        public String Endereco{
            get{return endereco;}
            set{endereco=value;}
        }
        // public List<Cadastro> LIST{
        //     get{return list;}
        //     set{}
        // }

        // public void ImprimeNaTela(){
        //     Console.WriteLine(list.);
        // }
    }

    class principal
    {
        static void Main(string[] args)
        {
            
            Contato ca = new Contato("Fernando","28/11/2000","000.000","00.00", "62", "@gmail", "Rua A");
            Contato cb = new Contato("Amanda","26/06/2000","000.000","00.00", "62", "@gmail", "Rua A");
            ca.AdicionaDados();
            cb.AdicionaDados();

            Console.WriteLine(ca.list.Nome);

            // Console.WriteLine(ca.ImprimeNaTela());
            // Console.WriteLine(cb.ImprimeNaTela());
            // Console.WriteLine("\n");
            // Console.WriteLine(ca);
            

            // foreach (var a in ca.list)
            // {
            //     Console.WriteLine(a.toString);
            // }
            
        }
    }
}
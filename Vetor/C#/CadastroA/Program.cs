using System;
using System.Collections.Generic;

namespace CadastroA
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Contato ca = new Contato("Fernando","28/11/2000","000.000","00.00", "62", "@gmail", "Rua A");
            Contato cb = new Contato("Amanda","26/06/2000","000.000","00.00", "62", "@gmail", "Rua A");
            ca.AdicionaDados();
            cb.AdicionaDados();

            Console.WriteLine(ca.lis);

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

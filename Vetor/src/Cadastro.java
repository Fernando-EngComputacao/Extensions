import javax.swing.*;
import java.util.ArrayList;

public class Cadastro implements InterfaceCadastro{
    ArrayList<Contato> list = new ArrayList<Contato>();

    @Override
    public void AdicionaContato(Contato contato) {
        list.add(contato);
    }
    public void AdicionaContato(){
        list.add(Dados());
    }
    public Contato Dados(){
        String nm, dn, tf, cp, rg, em, en;
        nm = JOptionPane.showInputDialog("Nome do Contato: ");
        dn = JOptionPane.showInputDialog("Data de Nascimento do Contato: ");
        tf = JOptionPane.showInputDialog("Telefone do Contato: ");
        rg = JOptionPane.showInputDialog("RG do Contato");
        cp = JOptionPane.showInputDialog("CPF do Contato");
        em = JOptionPane.showInputDialog("Email do Contato");
        en = JOptionPane.showInputDialog("Enderçoo do Contato");
        JOptionPane.showMessageDialog(null,"Você Adicionou um novo contato: \n\nREFERENTE AO(À): "+nm);
        return new Contato(nm, dn, cp, rg, tf, em, en);
    }

    @Override
    public Integer ConfirmaDados(){
        String text = "--- CADASTRO DE CONTATOS ----\n";
        text += "Escolha uma opção para continuar!\n";
        text += "1-Ler Contato em específico;\n";
        text += "2-Ler todos os contatos salvos;\n";
        text += "3-Inserir novo contato;\n4-Editar contato;\n";
        text += "5-Excluir contato;\n6-Terminar sessão.";

        return Integer.parseInt(JOptionPane.showInputDialog(text));
    }

    @Override
    public void ConfirmaDados(String aux){
        JOptionPane.showMessageDialog(null, aux);
    }

    @Override
    public void LeDados(Integer id) {
        String text = "Contato ["+id+"]\nNome: "+list.get(id).getNome()+",\nDataNasc: "+list.get(id).getDataNasc();
        text += ",\nCPF: "+list.get(id).getCpf()+", \nRG: "+list.get(id).getRg()+", \nTelefone: "+list.get(id).getTelefone();
        text += ", \nEmail: "+list.get(id).getEmail()+", \nEndereço: "+list.get(id).getEndereco();

        JOptionPane.showMessageDialog(null, text);
    }

    @Override
    public void AlteraDados(Integer id, Contato contato) {
        list.set(id, contato);
        JOptionPane.showMessageDialog(null, "Você alterou o contato de ID ["+id+"]");
    }

    @Override
    public void ExcluiDados(Integer id) {
        list.remove(list.get(id));
        JOptionPane.showMessageDialog(null, "Você excluiu o contato de ID ["+id+"]");
    }
    // toString() - Imprimir na Tela
    @Override
    public void ImprimirNaTela(){
        String aux = "\n*** CONTATOS EXISTENTES ***\n";
        if (list.size()==0){
            JOptionPane.showMessageDialog(null,"Lista de Contatos Vazia.");
        } else {
            for (int i=0; i<list.size(); i++){
                aux += "\n-> CONTATO ID ["+i+"]\nNome: "+ list.get(i).getNome();
                aux += "\nData de Nascimento: "+list.get(i).getDataNasc();
                aux +="\nCPF: "+list.get(i).getCpf()+"\nRG: "+list.get(i).getRg();
                aux += "\nTelefone: "+list.get(i).getTelefone()+"\nEndereço: "+list.get(i).getEndereco()+"\n";

            }
            ConfirmaDados(aux);
        }
    }
}

import javax.swing.*;
import java.util.ArrayList;

public class Contato implements InterfaceContato {
    private Integer id = 0;
    private String nome;
    private String dataNasc;
    private String cpf;
    private String rg;
    private String telefone;
    private String email;
    private String endereco;

    //Constructor
    public Contato(String nome, String dataNasc, String cpf, String rg, String telefone, String email, String endereco) {
        this.id++;
        this.nome = nome;
        this.dataNasc = dataNasc;
        this.cpf = cpf;
        this.rg = rg;
        this.telefone = telefone;
        this.email = email;
        this.endereco = endereco;
    }

    public Contato(){
        this.id++;
        this.nome = JOptionPane.showInputDialog("Nome: ");
        this.dataNasc = JOptionPane.showInputDialog("Data de Nascimento: ");
        this.cpf = JOptionPane.showInputDialog("CPF: ");
        this.rg = JOptionPane.showInputDialog("RG: ");
        this.telefone = JOptionPane.showInputDialog("Celular: ");
        this.email = JOptionPane.showInputDialog("Email: ");
        this.endereco = JOptionPane.showInputDialog("Endereço: ");
    }

    // Setters and Getters
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDataNasc() {
        return dataNasc;
    }

    public void setDataNasc(String dataNasc) {
        this.dataNasc = dataNasc;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getRg() {
        return rg;
    }

    public void setRg(String rg) {
        this.rg = rg;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
}

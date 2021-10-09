public interface InterfaceCadastro {
    void AdicionaContato(Contato contato);
    void LeDados(Integer id);
    void AlteraDados(Integer id, Contato contato);
    void ExcluiDados(Integer id);
    void ImprimirNaTela();
    Integer ConfirmaDados();
    void ConfirmaDados(String aux);
}

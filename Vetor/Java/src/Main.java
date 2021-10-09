import javax.swing.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Objeto Cadastro
        Cadastro cd = new Cadastro();



        Integer inicial = -1;

        while (inicial != 6){
            try {
                inicial = cd.ConfirmaDados();
                if (inicial < 1 || inicial > 6) {
                    cd.ConfirmaDados("\n\nVALOR INVÁLIDO, TENTE OUTRO.");
                }
                else if (inicial == 1){
                    try {
                        cd.LeDados(Integer.parseInt(JOptionPane.showInputDialog("Digite um ID de Contato.")));
                    } catch (Exception e){
                        JOptionPane.showMessageDialog(null, "Digite um ID válido!");
                    }
                }
                else if (inicial == 2){
                    cd.ImprimirNaTela();
                }
                else if (inicial == 3){
                    try {
                       cd.AdicionaContato();
                    }
                    catch (Exception e){
                        JOptionPane.showMessageDialog(null, "Digite um valor numérico.");
                    }
                } else if (inicial == 4){
                    try {
                        Integer a = Integer.parseInt(JOptionPane.showInputDialog("Insira o ID do Contato a ser Alterado!"));
                        Contato c = cd.Dados();
                        cd.AlteraDados(a, c);
                    } catch (Exception e){
                        JOptionPane.showMessageDialog(null, "Digite um valor numérico.");
                    }
                }
                else if (inicial == 5) {
                    try {
                        Integer a = Integer.parseInt(JOptionPane.showInputDialog("Digite o ID do Contato a ser Excluirdo."));
                        if (a > cd.list.size() || a < 0){
                            JOptionPane.showMessageDialog(null, "Digite um ID válido!");
                        } else
                            cd.ExcluiDados(a);
                    } catch (Exception e){
                    JOptionPane.showMessageDialog(null, "Digite um valor numérico.");
                    }
                } else
                    inicial = 6;
            } catch (Exception e){
                JOptionPane.showMessageDialog(null, "Digite um Valor Numérico!");
            }

        }


    }
}

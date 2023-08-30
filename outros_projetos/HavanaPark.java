import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.UIManager;
import javax.swing.plaf.ColorUIResource;

import java.awt.Color;
import java.awt.FlowLayout;

public class HavanaPark {

    public static void main(String[] args) {
        // Criar a janela
        JFrame janela = new JFrame("Minha Janela Swing");

        // Definir a cor vermelha para o botão de menu
        UIManager.put("Menu.background", new ColorUIResource(Color.RED));
        UIManager.put("Menu.foreground", new ColorUIResource(Color.WHITE));

        // Criar a barra de menu
        JMenuBar menuBar = new JMenuBar();

        // Criar o menu
        JMenu menu = new JMenu("Menu");

        // Criar um item de menu
        JMenuItem item = new JMenuItem("Item de Menu");

        // Adicionar o item de menu ao menu
        menu.add(item);

        // Adicionar o menu à barra de menu
        menuBar.add(menu);

        // Definir a barra de menu na janela
        janela.setJMenuBar(menuBar);

        // Criar o painel para a barra de pesquisa e o contador de vagas
        JPanel painelPesquisa = new JPanel();
        painelPesquisa.setLayout(new FlowLayout(FlowLayout.LEFT));
        painelPesquisa.setBackground(Color.RED);

        // Criar a barra de pesquisa
        JTextField campoPesquisa = new JTextField(15);

        // Adicionar a barra de pesquisa ao painel
        painelPesquisa.add(campoPesquisa);

        // Criar o contador de vagas
        JLabel contadorVagas = new JLabel("Vagas: 10");

        // Adicionar o contador de vagas ao painel
        painelPesquisa.add(contadorVagas);

        // Adicionar o painel de pesquisa à barra de menu
        menuBar.add(painelPesquisa);

        // Definir o tamanho da janela
        janela.setSize(400, 300);

        // Definir o comportamento de fechamento da janela
        janela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Tornar a janela visível
        janela.setVisible(true);
    }
}

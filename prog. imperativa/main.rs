// this document belongs to Joao Pedro Ferrira Frota, class U 2nd period of Cybersecurity

use std::io;

fn input(variable: &mut String) {
    io::stdin().read_line(variable)
        .expect("Falha ao ler a linha");
    variable.trim();
}

fn str_to_number(input: &str) -> f32 {
    input.trim().parse()
        .expect("Erro de conversão para número")
}

fn main() {
    let mut resposta = String::new();

    println!("Digite algo:");
    input(&mut resposta);

    let numero: f32 = str_to_number(&resposta);
    println!("Número digitado: {}", numero);
}

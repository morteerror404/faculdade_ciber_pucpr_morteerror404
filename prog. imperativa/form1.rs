std::io;

fn main(){

    let mut idade: String = String:: new();
    let idade_minima = 18;

    print!("digite sua idade: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(& mut idade).unwrap();
        .expect("flaha na entrada")
    
    match idade.parse::<i32>(){
        Ok(idade) =>{
            print!("numero valido")
        }Err(idade) =>{
            print!("numero invalido")
        }
    }

    if idade => idade_minima{
        print!("maior de idade")
    }else{
        print!("menor de idade")
    }

}

let login = "danilo";
let senha = "chocolate123";

let loginUser;
let senhaUser;

loginUser = prompt("Qual é o seu login?");

if (loginUser == login){
    senhaUser = prompt("Qual é a sua senha?")
    if(senhaUser == senha){
        alert("Você conseguiu entrar, seja bem vindo "+login);
    }
    else{
        alert("Senha incorreta :(");
    }
}
else{
    alert("Login incorreto :(");
}
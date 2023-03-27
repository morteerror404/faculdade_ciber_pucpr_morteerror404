#importar o pyrebase4 no pip
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAzC3bihZLaBY3p1QyA97bUKIJnHmkPgJg",
    "authDomain": "atividade-experiencia-criativa.firebaseapp.com",
    "projectId": "atividade-experiencia-criativa",
    "databaseURL": "",
    "storageBucket": "atividade-experiencia-criativa.appspot.com",
    "messagingSenderId": "362834039422",
    "appId": "1:362834039422:web:759f8efc4d8255b0857e2f",
    "measurementId": ""

}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user,password)
print("Resultado: ", status)




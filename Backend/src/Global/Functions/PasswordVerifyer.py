def emailVerifier(password:str,passwordConfirm:str):
    try:
        if not password or not password:
            return {
                "Message":"The password is null",
                "pass":False
            }
        
        elif password!=passwordConfirm:
            return {
                "Message":"The password don't match",
                "pass":False
            }
        
        elif len(password)>6: #precisa conter 6 caracters
            return {
                "Message":"Your password haven't 6 caracters",
                "pass":False
            }
        
        elif password.upper()==password: #precisa conter caracteres maiúsculos e minúsculos
            return {
                "Message":"Your password need to have uppercase letters and not uppercase letters",
                "pass":False
            }
        
        elif password.isdigit() or password.isalpha(): # precisa conter letras e numeros
            return {
                "Message":"Your password need to have numbers and letters",
                "pass":False
            }
        
        else:
            return {
                "Message":"Verified successfully",
                "pass":True
            }
    except:
        return {
            "Message":"Internal Error",
            "pass":False
        }
while True:
    print(emailVerifier(input()))
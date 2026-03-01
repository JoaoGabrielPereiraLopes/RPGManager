def emailVerifier(password:str,passwordConfirm:str):
    try:
        if not password or not password:
            return {
                "Message":"The password is null",
                "Success":False
            }
        
        elif password!=passwordConfirm:
            return {
                "Message":"The password don't match",
                "Success":False
            }
        
        elif len(password)>6:
            return {
                "Message":"Your password haven't 6 caracters",
                "Success":False
            }
        
        elif password.upper()==password:
            return {
                "Message":"Your password need to have uppercase letters and not uppercase letters",
                "Success":False
            }
        
        elif password.isdigit() or password.isalpha():
            return {
                "Message":"Your password need to have numbers and letters",
                "Success":False
            }
        
        return {
            "Message":"Password verified successfully",
            "Success":True
        }
    except:
        return {
            "Message":"Internal Error",
            "Success":False
        }
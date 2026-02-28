def emailVerifier(email:str):
    try:
        if not email:
            return False
        
        Location=email.split("@")
        if not Location or len(Location)!=2:
            print("Errou por falta de @")
            return False
        
        extension=email.split(".")
        if not extension or len(extension)<2:
            print("Errou por falta de .")
            return False
        
        return True
    except:
        return False
while True:
    print(emailVerifier(input()))
def emailVerifier(email:str):
    try:
        if not email:
            return {
                "Message":"Email is null",
                "Success":False
            }
        
        Location=email.split("@")
        if not Location or len(Location)!=2:
            return {
                "Message":"Your email needs to include a domain",
                "Success":False
            }
        
        extension=email.split(".")
        if not extension or len(extension)<2:
            return {
                "Message":"Your email needs to include a domain extension",
                "Success":False
            }
        
        return {
            "Message":"Email verified successfully",
            "Success":True
        }
    
    except:
        return {
            "Message":"Internal Error",
            "Success":False
        }
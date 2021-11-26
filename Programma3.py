def nameandage():
    print("om te stopen type stop")
    name= input("what is your name?")
    if name =="stop":
        quit()
    leeftijd= int(input("how old are you?"))
    if leeftijd =="stop":
        quit()

    print(name,leeftijd)
while True:
    nameandage()

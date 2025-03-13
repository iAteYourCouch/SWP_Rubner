def myFunction(schüler, alter, *args ,**kwargs):
    print(schüler)
    print(alter)
    print(args)
    print(kwargs)

myFunction("Sebastian Karamatic", 19, "Wirtschaft", **{"Jahrgang": 5})
myFunction("Matilda Musterfrau", 19, *("Biomedizin", ))
myFunction("Claudia Jungl", 25, *("Wirtschaft, Maschinenbau",))
myFunction("Sabo Rubner", 47, **{"Jahrgang": 5})

#kaputt
#myFunction("Sebastian Karamatic", "Wirtschaft", **{"alter": 5})
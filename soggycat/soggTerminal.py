import webbrowser
class vars:
    cmdop=True
    oson=True
    i="f"
    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
def sc():
    def comd(object):    
        if "-exit" in object:
            vars.cmdop=False
            print("exiting cli..")
        elif "echo" in object:
            print(object.replace("echo", ""))
        elif "opn" in object:
            if "-w" in object:
                repl1 = object.replace("-w", "")
                repl1 = repl1.replace("opn", "")
                print(repl1)
                webbrowser.open(repl1)
        elif "soggycat" in object:
            if "-off" in object:
                print("Turning off OS..")
                vars.oson=False
            elif "-change" in object:
                if "-var" in object:
                    if "i" in object:
                        vars.i = str(object.replace("soggycat", "") + object.replace("-change", "") + object.replace("-var", "") + object.replace("i", ""))
                    elif "oson" in object:
                        vars.oson = bool(str(object.replace("soggycat", "") + object.replace("-change", "") + object.replace("-var", "") + object.replace("oson", "")))
                    elif "cmdop" in object:    
                        vars.cmdop = bool(str(object.replace("soggycat", "") + object.replace("-change", "") + object.replace("-var", "") + object.replace("cmdop", "")))
            elif "-var" in object:
                if "i" in object:
                    print(vars.i)
                elif "oson" in object:
                    print(vars.oson)
                if "cmdop" in object:
                    print(vars.cmdop)
            else:
                print(vars.BLUE, "Be carefull when dealing with soggycat commands! you can literally change the code in the os!", vars.RESET)
        else:
            print("obj:", object, "not recognized")
    while vars.i=="f": 
        if vars.oson == True:
            if vars.cmdop == True:
                cmd = input("soggycat > ")
                comd(cmd)
            elif vars.cmdop == False:
                vars.cmdop = False
        else:
            vars.i="s"
sc()

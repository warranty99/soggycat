import webbrowser #SOGGY CAT BEST OS!! HUZZAHH
class Vars:
    cmdop=True
    oson=True
    i="f"
    RED="\033[91m"
    GREEN="\033[92m"
    BLUE="\033[94m"
    RESET="\033[0m"
    SystemSCName="soggycat"
def sc():
    def comd(object):    
        if "-exit" in object:
            Vars.cmdop=False
            print("exiting cli..")
        elif "echo" in object:
            print(object.replace("echo", ""))
        elif "opn" in object:
            if "-w" in object:
                repl1=object.replace("-w", "")
                repl1=repl1.replace("opn", "")
                print(repl1)
                webbrowser.open(repl1)
        elif "soggycat" in object:
            if "-off" in object:
                print("Turning off OS..")
                Vars.oson=False
            elif "-change" in object:
                if "-var" in object:
                    if "i" in object:
                        Vars.i=str(object.replace("soggycat", "")+object.replace("-change", "")+object.replace("-var", "")+object.replace("i", ""))
                    elif "oson" in object:
                        Vars.oson=bool(str(object.replace("soggycat", "")+object.replace("-change", "")+object.replace("-var", "")+object.replace("oson", "")))
                    elif "cmdop" in object:    
                        Vars.cmdop=bool(str(object.replace("soggycat", "")+object.replace("-change", "")+object.replace("-var", "")+object.replace("cmdop", "")))
                    elif "SystemSCName" in object:
                        systemnamedchanged=object.replace("soggycat", "")
                        systemnamedchanged=systemnamedchanged.replace("-change", "")
                        systemnamedchanged=systemnamedchanged.replace("-name", "")
                        systemnamedchanged=systemnamedchanged.replace(" ", "")
                        print("WARNING! Changing the system name can have weird, and i mean WEIRD side effects on the terminal, YOU WANTED THIS!")
                elif "-name" in object:
                    systemnamedchanged=object.replace("soggycat", "")
                    systemnamedchanged=systemnamedchanged.replace("-change", "")
                    systemnamedchanged=systemnamedchanged.replace("-name", "")
                    systemnamedchanged=systemnamedchanged.replace(" ", "")
                    print("WARNING! Changing the system name can have weird, and i mean WEIRD side effects on the terminal, YOU WANTED THIS!")
                    Vars.SystemSCName=str(systemnamedchanged)
            elif "-var" in object:
                dashvar=object.replace("soggycat", "")
                dashvar=dashvar.replace("-var", "")
                dashvar=dashvar.replace(" ", "")
                print(getattr(Vars, dashvar))
            elif "-info" in object:
                print("Running Soggycat >1.0.0")
            else:
                print(Vars.BLUE, "Be carefull when dealing with soggycat commands! you can literally change the code in the os!", Vars.RESET)
        else:
            print("obj:", object, "not recognized")
    while Vars.i=="f":
        if Vars.oson:
            if Vars.cmdop:
                cmd = input(Vars.SystemSCName+" >")
                comd(cmd)
            else:
                Vars.cmdop=False
        else:
            Vars.i="s"
sc()

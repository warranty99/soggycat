import webbrowser #SOGGYCAT BEST LANGUAGE!!
import re
class Vars:
    cmdop=True
    oson=True
    i="f"
    RED="\033[91m"
    GREEN="\033[92m"
    BLUE="\033[94m"   
    RESET="\033[0m"
    SystemSCName="soggycat"
    sogclpattern = r'<(.*?)>'
    sogclpattern2 = r'\.start(.*?)(?=\.end)'
    usrCreatedVars = {'placeholder': '0'}

def sc():
    def sogcl(code):
        matches = re.findall(Vars.sogclpattern, code)
        statements = []
        for match in matches:
            statements.extend(re.findall(Vars.sogclpattern2, match))
        for statement in statements:
            comd(statement)
    def comd(object):    
        if "-exit" in object:
            Vars.cmdop=False
            print("exiting cli..")
        elif "opn" in object:
            if "-w" in object:
                repl1=object.replace("-w", "")
                repl1=repl1.replace("opn", "")
                print(repl1)
                webbrowser.open(repl1)
        elif "soggycat" in object:
            if "-off" in object:
                print("Turning off...")
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
                        print("WARNING! Changing the name can have weird, and i mean WEIRD side effects on the terminal, YOU WANTED THIS!")
                elif "-name" in object:
                    systemnamedchanged=object.replace("soggycat", "")
                    systemnamedchanged=systemnamedchanged.replace("-change", "")
                    systemnamedchanged=systemnamedchanged.replace("-name", "")
                    systemnamedchanged=systemnamedchanged.replace(" ", "")
                    print("WARNING! Changing the name can have weird, and i mean WEIRD side effects on the terminal, YOU WANTED THIS!")
                    Vars.SystemSCName=str(systemnamedchanged)
            elif "-var" in object:
                dashvar=object.replace("soggycat", "")
                dashvar=dashvar.replace("-var", "")
                dashvar=dashvar.replace(" ", "")
                print(getattr(Vars, dashvar))
            elif "-create" in object:
                if "-file" in object:
                    if "-sogcl" in object:
                        if "-body" in object:
                            print("Created .sogcl file at current directory!")
                        else:
                            print("Successfully created empty .sogcl file at current directory!")
                    elif "-sog" in object:
                        print("Sorry! .sog isnt made yet! try the .sogcl maybe!")
                elif "-var" in object:
                    dashvarvar = object.replace("-var", "")
                    dashvarvar = object.replace("soggycat", "")
            elif "-info" in object:
                print("Running Soggycat >1.0.0")
            elif "-run" in object:
                if "-sogcl" in object:
                    if "-file" in object:
                        print("Sorry! directory file execution isnt available until v1.0.0 onwards!")
                    elif "-body" in object:
                        sogcl(object)
            else:
                print(Vars.BLUE, "Be carefull when dealing with soggycat commands! you can literally change the code in the os!", Vars.RESET)
        elif "help" in object:
            print("For Advanced Commands, do soggycat -help, for a regular help, do -help -regular")
        elif "echo" in object:
            print(object.replace("echo", "")) 
        else:
            print("obj: ", object, " not recognized")
    while Vars.i=="f":
        if Vars.oson:
            if Vars.cmdop:
                cmd = input(Vars.SystemSCName+" > ")
                comd(cmd)
            else:
                Vars.cmdop=False
        else:
            Vars.i="s"
sc()

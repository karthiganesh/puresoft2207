def process_main():
    print("main")

def file_open():
    print("file open")

def file_close():
    print("File Close")

def apply_color(ps1='black'):
    print("Colors are applied",ps1)

def outer_fun():
    print("TP1")
    def inner_fun(pn1):
        print("TP2")
        def inner_inner_fun(pn1):
            print("TP3",pn1)
            return pn1 + 100
        print("TP4")
        dct_a = {'vishal':inner_inner_fun}
        lst_menu_cmd = [
            {'mainmenu':process_main},
            {'firstmenu':file_open},
            {'secondmenu':file_close},
            {'thirdmenu':apply_color}
        ]
        x = dct_a['vishal'](20)
        y = inner_inner_fun(30)
        lst_menu_cmd[3]['thirdmenu']('red')
        print(x,y)
        return x/2
    print("TP5")
    print("a=",inner_fun(10))

#main starts
print("TP6")
outer_fun()

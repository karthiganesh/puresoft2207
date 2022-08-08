#kg220729 demo for UDF with custom modules
import demo_mod_const

def show_conf():
    print(f"Org     : {demo_mod_const.ORG_NAME}")
    print(f'Version : {demo_mod_const.VERSION_NUMBER}')

#main starts here
if __name__ == '__main__':
    print("Starting...")
    show_conf()
    print("Completed.")
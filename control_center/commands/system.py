import os

def clear_screen(context, registry):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
def exit_app(context, registry):
    print("Cerrando sistema...")
    context.running = False
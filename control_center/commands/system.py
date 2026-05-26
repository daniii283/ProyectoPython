import os

def clear_screen(context, registry, args):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    
def exit_app(context, registry, args):
    print("Cerrando sistema...")
    context.running = False
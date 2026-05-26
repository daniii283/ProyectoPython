def show_help(context, registry, args):
    print("Comandos disponibles: ")
        
    for command, command_info in sorted(registry.all()):
        description = command_info["description"]
        print(f"{command:<12}   - {description}")
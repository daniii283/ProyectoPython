def show_help(context, registry):
    print("Comandos disponibles: ")
        
    for command, command_info in sorted(registry.all()):
        description = command_info["description"]
        print(f"{command:<12}   - {description}")
import os

class ControlCenterApp:

    def __init__(self):
        self.running = True
        self.system_name = "NEXUS"
        self.version = "0.1.0"
        self.commands = {
            "help": {
                "description": "muestra esta ayuda",
                "handler": self.show_help
            },
            "status": {
                "description": "muestra el estado del sistema",
                "handler": self.show_status
            },
            "clear": {
                "description": "limpia la terminal",
                "handler": self.clear_screen,
            },
            "exit": {
                "description": "cierra el sistema",
                "handler": self.exit_app
            },
            "modules": {
                "description": "muestra los módulos del sistema",
                "handler": self.show_modules
            }
        } 
        self.modules =  {
            "core": "online",
            "terminal": "online",
            "diagnostic": "stanby"
        }
        
    def run(self):
        print(f"{self.system_name} Control Center v{self.version}")
        print("Type 'help' to see available commands.")

        while self.running:
            comando = input(f"{self.system_name} > ")
            self.process_command(comando)
            
    def process_command(self, comando):
        command = comando.lower().strip()
        if not command:
            return
        
        command_info = self.commands.get(command)
    
        if command_info is None:
            print("Comando desconocido")
            return

        handler = command_info["handler"]
        
        handler()
        
    
    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    
    def show_help(self):
        print("Comandos disponibles: ")
        
        for command in sorted(self.commands):
            command_info = self.commands[command]
            description = command_info["description"]
            print(f"{command:<10}   - {description}")
    
    def show_status(self):
        print("SYSTEM STATUS")
        print(f"Name: {self.system_name}")
        print(f"Version: {self.version}")
        print("System: online")
        print("Mode: CLI")
        print("Core: stable")
        print("Alerts: 0")
    
    def exit_app(self):
        print("Cerrando sistema...")
        self.running = False
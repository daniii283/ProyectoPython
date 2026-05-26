import os

class ControlCenterApp:

    def __init__(self):
        self.running = True
        self.system_name = "NEXUS"
        self.version = "0.1.0"
        self.mode = "CLI"
        self.core_status = "stable"
        self.alerts = 0
        self.modules =  {
            "core": "online",
            "terminal": "online",
            "diagnostics": "standby"
        }
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
            },
            "alert": {
                "description": "registra una nueva alerta",
                "handler": self.register_alert
            },
            "reset-alerts": {
                "description": "reinicia las alertas activas",
                "handler": self.reset_alerts
            }

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
            
    def register_alert(self):
        self.alerts += 1
        print(f"Alerta registrada. Alertas activas: {self.alerts}")
    
    
    def reset_alerts(self):
        if self.alerts == 0:
            print("No hay alertas activas.")
            return


        alertas_antiguas = self.alerts
        self.alerts = 0
        print(f"Se han reiniciado {alertas_antiguas} alerta(s)")
    
        
    def show_modules(self):
        print("ACTIVE MODULES")
        
        for module in sorted(self.modules):
            module_status = self.modules[module]
            print(f"{module:<12}    - {module_status}")
            
    
    def show_help(self):
        print("Comandos disponibles: ")
        
        for command in sorted(self.commands):
            command_info = self.commands[command]
            description = command_info["description"]
            print(f"{command:<12}   - {description}")
    
    def show_status(self):
        print("SYSTEM STATUS")
        print(f"Name: {self.system_name}")
        print(f"Version: {self.version}")
        print("System: online")
        print(f"Mode: {self.mode}")
        print(f"Core: {self.core_status}")
        print(f"Alerts: {self.alerts}")
    
    def exit_app(self):
        print("Cerrando sistema...")
        self.running = False
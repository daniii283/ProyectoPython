import os
from control_center.core.context import SystemContext
from control_center.core.command_registry import CommandRegistry

class ControlCenterApp:

    def __init__(self):
        self.context = SystemContext()
        self.commands = CommandRegistry()
        self.register_commands()

    
    def register_commands(self):
        self.commands.register("help", "muestra esta ayuda", self.show_help)
        self.commands.register("status", "muestra el estado del sistema", self.show_status)
        self.commands.register("clear", "limpia la terminal", self.clear_screen)
        self.commands.register("exit", "cierra el sistema", self.exit_app)
        self.commands.register("modules", "muestra los módulos del sistema", self.show_modules)
        self.commands.register("alert", "registra una nueva alerta", self.register_alert)
        self.commands.register("reset-alerts", "reinicia las alertas activas", self.reset_alerts)
        self.commands.register("diagnostics", "ejecuta un diagnostico básico del sistema", self.run_diagnostics)
                
    def run(self):
        print(f"{self.context.system_name} Control Center v{self.context.version}")
        print("Type 'help' to see available commands.")

        while self.context.running:
            comando = input(f"{self.context.system_name} > ")
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
        self.context.alerts += 1
        print(f"Alerta registrada. Alertas activas: {self.context.alerts}")
    
    
    def reset_alerts(self):
        if self.context.alerts == 0:
            print("No hay alertas activas.")
            return
        alertas_antiguas = self.context.alerts
        self.context.alerts = 0
        print(f"Se han reiniciado {alertas_antiguas} alerta(s)")
    
    def run_diagnostics(self):
        modules_count = len(self.context.modules)
        if self.context.alerts == 0:
            result = "nominal"
        else:
            result = "attention required"
            
        print("DIAGNOSTICS REPORT")
        print(f"Core: {self.context.core_status}")
        print(f"Modules checked: {modules_count}")
        print(f"Alerts active: {self.context.alerts}")
        print(f"Result: {result}")
        
        
    def show_modules(self):
        print("ACTIVE MODULES")
        
        for module in sorted(self.context.modules):
            module_status = self.context.modules[module]
            print(f"{module:<12}    - {module_status}")
            
    
    def show_help(self):
        print("Comandos disponibles: ")
        
        for command, command_info in sorted(self.commands.all()):
            description = command_info["description"]
            print(f"{command:<12}   - {description}")
    
    def show_status(self):
        print("SYSTEM STATUS")
        print(f"Name: {self.context.system_name}")
        print(f"Version: {self.context.version}")
        print("System: online")
        print(f"Mode: {self.context.mode}")
        print(f"Core: {self.context.core_status}")
        print(f"Alerts: {self.context.alerts}")
    
    def exit_app(self):
        print("Cerrando sistema...")
        self.context.running = False
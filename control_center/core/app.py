from control_center.core.context import SystemContext
from control_center.core.command_registry import CommandRegistry
from control_center.commands.status import show_status
from control_center.commands.modules import show_modules
from control_center.commands.help import show_help
from control_center.commands.diagnostics import run_diagnostics
from control_center.commands.alerts import register_alert, reset_alerts
from control_center.commands.system import clear_screen, exit_app

class ControlCenterApp:

    def __init__(self):
        self.context = SystemContext()
        self.commands = CommandRegistry()
        self.register_commands()

    def register_commands(self):
        self.commands.register("help", "muestra esta ayuda", show_help)
        self.commands.register("status", "muestra el estado del sistema", show_status)
        self.commands.register("clear", "limpia la terminal", clear_screen)
        self.commands.register("exit", "cierra el sistema", exit_app)
        self.commands.register("modules", "muestra los módulos del sistema", show_modules)
        self.commands.register("alert", "registra una nueva alerta", register_alert)
        self.commands.register("reset-alerts", "reinicia las alertas activas", reset_alerts)
        self.commands.register("diagnostics", "ejecuta un diagnostico básico del sistema", run_diagnostics)
                
    def run(self):
        print(f"{self.context.system_name} Control Center v{self.context.version}")
        print("Type 'help' to see available commands.")

        while self.context.running:
            raw_comando = input(f"{self.context.system_name} > ")
            self.process_command(raw_comando)
            
    def process_command(self, raw_command):
        command = raw_command.lower().strip()
        if not command:
            return
        command_info = self.commands.get(command)
        if command_info is None:
            print("Comando desconocido")
            return
        handler = command_info["handler"]
        handler(self.context, self.commands)
        

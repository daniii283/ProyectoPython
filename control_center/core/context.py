class SystemContext:
    def __init__(self):
        self.running = True
        self.system_name = "NEXUS"
        self.version = "0.1.0"
        self.mode = "CLI"
        self.core_status = "stable"
        self.alerts = 0
        self.modules = {
            "core": "online",
            "terminal": "online",
            "diagnostics": "standby"
        }
        
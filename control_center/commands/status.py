def show_status(context, registry):
    system_status = "online" if context.running else "offline"
        
    print("SYSTEM STATUS")
    print(f"Name: {context.system_name}")
    print(f"Version: {context.version}")
    print(f"System: {system_status}")
    print(f"Mode: {context.mode}")
    print(f"Core: {context.core_status}")
    print(f"Alerts: {context.alerts}")
    
def register_alert(context, registry):
    context.alerts += 1
    print(f"Alerta registrada. Alertas activas: {context.alerts}")
    
    
def reset_alerts(context, registry):
    if context.alerts == 0:
        print("No hay alertas activas.")
        return
    previous_alerts = context.alerts
    context.alerts = 0
    print(f"Se han reiniciado {previous_alerts} alerta(s)")
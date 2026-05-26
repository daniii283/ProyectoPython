def run_diagnostics(context, registry, args):
    modules_count = len(context.modules)
    if context.alerts == 0:
        result = "nominal"
    else:
        result = "attention required"
        
    print("DIAGNOSTICS REPORT")
    print(f"Core: {context.core_status}")
    print(f"Modules checked: {modules_count}")
    print(f"Alerts active: {context.alerts}")
    print(f"Result: {result}")
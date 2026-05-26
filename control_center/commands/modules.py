def show_modules(context, registry):
    print("ACTIVE MODULES")
        
    for module in sorted(context.modules):
        module_status = context.modules[module]
        print(f"{module:<12}    - {module_status}")
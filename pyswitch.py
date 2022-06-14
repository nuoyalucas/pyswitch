def switch(variable,case):
    for key,value in case.items():
        if (variable == key):
            exec(value)
            break
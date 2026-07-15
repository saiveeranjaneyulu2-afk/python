Global variable:
value = 10

def test_scope():
    # Local variable with the same name
    value = 20
    
    # Printing local variable
    print("Local variable inside function:", value)
    
    # Printing global variable using globals() dictionary
    print("Global variable inside function:", globals()['value'])

test_scope()

print("Global variable outside function:", value)

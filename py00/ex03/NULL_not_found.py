def NULL_not_found(object: any)-> int:
    
    try:
        match object:
            case None:
                print(f'Nothing: {object} {type(object)}')
            case float() if object != object:
                print(f'Cheese: {object} {type(object)}')
            case int() if object == 0:
                print(f'Zero: {object} {type(object)}')
            case str() if object == "":
                print(f'Empty: {object} {type(object)}')
            case bool() if object == False:
                print(f'Fake: {object} {type(object)}')
            case _:
                print("Type: not Found")
    except Exception as e:
        print(f'Error: {e}')
    return 1
def all_thing_is_obj(object: any) ->int:
    
    ret = None
    try:
        match object:
            case str():
                ret = f"{object} is in the kitchen : {type(object)}"            
            case tuple():
                ret = f"Tuple : {type(object)}"
            case list():
                ret = f"List : {type(object)}"
            case set():
                ret = f"Set : {type(object)}"
            case dict():
                ret = f"Dict : {type(object)}"
            case _:
                ret = "Type not found"
    except Exception as e:
        print(f'Error {e}')

    print(ret);
    return 42

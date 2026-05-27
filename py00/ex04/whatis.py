import sys

def whatis(argv):
        
    try:
        # print(f'argumentos: {len(sys.argv)}')
        assert len(argv) < 3, "more than one argument provided"
        if (len(argv) == 2):
            try:
                nb = int(sys.argv[1])
            except ValueError:
                raise AssertionError("argument is not an integer")
            if(nb % 2 == 0):
                print("I`m Even")
            else:
                print("I`m Odd")
    except AssertionError as e:
        print(f'AssertionError: {e}');
    except Exception as e:
        print(e)

if __name__ == "__main__":
    whatis(sys.argv)

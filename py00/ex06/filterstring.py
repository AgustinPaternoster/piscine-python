import ft_filter as ftt
import sys

def main(argv:list)->list:
     
    text = argv[1].split()
    try:
        assert len(argv) == 3 , "the arguments are bad"
        for word in text:
            if not word.isalpha():
                raise AssertionError("the arguments are bad")
        try:
            nb = int(argv[2])
        except:
            raise AssertionError("the arguments are bad")
        result = ftt.ft_filter(lambda n: len(n) > nb, text)
        print(list(result))

    except EOFError:
        print("EOF")
    except AssertionError as e:
        print(f'AssertionError: {e}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main(sys.argv)



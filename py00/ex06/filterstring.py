import ft_filter as ftt
import sys

def filterstring(string: str , n: int)->list:
    text = string.split()
    for word in text:
        if not word.isalpha():
            raise AssertionError("the arguments are bad")
    return list(ftt.ft_filter(lambda x: len(x) > n, text))


def main(argv:list)->list:
     
    try:
        assert len(argv) == 3 , "the arguments are bad"
        try:
            nb = int(argv[2])
        except:
            raise AssertionError("the arguments are bad")
        result = filterstring(argv[1], nb)
        print(list(result))

    except EOFError:
        print("EOF")
    except AssertionError as e:
        print(f'AssertionError: {e}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    main(sys.argv)



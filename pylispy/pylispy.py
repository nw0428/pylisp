def cons(x, y):
    '''
    cons(x, y) takes its two arguments and puts them into a python tuple.
    This tuple can be used to represent a node in a linked list, or a pair
    '''
    return (x, y)

def car(x):
    '''
    car(cons(x, y)) returns x. In other words, car returns the head of a linked list or the left item of a pair
    '''
    return x[0]

def cdr(x):
    '''
    cdr(cons(x, y)) returns y. In other words, cdr returns the tail of a linked list or the right item of a pair
    '''
    return x[1]

def caar(x):
    return car(car(x))

def cddr(x):
    return cdr(cdr(x))

def cdar(x):
    return cdr(car(x))

def cadr(x):
    return car(cdr(x))

def cdadr(x):
    return cdr(car(cdr(x)))

def is_null(x):
    '''
    is_null(null) returns true
    is_null(()) returns true
    In all other cases is_null returns false
    '''
    return x == ()

def is_pair(x):
    '''
    is_pair(x) returns true if x is a pair/2-tuple/cons cell or null
    if x is anything else it returns false
    '''
    return isinstance(x, tuple) and len(x) == 2

# null: Final = ()
null = ()

def append(x, y):
    '''
    Given two PyLispy lists x and y this function concatenates them, with y coming after x
    '''
    if is_null(x):
        return y
    elif not is_pair(x) or not is_pair(y): # This check is probably unnecessary
        raise ValueError("Illegal arguments")
    else:
        return cons(car(x), append(cdr(x), y))

def ls(*argv):
    '''
    ls(*argv) takes a list of arguments and turns them into a lisp style list of cons cells
    so ls(1,2,3,4,5) => cons(1, cons(2, cons(3, cons(4, cons(5, ())))))
    '''
    if len(argv) is 0:
        return null
    else:
        return cons(argv[0], ls(*argv[1:]))


if __name__ == "__main__":
    print("Nothing in main at the moment")


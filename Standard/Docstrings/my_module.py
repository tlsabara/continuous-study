"""My Module, short Description

Here is a long description of My Module and should be written things about how to use, functions, links of documentation
and references.
"""


def my_function(a: int, b: int, c: str, d: bool) -> int:
    """This function was buildit only to explain docstring in functions. (Foo)

    :param a:Any Number
    :param b:Another any Number
    :param c:Any String
    :param d:A dumb bool
    :return:One of numbers passed in parameters
    """
    if str(a + b) in c:
        return a
    elif d:
        return a + b
    else:
        return b



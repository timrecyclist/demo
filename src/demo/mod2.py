def demo():
    print("Hello from mod2")


def concat(str1, str2, sep=" "):
    """
    Concatenates two strings

    Parameters:
        str1 - string
        First string

        str2 - string
        Second string

        sep - string
        The separator between the first and second strings

    Returns:
        String
        A concatenation of str1 and str2 separated by sep
    """
    return f"{str1}{sep}{str2}"

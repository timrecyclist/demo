def demo():
    """
    Test function that prints hello

    Returns:
        None
    """
    print("Hello from demo")


def adder(num1, num2):
    """
    Adds two numbers together

    Parameters:
        num1 - int | float
        The first number to be added

        num2 - int | float
        The second number to be added

    Returns:
        int | float
        The sum of num1 and num2
    """
    return num1 + num2


def percent_change(datapoint1, datapoint2):
    """
    Returns the percentage change between two datapoints.
    datapoint2 is intended to be the datapoint recorded at a later time than
    datapoint 1

    Parameters:
        datapoint1 - int | float
        The first datapoint

        datapoint2 - int | float
        The second datapoint

    Returns:
        String
        The percent change between the given datapoints
        i.e. ((datapoint2-datapoint1)/datapoint1)*100
    """
    return f"{str(round(((datapoint2-datapoint1)/datapoint2) * 100))}%"

"""
Temperature conversion functions

Usage:
c_temp = c2f(f_temp)
f_temp = f2c(c_temp)
"""
import sys

def c2f(cel: float) -> float:
    """
    Convert Celsius temperature to Fahrenheit

    :param cel: Celsius temperature as int or float
    :return: Fahrenheit temperature as float
    """
    cel = float(cel)
    f = (9/5 * cel) + 32

    return round(f, 3)

def f2c(fahr: float) -> float:
    """
    Convert Fahrenheit temperature to Celsius

    :param fahr: Fahrenheit temperature as int or float
    :return: Celsius temperature as float
    """
    fahr = float(fahr)
    c = (fahr - 32) * (5/9)

    return round(c, 3)

def _c2f_cli():
    """
    CLI utility script
    Called from command line as 'c2f'
    """
    cel = float(sys.argv[1])
    return c2f(cel)

def _f2c_cli():
    """
    CLI utility script
    Called from command line as 'f2c'
    """
    fahr = float(sys.argv[1])
    return f2c(fahr)

if __name__ == '__main__':
    print(c2f(100))
    print(c2f(0.0))
    print(f2c(212.1))
    print(f2c(-40))



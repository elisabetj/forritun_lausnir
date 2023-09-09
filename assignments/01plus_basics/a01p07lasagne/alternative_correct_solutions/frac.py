from fractions import Fraction

degrees_farenheit = int(input())
degrees_celcius = (degrees_farenheit - 32) * Fraction(5, 9)
degrees_celcius += (1 if degrees_celcius >= 0 else -1) * Fraction(
    degrees_celcius.denominator // 2, degrees_celcius.denominator
)
degrees_celcius = int(degrees_celcius)

print(degrees_celcius)

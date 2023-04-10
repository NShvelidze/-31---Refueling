def main():
    x = input("Fraction: ")
    fraction = convert(x)
    print(fraction)
    percentage = gauge(fraction)
    print(percentage)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            fraction = int(x) / int(y)
            if fraction > 1:
                raise(ValueError)
            else:
                return fraction
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 0.01:
        return "E"
    if percentage >= 0.99:
        return "F"
    else:
        x = "{:.0%}".format(percentage)
        return x

if __name__ == "__main__":
    main()

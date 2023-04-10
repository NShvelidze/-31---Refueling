from fuel import convert, gauge
import pytest

def main():
    test_input()
    test_zero_division()
    test_value_error()

def test_input():
    assert convert("1/4") == 0.25 and gauge(0.25) == "25%"
    assert convert("1/100") == 0.01 and gauge(0.01) == "E"
    assert convert("99/100") == 0.99 and gauge(0.99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("2/1")

if __name__ == "__main__":
    main()

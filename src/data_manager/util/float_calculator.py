from decimal import Decimal


def calculate(num1: float, num2: float, operation: str) -> float:
    input1 = Decimal(str(num1))
    input2 = Decimal(str(num2))
    output = None
    if operation == "ARITH_MULTI":
        output = input1 * input2
    elif operation == "ARITH_ADD":
        output = input1 + input2

    return float(output)

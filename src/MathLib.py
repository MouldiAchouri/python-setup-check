from src.MathRequests import MathRequest

class Mathlib(MathRequest):

    def __init__(self):
        match (MathRequest.oper()):
            case "+":
                MathRequest.
            case '-':
                res = ope1 - ope2
            case '*':
                res = ope1 * ope2
            case '/':
                if ope2 == 0:
                    print("Error: Division by zero is undefined.")
                    return
                res = ope1 / ope2
            case '^':
                res = 1
                for count in range(int(ope1)):
                    res = res * ope2
            case _:
                print("Invalid operator.")
                return
        return res
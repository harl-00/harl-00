from modules.inputs import numbers
from modules.process import addition, subtraction, multiplication, division
from modules.outputs import final

def main():
    num1, num2 = get_numbers()
    results = [f"{num1} plus {num2} is {addition(num1 , num2)}",
        f"{num1} minus {num2} is {subtraction(num1 , num2)}",
        f"The product of {num1} and {num2} is {multiplication(num1 , num2)}",
        f"{num1} divided by {num2} is {division(num1 , num2)}"]
        

    final(results)
        

import modules.inputs as i
import modules.processData as p
import modules.outputs as o
print(dir(i))
def main():
    num1, num2 = i.get_numbers()
    results = [f"{num1} plus {num2} is {p.addition(num1 , num2)}",
        f"{num1} minus {num2} is {p.subtraction(num1 , num2)}",
        f"{num1} multiplied  {num2} is {p.multiplication(num1 , num2)}",
        f"{num1} divided by {num2} is {p.division(num1 , num2)}"]
        

    o.final(results)


main()
        

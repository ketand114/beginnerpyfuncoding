from StackLinkList import Stack

def Calculate(operand2,operand1,operator):
    if operator is "+":
        return operand1+operand2
    elif operator is "*":
        return operand1*operand2
    elif operator is "/":
        return operand1/operand2
    else:
        return operand1-operand2

def main():
    pass

if __name__ == '__main__':
    main()

    equation = "(((((((2+5)*(2*5))/5)-4)*5)-1)"
    Operator = Stack()
    Operands = Stack()

    for i in range(len(equation)):
        if equation[i] is ")":
            op2 = Operands.pop()
            op1 = Operands.pop()
            fn = Operator.pop()
            print op1,fn,op2
            calvalue = Calculate(op2,op1,fn)
            Operands.push(calvalue)
            print "Calculation done"
            Operands.showstack()
            Operator.showstack()
        elif equation[i] in ['+','*','/','-']:
            Operator.push(equation[i])
            print "Operator found"
            Operands.showstack()
            Operator.showstack()
        elif equation[i] in ['0','1','2','3','4','5','6','7','8','9']:
            Operands.push(int(equation[i]))
            print "Operands found"
            Operands.showstack()
            Operator.showstack()
        else:
            pass

    print "The equation evaluates to:",Operands.pop()

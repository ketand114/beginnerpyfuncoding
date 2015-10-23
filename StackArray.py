def stackEmptyposition(array):
    position = None
    for i in range(len(array)):
        if array[i] == None:
            position = i
            return position
    return position

def push(array,data):
    position = stackEmptyposition(array)
    if position is not None:
        array[position]=data
    else:
        position = len(array)
        array = resizeup(array)
        array[position] = data
    return array

def pop(array):
    position = stackEmptyposition(array)
    if position is not None:
        data = array[position-1]
        array[position-1]= None
    else:
        data = array[-1]
        array[-1] = None
    if (position-1) <= (len(array)/4):
        array = resizedown(array)
    print "Data popped from stack:",data
    return array

def resizeup(array):
    newarray = [None]*(len(array)*2)
    for i in range(len(array)):
        newarray[i] = array[i]
    return newarray

def resizedown(array):
    newarray = [None]*(len(array)/2)
    for i in range(len(array)/4):
        newarray[i] = array[i]
    return newarray

def showstack(array):
    for i in range(len(array)):
        print "|", array[i],
    print "|"


def main():
    pass

if __name__ == '__main__':
    main()
    A = [None]*1
    A = push(A,10)
    A = push(A,20)
    showstack(A)
    A = push(A,30)
    showstack(A)
    A = push(A,45)
    A = push(A,99)
    showstack(A)
    A = pop(A)
    showstack(A)
    A = pop(A)
    showstack(A)
    A = pop(A)
    showstack(A)
    A = pop(A)
    showstack(A)

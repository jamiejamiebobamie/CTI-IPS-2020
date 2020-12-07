def k_backspace(inputString):
    i = len(inputString)-1
    stack=0
    intended_string_array = []
    while i >= 0:
        if inputString[i] != "<":
            if not stack:
                intended_string_array.append(inputString[i])
            else:
                stack-=1
        else:
            stack+=1
        i-=1

    return "".join(intended_string_array[::-1])

# don't forget to actually call your answer's function!
testInput = 'a<bc<'
actualOutput = k_backspace(testInput)
print(actualOutput)
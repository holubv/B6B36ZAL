STATIC_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(arg):
    text = STATIC_TEXT + str(arg)
    with open('02_python_output.txt', 'w') as file:
        file.write(text)
    return '02_python_output.txt'

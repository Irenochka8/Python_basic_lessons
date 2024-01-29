sentence = input()
literal = '''!"#$%&'()*+,  -./:;<=>?@[\\]^`{|}~'''
kwlist = "False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"
# result = ""
for i in sentence:
    if literal in sentence:
        result = "False"

    if sentence.startswith(kwlist[::]):
        result = "False"
    elif sentence[0].isdigit():
        result = "False"
    elif not sentence.islower():
            result = "False"
    elif not sentence.isalnum():
            result = "False"

    elif sentence.find("_")>1:
        result = "False"
    else:
        result = "True"
print(result)












# if sentence.count('_') == 1:
#     result = "True"
# else:
#     sentence.count('_')<1
#     result = "False"

    # if sentence[0].isdigit():
    #     result = "False"
    # else:
    #     result = "True"




    # for text in sentence:
    #     if i in kwlist == sentence:
    #         result = "False"
    #     else:
    #         result = "True"
    #if sentence.find(literal):
    #    result = "False"
    #else:
    #    sentence.isalpha()
    #    result = "True"
    # for i in sentence:
    #     if i in kwlist:
    #     result = "False"
    # else:
    #     result = "True"












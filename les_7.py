#Task_1
def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"
print(say_hi("Frank", 68))

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

#Task_2
def correct_sentence(text):
    sentences = text.split(". ")
    result_text = []
    for sentence in sentences:
        words = sentence.split()
        if words[0]:
            words[0] = words[0].capitalize()
            result_sentence = " ".join(words)
            result_text.append(result_sentence)
    wright_text = ". ".join(result_text)
    if not wright_text.endswith("."):
        wright_text += (".")
    return wright_text
print(correct_sentence("greetings. friends"))

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')

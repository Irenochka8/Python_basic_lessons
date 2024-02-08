# Task_1 count_popular_words
text = "When I was One I had just begun When I was Two I was nearly new"
words = ['i', 'was', 'three', 'near']

def popular_words(text, words):
    text_words = text.lower().split()
    popular_dict_words = {word: words.count(text_words) for word in words}
    for word in text_words:
        if word in words:
            popular_dict_words[word] += 1
    return popular_dict_words
print(popular_words(text, words))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

 # Task_2 difference max_numb and min_numb
def difference(*numb_args):
    if not numb_args:
        return 0
    else:
        result = max(numb_args)-min(numb_args)
    return round(result, ndigits=1)
print(difference(5, -5))

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

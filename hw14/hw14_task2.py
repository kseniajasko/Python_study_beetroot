# Write a decorator that takes a list of stop words and replaces them
# with *inside the decorated function

def stop_words(words: list):
    def search(func):
        def search_1(name):
            a = func(name)
            for word in words:
                a = a.replace(word, '*')
            return a
        return search_1
    return search


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))
# based off what is said by google:
# something that allows for programmatic generation of code.
# I hope this works.
# I have never "metaprgrammed" before

class WordCounter:
    def __init__(self, text):
        self.text = text.lower()
        self.words = self.text.split()
    
    def count_word(self, word):
        return self.words.count(word.lower())

    @classmethod
    def generate_counter_methods(cls, *words):
        """Dynamically generates methods for counting specific words."""
        for word in words:
            method_name = f'count_{word}'
            setattr(cls, method_name, cls._create_counter_method(word))
    
    @staticmethod
    def _create_counter_method(word):
        def counter(self):
            return self.count_word(word)
        return counter

# Test cases using pytest
def test_word_counter():
    with open("task6_read_me.txt") as file:
        read = file.read()
        file.close()
    text = read
    counter = WordCounter(text)
    
    WordCounter.generate_counter_methods("lorem", "nam", "tristique")
    
    assert counter.count_lorem() == 3
    assert counter.count_nam() == 1
    assert counter.count_tristique() == 1
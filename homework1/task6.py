with open("task6_read_me.txt") as file:
    read = file.read()
    file.close()

#TODO:
# Implement metaprogramming techniques to dynamically generate function names
# for your pytest test cases based on the filenames of the text files. Include pytest test cases that verify
# the word count for each text file.
# what is metaprogramming??????
# ???

def test_wordcount():
    assert len(read.split()) == 127
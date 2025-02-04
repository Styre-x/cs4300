books = [
    "Name: The Cuckoo's Egg, Author: Cliff Stoll",
    "Name: Ghost in the Wires, Author: Kevin Mitnick",
    "Name: Hackers: Heroes of the Computer Revolution, Author: Steven Levy",
    "Name: The Phoenix Project, Author: Gene Kim",
    "Name: The Code Book, Author: Simon Singh",
    "Name: Gödel, Escher, Bach, Author: Douglas Hofstadter",
    "Name: Snow Crash, Author: Neal Stephenson",
    "Name: Neuromancer, Author: William Gibson",
    "Name: The 48 Laws of Power, Author: Robert Greene",
    "Name: Thinking, Fast and Slow, Author: Daniel Kahneman"
]

students = {
    "student1": 1,
    "student2": 2,
    "student3": 3
}

def test_slicing():
    assert books[:3] == ["Name: The Cuckoo's Egg, Author: Cliff Stoll",
    "Name: Ghost in the Wires, Author: Kevin Mitnick",
    "Name: Hackers: Heroes of the Computer Revolution, Author: Steven Levy"]

def test_students():
    for i in range(1,4):
        assert students.get("student" + str(i)) == i
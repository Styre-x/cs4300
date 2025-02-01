def printHello():
    print("hello, world")
    return True

def test_main():
    assert printHello()

if __name__ == "__main__":
    test_main()

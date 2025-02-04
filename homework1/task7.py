import matplotlib.pyplot as plt

def create_plot():
    fig, ax = plt.subplots()
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]
    ax.plot(x, y, label="y = x^2")
    ax.set_title("Basic Line Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    return fig, ax

# I found this only works well in a jupyter notebook AFTER setting all the code up. Oops lol. 

def test_plot():
    fig, ax = create_plot()
    
    # Check if a figure is created
    assert fig is not None, "Figure was not created."

    # Check if an Axes object exists
    assert len(fig.axes) > 0, "No axes found in figure."

    line = ax.lines[0]
    assert list(line.get_xdata()) == [0, 1, 2, 3, 4], "X data does not match expected values."
    assert list(line.get_ydata()) == [0, 1, 4, 9, 16], "Y data does not match expected values."

if __name__ == "__main__":
    # Run the test when executed
    test_plot()
    print("Test passed!")

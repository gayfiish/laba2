import matplotlib.pyplot as plt


def create_graph():
    x_values = list(range(-10, 11))
    y_values = [x ** 2 for x in x_values]

    plt.plot(x_values, y_values)
    plt.title("Graph y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    create_graph()
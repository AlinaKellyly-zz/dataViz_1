import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

def run():
    fig, ax = plt.subplots()
    ax.plot(squares)

    plt.show()

if __name__=='__main__':
    run()
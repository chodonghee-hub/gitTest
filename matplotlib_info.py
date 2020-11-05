from matplotlib import pyplot as plt
from random import randint as rd

### matplotlib can express the result as chart

#--- all the x, y is list type data

#============== MAIN METHOD ===============
#--- plt.plot(x, y) → set line chart result
#--- plt.bar(x, y) → set bar chart result
#--- plt.title → set chart title
#--- plt.xlabel → set x side label
#--- plt.ylabel → set y side label
#--- plt.legend → set each chart's name
#--- plt.show → print your chart
#==========================================

x = [idx for idx in range(1, 10)]
y = [idx**2 for idx in x]
z = [rd(1, 10) for idx in range(9)]

def show_line_chart(x, y):
    plt.plot(x, y)
    plt.title('< Chart Title >')
    plt.xlabel('X side label')
    plt.ylabel('Y side label')
    plt.show()

def show_bar_chart(x, y):
    plt.bar(x, y, width=0.3, color = 'green')
    plt.title('< Chart Title >')
    plt.xlabel('X side label')
    plt.ylabel('Y side label')
    plt.show()

def show_two_line_chart(x, y, z):
    plt.plot(x, y)
    plt.plot(x, z)
    plt.title('< Chart Title >')
    plt.xlabel('X side label')
    plt.ylabel('Y side label')
    plt.legend(['A', 'B'])
    plt.show()


show_two_line_chart(x, y, z)
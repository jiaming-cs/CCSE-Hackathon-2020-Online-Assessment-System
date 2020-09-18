import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def make_pie_chart(suggestion_dict):
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = list(suggestion_dict.keys())
    sizes = list(suggestion_dict.values())
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig("./graphs/pie_chart.png")
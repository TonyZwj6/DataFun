# EDA:explory data analysis
# getting familiar with your data
# for example:summarize it using
# - statistics (like mean,standard deviation,sum,
# - visualizations(like line charts,bar charts,
# histograms,etc.)
# - data mining (like looking for patterns,
# relationship,griups,etc.)

# focus on visualizations
# 3 goals of visualizations
# 1.clearly and accurately represent data
# 2.be creative,while trying to to interest

# we are going to use the matplotlib library
# to visualize data as 2D charts



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def line_chart_example(x_ser,y_ser):
   # x_ser and y_ser are "prallel"
   # meaning same length and data in same order
   plt.plot(x_ser,
            y_ser,
            label="population",
            c="green", # c is for color
            lw=5) #lw is for line width
   plt.plot(x_ser,
            y_ser *2,
            label="population x2",
            c="purple",
            ls="--")
   #
   #
   plt.legend()
   #plt.show()
   #2.
   plt.ylabel("popultion(in millions)")
   plt.xlabel("city class")
   plt.title("Chinese population Analysis")
   plt.savefig("line.png") #jpg,pdf,etc

def scatter_chart_example(x_ser,y_ser):
    plt.figure()
    plt.scatter(x_ser,
                y_ser,
                s=300,
                marker="x")
    plt.savefig("scatter.png")

def bar_chart_example(x_ser,y_ser):
    plt.figure()
    plt.bar(x_ser,
            y_ser,)
    plt.savefig("bar.png")
def pie_chart_example(values_ser,label_ser):
    plt.figure()
    plt.pie(values_ser,
            labels=label_ser,
            autopct="%1.1f%%")
    plt.savefig("pie.png")
def histogram_chart_example(values_ser1,
                            values_ser2):
    plt.figure()
    plt.hist(values_ser1,
             bins=30,
             alpha=0.5)
    plt.hist(values_ser2,
             bins=30,
             alpha=0.5)
    plt.ylabel("Count (Frequency) of each X-axis Bin")
    plt.savefig("histogram.png")
df = pd.read_csv("merged.csv")
print(df)
# grab the total population for each Class
# (Large,Medium,Small)
grouped_by_class=df.groupby("class")
class_pop_ser=grouped_by_class["population"].sum()
print(class_pop_ser)

line_chart_example(class_pop_ser.index,class_pop_ser)
# great for numeric (y) data points that can be
# interpolated (or interpreted) between numeric
# (x) data points

# 2.scatter chart example
# great for LOTS of numeric (y) date points
# that should not be interpolated between
#
scatter_chart_example(class_pop_ser.index,class_pop_ser)
# 4.pie chart example
# great for numeric data that represents
# parts(percentages) of a whole (total)
bar_chart_example(class_pop_ser.index,class_pop_ser)
#
#
#
pie_chart_example(class_pop_ser,
                  class_pop_ser.index)
# histogram example
# great for showing the distribution (shape)
#
mean=100
stdev=25
num_datapoints=1000
rand_data1=np.random.normal(mean,
                            stdev,
                            num_datapoints)

rand_data2=np.random.normal(mean,
                            stdev/  2,
                             num_datapoints)
# task
#
#
#
histogram_chart_example(rand_data1,rand_data2)




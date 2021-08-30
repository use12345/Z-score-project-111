import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=  pd.read_csv("medium_data.csv")
data = df["id_list"].tolist()

#fig= ff.create_distplot([data],["Math Scores"], show_hist=False)
#fig.show()



mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("mean of population=",mean)
print("std_deviation of population=",std_deviation)


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list =[]
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation= statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("mean of sampling distribution=",mean)
print("std_deviation of sampling distribution=",std_deviation)

fig = ff.create_distplot([mean_list],["Id List"], show_hist=False)
fig.show()


first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-std_deviation,(2*mean+std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
#FIRST 
df = pd.read_csv("medium_data.csv")
data = df["id_list"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["id_list"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF IDS "))

fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17], mode="lines", name=" STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17], mode="lines", name=" STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17], mode="lines", name=" STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - mean_of_sample1)/std_deviation
print("The Z score  is :", z_score)





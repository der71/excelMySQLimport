import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import yaml


def main():
    with open('config.yaml', 'r') as file:
        stream = file.read()
    config = yaml.safe_load(stream)

    # connect to MySQL database
    mydb = mysql.connector.connect(
      host=config['host'],
      user=config['user'],
      password=config['password'],
      database=config['database']
    )

    selects = ["Analyte = 'Glutamate'", "Analyte = 'Glutamine'"]
    columns = ["Fold_change"]
    # columns = ["P_Value", "VIP_score", "Fold_change"]
    results = []

    mycursor = mydb.cursor()
    for select in selects:
        sql = "SELECT " + ', '.join(columns) + " FROM `projects` WHERE " + select + " ORDER BY " + ', '.join(columns)
        print(sql)
        mycursor.execute(sql)
        results.append(mycursor.fetchall())

    print(results)

    to_plot = []
    for result in results:
        res1 = []
        for col in result:
            res1.append(float(str(col).replace(",)", "").replace("(", "")))
        to_plot.append(res1)

    plot(to_plot, columns[0], selects)

def plot (data, title, selects):
    # x axis values
    x = range(len(data[0]))
    # corresponding y axis values
    y1 = data[0]
    y2 = data[1]
    # plotting the points

    plt.plot(x, y1, label = selects[0])
    plt.plot(x, y2, label = selects[1])
    plt.legend()

    # naming the x axis
    plt.xlabel('x - samples')
    # naming the y axis
    plt.ylabel('y - title')

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    plt.show()

main()

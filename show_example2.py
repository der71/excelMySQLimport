import matplotlib.pyplot as plt
import mysql.connector
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
    sql = SELECT + ', '.join(columns) + FROM `projects` WHERE " + select + " ORDER BY VIP_score"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    for result in results:
        print(result)

main()

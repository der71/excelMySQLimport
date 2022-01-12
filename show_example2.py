import matplotlib.pyplot as plt
import mysql.connector

def main():
    # connect to MySQL database
    mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="user",
      password="password",
      database="database"
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

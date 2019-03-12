# data-analyze
First week of VNPT Internship:
1. Implementation of pandas and matplotlib.pyplot 
- Use pandas to read csv file, translate it into DataFrame and do data manipulation on DataFrame
     
```python
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    import sys

    df = pd.read_csv('C:/Users/Hp-PC/Desktop/python/Telecom_customer_churn.csv')
    X = df.iloc[:,55].values #
    n_Points = 2000. #number of points
    dx = np.nanmax(X)/n_Points #dx on hist
    y = []
    for i in range(0,len(X)):
      if(np.isnan(X[i])):
        y.append('null')
      if(~np.isnan(X[i])):
        number = int(X[i]/dx)*dx
        y.append(number)
        #print(X[i])

    X1 = pd.DataFrame({"amount" : X, "range": y})
    print(X1.groupby("range").count().sort_values(by = "amount", ascending = False))
    #X2 = pd.DataFrame({"amount" : X[int(int(sys.argv[1])/dx):int(int(sys.argv[2])/dx)], "range" : y[int(int(sys.argv[1])/dx):int(int(sys.argv[2])/dx)]})
    X1.hist(column = 'range',bins = int(n_Points))#, range = (int(sys.argv[1]), int(sys.argv[2])))

    '''Setting up the plot'''
    #set limit for the plot
    #plt.xlim(X.min(), np.nanmax(X))
    plt.xlim(int(sys.argv[1]), int(sys.argv[2]))
    #plt.ylim(0,400)
    plt.xlabel('range')
    plt.ylabel('frequency')

    #plt.savefig('20190220.jpg')
    plt.show()  

  ```

- Outcome:
 
 ![alt text](https://github.com/tson1997/data-analyze/blob/master/20190220.jpg)



2. Implement MySQL Workbench to manipulate the data more easily

3. Learn to connect python and MySQL through mysql.connector library
- Use the library to re-implement the code above:
    ```python
    import mysql.connector as mc
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    conn = mc.connect(user = 'root', password = 'password', database = 'company')
    cur = conn.cursor()

    #get the data from database 
    query = "SELECT totcalls FROM test2 GROUP BY totcalls; "
    cur.execute(query)
    res = np.array(cur.fetchall())

    '''
    query = " ALTER TABLE test2 ADD COLUMN rangeA VARCHAR(200) AFTER eqpdays; "
    cur.execute(query)
    '''

    n_Points = 200
    dx = float(res.max())/n_Points

    # New list y to store data
    y = []

    for i in range(len(res)):
      y.append(res[i][0]/dx)
    query = " UPDATE test2 SET rangeA = CONCAT('From ', (SELECT CAST(totcalls/%f AS SIGNED))*%f, ' to ', (SELECT CAST(totcalls/%f AS SIGNED))*%f + %f);" 
    cur.execute(query %(dx, dx, dx, dx,dx))
    plt.hist(y, bins = n_Points)

    cur.execute("SELECT rangeA, COUNT(*) FROM test2 GROUP BY rangeA ORDER BY COUNT(*) DESC")
    rs = cur.fetchall()

    conn.commit()
    conn.close()

    for i in range(len(rs)):
      print("%-50s"%rs[i][0],"%10d"%rs[i][1])

    plt.show()
    ```
-> **Note:** MySQL makes it easier and faster to implement the code on data those are big in size


3. Using MySQL and Python to analyze the Nobel Prize database

4. Using MySQL and Python to analyze the EPL database 
- The database (csv file) is at: https://datahub.io/sports-data/english-premier-league
- MySQL code for finding the season ranking:
```SQL
CREATE TABLE Home 
SELECT HomeTeam, COUNT(*) AS HomeWin
FROM season1718
WHERE FTR = 'H'
GROUP BY HomeTeam;

CREATE TABLE HomeL 
SELECT HomeTeam, COUNT(*) AS HomeLose
FROM season1718
WHERE FTR = 'A'
GROUP BY HomeTeam;

CREATE TABLE Away
SELECT AwayTeam, COUNT(*) AS AwayWin
FROM season1718
WHERE FTR = 'A'
GROUP BY AwayTeam;

CREATE TABLE AwayL
SELECT AwayTeam, COUNT(*) AS AwayLose
FROM season1718
WHERE FTR = 'H'
GROUP BY AwayTeam;

CREATE TABLE joint
SELECT HomeTeam, HomeWin, AwayWin
FROM Home JOIN Away
ON HomeTeam = AwayTeam;

CREATE TABLE jointL
SELECT HomeTeam, HomeLose, AwayLose
FROM HomeL JOIN AwayL
ON HomeTeam = AwayTeam;

CREATE TABLE ranking1718
(id INT)
SELECT joint.HomeTeam AS Team, HomeWin + AwayWin AS Win, HomeLose+ AwayLose AS Lose, ( HomeWin + AwayWin)*3 + (38 - HomeWin - HomeLose- AwayWin - AwayLose) AS Pts
FROM joint
JOIN jointL
ON joint.HomeTeam = jointL.HomeTeam;

ALTER TABLE ranking1718
ADD COLUMN Deuce INT AFTER Win;

UPDATE ranking1718
SET Deuce = 38 - Win - Lose;

SELECT RANK() OVER(ORDER BY Lose,Pts DESC) AS Ranking, Team, Win, Lose, Pts FROM ranking1718;

DROP TABLE away, awayl,home,homel,joint, jointl;


```
- Compare total number of goals between two teams by months




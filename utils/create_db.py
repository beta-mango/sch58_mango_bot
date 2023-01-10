import sqlite3
connection = sqlite3.connect('ttable.db')
cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS c21(
    number TEXT,
    monday TEXT,
    tuesday TEXT,
    wednesday TEXT,
    thursday TEXT,
    friday TEXT);
""")
connection.commit()
lesson = ''
numbers = 1
for i in range(1, 9):
    mon = str(input('monday'))
    tues = str(input('tuesday'))
    wed = str(input('wednesday'))
    thur = str(input('thursday'))
    fri = str(input('friday'))
    data_tuple = (str(i), mon, tues, wed, thur, fri)
    cur.execute("""INSERT INTO c21(number, monday, tuesday, wednesday, thursday, friday) 
                   VALUES(?, ?, ?, ?, ?, ?);""", data_tuple)
    connection.commit()

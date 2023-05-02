# Evan Hanson
# 4/19/2021
# Homework 11: Databases

import mysql.connector

# establish connection to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password1234",
    database="Sakila"
)

# create cursor object to interact with the database
mycursor = db.cursor()

# execute a SQL query to retrieve data from the database
mycursor.execute("SELECT a.first_name, a.last_name, a.actor_id FROM sakila.actor a JOIN sakila.film_actor USING(actor_id) GROUP BY a.actor_id HAVING COUNT(*) > 40")

# retrieve the results of the query
results = mycursor.fetchall()

# print out the results of the query
for result in results:
    print(result)
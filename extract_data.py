import mysql.connector


db = mysql.connector.connect(
    host="127.0.0.1", user="trung", password="vdt", database="thongkebaibao"
)

cursor = db.cursor()

cursor.execute(
    "SELECT a.id, a.venue, a.publicationDate, c.name FROM articles a LEFT JOIN category c on a.categoryId = c.id WHERE c.name != 'Unclassified'"
)
results = cursor.fetchall()
with open("train_set.csv", "w", encoding="utf-8") as f:
    f.write("id,venue,category\n")
    for item in results:
        if item[1]:
            line = f"{item[0]},{item[1].replace(',', '')},{item[3]}\n"
            f.write(line)

cursor.execute(
    "SELECT a.id, a.venue, a.publicationDate, c.name FROM articles a LEFT JOIN category c on a.categoryId = c.id WHERE c.name = 'Unclassified'"
)
results = cursor.fetchall()
with open("test_set.csv", "w", encoding="utf-8") as f:
    f.write("id,venue,category\n")
    for item in results:
        if item[1]:
            line = f"{item[0]},{item[1].replace(',', '')}\n"
            f.write(line)

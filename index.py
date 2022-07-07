from utils_db import *

#try:
db = next(get_db())

# L = db.query(Bank_bill).all()
# print(len(L))

result = db.execute("Show tables;")

print(db)
db.close()

print("Everything is ok")
#except Exception as e:
#    print("Da co loi xay ra, co the db connection bi sai !")

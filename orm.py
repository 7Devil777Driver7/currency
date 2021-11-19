import sqlite3

connection = sqlite3.connect('/db.sqlite3')
connection.row_factory = sqlite3.Row
cur = connection.cursor()

sql = '''
select ID, EmailFrom, Subject, Message from Contacts
'''

cur.execute(sql)
results = cur.fetchall()
connection.close()


class User():
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def save(self):
        connection = sqlite3.connect('/db.sqlite3')
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()

        sql = '''
        UPDATE Contacts SET 
            EmailFrom =, 
            Subject =, 
            Message = .
        WHERE
            ID = {self.ID}
        '''

        cur.execute(sql)
        connection.commit()
        connection.close()



users = [
    User(**data) for data in results
]


#for user in results:
#    print(dict(user))

print(u1.get_full_name)


# CREATE TABLE ContactUs (
#     ID INTEGER PRIMARY KEY,
#     EmailFrom varchar(60),
#     Subject varchar(255),
#     Message VARCHAR(5000)
# );
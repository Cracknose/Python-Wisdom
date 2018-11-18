import sqlite3

""" 
	EXCEPT
		except sqlite3.OperationalError as e:
"""

def init():
	# Check for database file or else create db file
	db = sqlite3.connect("bookmarks.db")
	# Get a cursor object
	cursor = db.cursor()


def create_table():
	cursor.execute('''
	    CREATE TABLE bookmarks(url TEXT PRIMARY KEY, name TEXT, category TEXT, tags TEXT) 
	''')
	db.commit()


def insert_row():
	# Insert a row of data
	cursor.execute("INSERT INTO table VALUES ('value','value','value')")
	db.commit()

def search_table():
	variable = cursor.execute('''SELECT * FROM bookmarks WHERE checked IS NULL ''').fetchone()
	variable = cursor.execute("SELECT * FROM blacklist WHERE domain=?", (s_url,)).fetchone()
	

def update_value():
	cursor.execute("UPDATE table SET column1=?, column2=? WHERE column3=?", (uPrice, uDate, uId))

def add_bookmark(value1, value2):
	cursor.execute('''INSERT INTO table(column1, column2) 
  					VALUES(?,?)''', (value1, value2))
	db.commit()


def ending():
	try:
		# write code with a try so a database error wont crash everything
	except:
		# awlays end a session with db.close()
		db.close()

import sqlite3

conn = sqlite3.connect("finance.db")
conn.execute("CREATE TABLE IF NOT EXISTS portfolio(name text, shares integer, price text, total text, symbol text, id integer)")
conn.execute("CREATE TABLE IF NOT EXISTS histories(symbol text, shares text, price text, transacted datetime default CURRENT_TIMESTAMP, id integer)")
conn.execute("CREATE TABLE IF NOT EXISTS users(id integer primary key AUTO_INCREMENT not null, username text not null, cash numeric not null default 10000.00, hash text not null)")
conn.execute("CREATE UNIQUE INDEX username ON users(username)")
conn.commit()
conn.close()
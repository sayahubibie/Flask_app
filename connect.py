from flask import Flask,render_template
import sqlite3

conn = sqlite3.connect('sqlite-sakila.db')
conn.row_factory = sqlite3.Row 
print('Open the database successfully')

cur = conn.cursor()


app = Flask(__name__)


@app.route('/customer')
def sql_data():
    conn = sqlite3.connect('sqlite-sakila.db')
    conn.row_factory = sqlite3.Row
    print('------Opened the database successfully in our function')

    cur = conn.cursor()
    #sql="""select customer_id,store_id,first_name,last_name,email,address_id,active,create_date,last_update  from customer"""
    sql="""select * from customer """
    # sql = """select customer_id,store_id,first_name,last_name,create_date,last_update from customer"""
    print(sql)

    cur.execute(sql)
    result = cur.fetchall()
    #print('sql data : ', result)

    return render_template('test.html',test=result)


#sql_data()
#app.run(debug=True)
if __name__=='__main__':
    app.run(port=4005)
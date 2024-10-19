#N7y
import argparse
import pandas as pd
import sqlite3
import MySQLdb
import sys


def xl2html(excel_file):
    df = pd.read_excel(excel_file)
    return generate(df)


def sqli2html(db_file, table_name):
    conn = sqlite3.connect(db_file)
    # check valid tabl
    query = f"SELECT * FROM {table_name}" 
    df = pd.read_sql_query(query, conn)
    return generate(df)





def sql2html(db_host, db_user, db_password, db_name, table_name):
    conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    rows = cursor.fetchall()
    col = [i[0] for i in cursor.description]
    df = pd.DataFrame(rows, columns=col)
    return generate(df)

def generate(df):
    html_table = df.to_html(index=False, classes='fancy-table', border=0)
    p1_html = '''
    <html>
    <head>
        <style>
            .fancy-table {
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 18px;
                text-align: left;
                border: 1px solid #ddd;
            }
            .fancy-table th, .fancy-table td {
                padding: 12px 15px;
                border: 1px solid #ddd;
            }
            .fancy-table th {
                background-color: #f4b084;
                color: white;
            }
            .fancy-table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            section {
                padding: 20px;
                border: 2px solid #4CAF50;
                background-color: #f9f9f9;
            }
        </style>
    </head>
    <body>
        <section>
    '''
    p2_html = '''
            </section>
        </body>
        </html>
    '''
    full_html = p1_html + html_content + p2_html 
    html = f'''
        <section>
            \t{html_table}
        </section>
    '''
    css = '''
    <style>
            .fancy-table {
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 18px;
                text-align: left;
                border: 1px solid #ddd;
            }
            .fancy-table th, .fancy-table td {
                padding: 12px 15px;
                border: 1px solid #ddd;
            }
            .fancy-table th {
                background-color: #f4b084;
                color: white;
            }
            .fancy-table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            section {
                padding: 20px;
                border: 2px solid #4CAF50;
                background-color: #f9f9f9;
            }
        </style>
    '''
    return html, css, full_html



if len(sys.argv) == 1:
    print("""
            \r \r  Convert data from Excel, SQLite, or MySQL into an HTML table
\t\t\t\t\t Auther: N7y

[...     [..                   
[. [..   [..[..... [..         
[.. [..  [..      [.. [..   [..
[..  [.. [..     [..   [.. [.. 
[..   [. [..    [..      [...  
[..    [. ..    [..       [..  
[..      [..    [..      [..   
                       [..  

    \r Usage is very human just
    \r python3 table.py --help # for more info

        """)
    exit()

parser = argparse.ArgumentParser(description="Convert data from Excel, SQLite, or MySQL into an HTML table.")
parser.add_argument('--option', type=str, required=True, choices=['excel', 'sqlite', 'mysql'], help="Choose the data source: 'excel', 'sqlite', or 'mysql'.")
parser.add_argument('--excel-file', type=str, help="Path to the excel file")

parser.add_argument('--sqlite-db', type=str, help="Path to the SQLite database file")
parser.add_argument('--table-name', type=str, help="Table name to extract data from ")

parser.add_argument('--mysql-host', type=str, help="mysql host")
parser.add_argument('--mysql-user', type=str, help="mysql username ")
parser.add_argument('--mysql-password', type=str, help="mysql password ")
parser.add_argument('--mysql-db', type=str, help="mysql db name")

args = parser.parse_args()

if args.option == 'excel' and args.excel_file:
    html, css ,html_content = xl2html(args.excel_file)
elif args.option == 'sqlite' and args.sqlite_db and args.table_name:
    html, css ,html_content = sqli2html(args.sqlite_db, args.table_name)
elif args.option == 'mysql' and args.mysql_host and args.mysql_user and args.mysql_password and args.mysql_db and args.table_name:
    html, css, html_content = sql2html(args.mysql_host, args.mysql_user, args.mysql_password, args.mysql_db, args.table_name)
else:
    print("Unknown info exiting...")
    exit()



print(html)
print(css)
print("\n\n \t\t Full Content\n")
print(html_content)








#N7y
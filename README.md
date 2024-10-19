# table2html
Convert data from excel, sqlite, or mysql into an html table


```sh
└──╼ $python3 table.py --help
usage: table.py [-h] --option {excel,sqlite,mysql} [--excel-file EXCEL_FILE] [--sqlite-db SQLITE_DB] [--table-name TABLE_NAME] [--mysql-host MYSQL_HOST] [--mysql-user MYSQL_USER]
                [--mysql-password MYSQL_PASSWORD] [--mysql-db MYSQL_DB]

Convert data from Excel, SQLite, or MySQL into an HTML table.

optional arguments:
  -h, --help            show this help message and exit
  --option {excel,sqlite,mysql}
                        Choose the data source: 'excel', 'sqlite', or 'mysql'.
  --excel-file EXCEL_FILE
                        Path to the excel file
  --sqlite-db SQLITE_DB
                        Path to the SQLite database file
  --table-name TABLE_NAME
                        Table name to extract data from
  --mysql-host MYSQL_HOST
                        mysql host
  --mysql-user MYSQL_USER
                        mysql username
  --mysql-password MYSQL_PASSWORD
                        mysql password
  --mysql-db MYSQL_DB   mysql db name

```

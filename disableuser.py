# Wil Coiner
# 2/10/19
# Disables user in all cloud systems
# Requires source database list to be a CSV with 4 columns for driver, server, uid, and pwd

import pyodbc
import csv

def disable_user(username,list_of_dbs):
    """Disables user in all databases in list"""
    for db in list_of_dbs[1:]:
        try:
            cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server="+db[0]+";"
                        "Database="+db[1]+";"
                        "uid="+db[2]+";pwd="+db[3])
            crsr = cnxn.cursor()
            sql_command = "UPDATE Principal SET IsEnabled = 'False' WHERE loginname ='" + username + "'"
            crsr.execute(sql_command)
            print(crsr.rowcount, 'users disabled')
            cnxn.commit()
            crsr.close()
            cnxn.close()
            print("SQL executed successfully, disabled",username,"from",db[1])
            sqlresults = str("SQL executed successfully, disabled " + username + " from " + db[1] + '\n')
            with open('SQL_Results.txt', 'w') as outfile:
                outfile.write(sqlresults)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '28000':
                print("LDAP Connection failed: check database and login credentials")


def main():
    databasename = str(input("Enter the full file path of database file: "))
    while  1 == 1:
        username = str(input("Enter the username: "))
        with open(databasename, 'r') as infile:
            reader = csv.reader(infile)
            list_of_dbs = list(reader)
        disable_user(username,list_of_dbs)



if __name__ == '__main__':
    main()



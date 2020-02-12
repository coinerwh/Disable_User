# Wil Coiner
# 2/10/19
# Disables user in all cloud systems.
# Requires source database list to be a CSV with 4 columns for driver, server, uid, and pwd


import pyodbc
import pandas as pd
import csv

def disable_user(username,list_of_dbs):
    """Disables user in all databases in list"""
    for db in list_of_dbs[1:]:
        try:
            cnxn = pyodbc.connect("Driver={SQL Server};"
                        "Server="+db[0]+";"
                        "Database="+db[1]+";"
                        "uid="+db[2]+";pwd="+db[3])
            query = "SELECT * FROM Principal WHERE loginname ='" + username + "'"
            return pd.read_sql_query(query, cnxn)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '28000':
                print("LDAP Connection failed: check database and login credentials")


def main():
    bad_credentials = True
    while bad_credentials == True:
        databasename = str(input("Enter the full file path of database file: "))
        username = str(input("Enter the username: "))
        with open(databasename, 'r') as infile:
            reader = csv.reader(infile)
            list_of_dbs = list(reader)
        sqlresults = disable_user(username,list_of_dbs)
        print(sqlresults)


if __name__ == '__main__':
    main()

### Code that writes to file if successful. Loops if unable to execute ###

# if sqlresults == None:
    # bad_credentials = True
# else:
    # print(sqlresults)
    # with open('SQL_Results.txt','w') as outfile:
        #outfile.write(sqlresults)
    # bad_credentials = False

### Dynamic and hardcoded connection code ###

#pyodbc.connect("Driver={SQL Server};"
                    #"Server="+db[0]+";"
                    #"Database="+db[1]+";"
                    #"uid="+db[2]+";pwd="+db[3])

#cnxn = pyodbc.connect("Driver={SQL Server};"
                                  #"Server=axiomepmdb01.database.windows.net;"
                                  #"Database=AxiomSupportTraining;"
                                  #"uid=support_wcoiner;pwd=RhFn++bG69$m,N70")

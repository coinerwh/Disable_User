disableuser runs a SQL script that disables users in a list of databases based on loginname. This was designed for use to expedite an internal process for disabling employees that have left the company.

Reads in a CSV file with a row for each server, database, user ID, and password.
Program loads the file and generates a parent list with a list for each row.
If ran as a script, the program asks the user for the database file name and location along with the user to be deleted.

The script calls the disable_user function, which iterates through the list of databases, tries to connect and run the SQL.
It then prints the rows effected, prints the result, and saves the result to a text file.
If it fails to connect it returns an exception statement.
The program then asks for another loginname until the user exits the program.

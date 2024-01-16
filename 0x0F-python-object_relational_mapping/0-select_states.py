#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    try:
        # Establish the database connection
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        
        # Create a cursor
        c = db.cursor()

        # Execute the query
        c.execute("SELECT * FROM `states`")

        # Fetch all rows and print them
        [print(state) for state in c.fetchall()]

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and database connection in the finally block
        if c:
            c.close()
        if db:
            db.close()

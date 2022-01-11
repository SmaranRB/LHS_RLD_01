import mysql.connector as m
import Program_init as Init
try:
    
    con = m.connect(host = 'localhost',user = 'root',passwd = Init.passwd)
    
    if con.is_connected() == True:
        print('Connection Established')
    else:
        print('Connection not Established')

    mycursor = con.cursor()

    create_database = 'Create database Child_performance'
    mycursor.execute(create_database)
    
    Create_Table = 'Create Table Child_Info (Game_Name varchar(20), Game_Time float(20))'
    mycursor.execute(Create_Table)
    
    #add_data = 'Insert into Child_Info Values('+

    
except:
    pass
else:
    con.close()


#GameName|TotalTimeTaken|Time 
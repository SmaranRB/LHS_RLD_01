import time
import mysql.connector as m
import sys
import Program_init
try:
    Server = m.connect(host = 'localhost', user = 'root', passwd = Program_init.passwd, db = 'autism' )
    
except m.Error:
    print('Error:', m.Error)
    sys.exit()

else:

    def push_data(game, t_time, date = round(time.time(),3)):
        
        cs = Server.cursor()
        cs.execute("insert into user1 values ( '%s' , %d , now() )"%(game,t_time))
        Server.commit()
        cs.close()
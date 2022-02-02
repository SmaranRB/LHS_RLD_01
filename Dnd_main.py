import time
import random
import mysql.connector as m
from Dnd.Dnd_exec import *
import Program_init

try:
    Server = m.connect(host = 'localhost', user = 'root', passwd = Program_init.passwd, db = 'autism')

except Exception() as E:
    print(E)

else:
    
    cs = Server.cursor()
    stime = time.time()
    
    L = ['Fish()', "Ball()" , "Book()"]
    M = ["Elephants()" , "Shapes()"]

    # ----- random select -----

    a = random.choice(L)
    eval(a)
    L.remove(a)
    b = random.choice(L)
    eval(b)
    c = random.choice(M)
    eval(c)

    # ----- sql values -----

    ftime = time.time()
    Ttime = round(ftime - stime,3)
    cs.execute("insert into user1 values ('dnd',%d,now())"%(Ttime))
    Server.commit()

    cs.close()
    Server.close()

    #pygame.quit

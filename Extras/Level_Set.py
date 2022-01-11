'''
exec(open("1-Fish.py").read())
exec(open("2-Ball.py").read())
exec(open("3-Book.py").read())
exec(open("4-Elephants.py").read())
exec(open("5-Shapes.py").read())
'''

inp=''
print("\nWelcome to Drag and Drop game!\nLevels : 1 , 2 , 3 , 4 , 5\nEnter 'exit' to escape.")

while inp.lower()!='exit':
   try:
      inp = input("\nEnter level : ")

      if inp == "1":
         exec(open(r".\Dnd\1-Fish.py").read())
      elif inp == "2":
         exec(open(r".\Dnd\2-Ball.py").read())
      elif inp == "3":
         exec(open(r".\Dnd\3-Book.py").read())
      elif inp == "4":
         exec(open(r".\Dnd\4-Elephants.py").read())
      elif inp == "5":
         exec(open(r".\Dnd\5-Shapes.py").read())

      elif inp.lower()=="playall":
         exec(open(r".\Dnd\1-Fish.py").read())
         exec(open(r".\Dnd\2-Ball.py").read())
         exec(open(r".\Dnd\3-Book.py").read())
         exec(open(r".\Dnd\4-Elephants.py").read())
         exec(open(r".\Dnd\5-Shapes.py").read())
         print("(all games done)")
      pygame.quit()
   except:
         pass
   
print("\nThank you for playing!\n")

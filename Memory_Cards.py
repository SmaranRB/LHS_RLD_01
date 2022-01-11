def Memory_cards():

    import Memory_cards.Program_init as Init
    import Memory_cards.Main_logic_2x2 as L1
    import Memory_cards.Main_logic_2x3 as L2
    import Memory_cards.MySQL_connector as MySQL
    import time
    
    Path_addn = 'Memory_cards'

    screen = L1.Load_Screen(1280,720)
    game = 'mmc'
    #Init.play_intro(screen)

    StartTime = time.time()

    L1.main(['Vegetables\\Radish','Vegetables\\Potato'],'Bg7',screen) # 2x2 Colours-Simple

    L1.main(['Animals\\Elephant','Animals\\Tiger'],'Bg6',screen) # 2x2 Animals-Simple

    L2.main(['Vegetables\\Radish','Vegetables\\Potato','Vegetables\\Carrot'],'Bg7',screen) # 3x3 Colours-Simple

    L2.main(['Animals\\Elephant','Animals\\Tiger','Animals\\Flamingo'],'Bg6',screen,'Hex1') # 3x3 Animals-Simple 

    EndTime = time.time()
    MySQL.push_data(game, round(EndTime - StartTime,3))
            

Memory_cards()
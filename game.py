loc11, loc12, loc13 = " ", " ", " "
loc21, loc22, loc23 = " ", " ", " "
loc31, loc32, loc33 = " ", " ", " "

def table():
    print(f"{loc11} | {loc12} | {loc13}")
    print(f"--+---+--")
    print(f"{loc21} | {loc22} | {loc23}")
    print(f"--+---+--")
    print(f"{loc31} | {loc32} | {loc33}")
    
def check_if_exist(cell_name):
    if len(cell_name.strip()) == 0:
        return False
    elif len(cell_name.strip()) != 0:
        return True

def insert_mark(player):
    
    global loc11, loc12, loc13
    global loc21, loc22, loc23
    global loc31, loc32, loc33
    
    print(f"Player {player}:")
    while True:
        first_cell = int(input("Enter first cell id (1-3): "))
        second_cell = int(input("Enter second cell id (1-3): "))
        
        if first_cell > 3 or second_cell > 3 or first_cell <= 0 or second_cell <= 0:
            print("Invalid move. Try again.")
        else:
            if first_cell == 1 and second_cell == 1:
                checked = check_if_exist(loc11)
                if checked == False:
                    loc11 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 1 and second_cell == 2:
                checked = check_if_exist(loc12)
                if checked == False:
                    loc12 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 1 and second_cell == 3:
                checked = check_if_exist(loc13)
                if checked == False:
                    loc13 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                    
                    
            elif first_cell == 2 and second_cell == 1:
                checked = check_if_exist(loc21)
                if checked == False:
                    loc21 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 2 and second_cell == 2:
                checked = check_if_exist(loc22)
                if checked == False:
                    loc22 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 2 and second_cell == 3:
                checked = check_if_exist(loc23)
                if checked == False:
                    loc23 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                    
                    
            elif first_cell == 3 and second_cell == 1:
                checked = check_if_exist(loc31)
                if checked == False:
                    loc31 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 3 and second_cell == 2:
                checked = check_if_exist(loc32)
                if checked == False:
                    loc32 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 3 and second_cell == 3:
                checked = check_if_exist(loc33)
                if checked == False:
                    loc33 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
        
                
def check_win_or_tie(player):
    if loc11.strip() == loc12.strip() == loc13.strip() and loc11 != " ":
        print(f"Player {player} wins!")
        return True
    elif loc21.strip() == loc22.strip() == loc23.strip() and loc21 != " ":
        print(f"Player {player} wins!")
        return True
    elif loc31.strip() == loc32.strip() == loc33.strip() and loc31 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif loc11.strip() == loc21.strip() == loc31.strip() and loc11 != " ":
        print(f"Player {player} wins!")
        return True
    elif loc12.strip() == loc22.strip() == loc32.strip() and loc12 != " ":
        print(f"Player {player} wins!")
        return True
    elif loc13.strip() == loc23.strip() == loc33.strip() and loc13 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif loc11.strip() == loc22.strip() == loc33.strip() and loc11 != " ":
        print(f"Player {player} wins!")
        return True
    elif loc13.strip() == loc22.strip() == loc31.strip() and loc13 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif (loc11 != " " and loc12 != " " and loc13 != " " and
            loc21 != " " and loc22 != " " and loc23 != " " and
            loc31 != " " and loc32 != " " and loc33 != " "):
        print("It's a draw!")
        return True

table()
while True:
    insert_mark("X")
    table()
    res_x = check_win_or_tie("X")
    if res_x == True:
        break
    
    insert_mark("O")
    table()
    res_o = check_win_or_tie("O")
    if res_o == True:
        break

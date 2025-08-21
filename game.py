a1, a2, a3 = " ", " ", " "
b1, b2, b3 = " ", " ", " "
c1, c2, c3 = " ", " ", " "

def table():
    print(f"{a1} | {a2} | {a3}")
    print(f"--+---+--")
    print(f"{b1} | {b2} | {b3}")
    print(f"--+---+--")
    print(f"{c1} | {c2} | {c3}")
    
def check_if_exist(cell_name):
    # print(cell_name)
    if len(cell_name.strip()) == 0:
        return False
    elif len(cell_name.strip()) != 0:
        return True

def insert_mark(player):
    
    global a1, a2, a3
    global b1, b2, b3
    global c1, c2, c3
    
    print(f"Player {player}:")
    while True:
        first_cell = int(input("Enter first cell id (1-3): "))
        second_cell = int(input("Enter second cell id (1-3): "))
        
        if first_cell > 3 or second_cell > 3 or first_cell <= 0 or second_cell <= 0:
            print("Invalid move. Try again.")
        else:
            if first_cell == 1 and second_cell == 1:
                checked = check_if_exist(a1)
                if checked == False:
                    a1 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 1 and second_cell == 2:
                checked = check_if_exist(a2)
                if checked == False:
                    a2 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 1 and second_cell == 3:
                checked = check_if_exist(a3)
                if checked == False:
                    a3 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                    
                    
            elif first_cell == 2 and second_cell == 1:
                checked = check_if_exist(b1)
                if checked == False:
                    b1 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 2 and second_cell == 2:
                checked = check_if_exist(b2)
                if checked == False:
                    b2 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 2 and second_cell == 3:
                checked = check_if_exist(b3)
                if checked == False:
                    b3 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                    
                    
            elif first_cell == 3 and second_cell == 1:
                checked = check_if_exist(c1)
                if checked == False:
                    c1 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 3 and second_cell == 2:
                checked = check_if_exist(c2)
                if checked == False:
                    c2 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
                
            elif first_cell == 3 and second_cell == 3:
                checked = check_if_exist(c3)
                if checked == False:
                    c3 = str(player)
                    break
                else:
                    print("Cell already taken. Try again.")
        
                
def check_win_or_tie(player):
    if a1.strip() == a2.strip() == a3.strip() and a1 != " " and a2 != " "and a3 != " ":
        print(f"Player {player} wins!")
        return True
    elif b1.strip() == b2.strip() == b3.strip() and b1 != " " and b2 != " "and b3 != " ":
        print(f"Player {player} wins!")
        return True
    elif c1.strip() == c2.strip() == c3.strip() and c1 != " " and c2 != " "and c3 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif a1.strip() == b1.strip() == c1.strip() and a1 != " " and b1 != " "and c1 != " ":
        print(f"Player {player} wins!")
        return True
    elif a2.strip() == b2.strip() == c2.strip() and a2 != " " and b2 != " "and c2 != " ":
        print(f"Player {player} wins!")
        return True
    elif a3.strip() == b3.strip() == c3.strip() and a3 != " " and b3 != " "and c3 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif a1.strip() == b2.strip() == c3.strip() and a1 != " " and b2 != " "and c3 != " ":
        print(f"Player {player} wins!")
        return True
    elif a3.strip() == b2.strip() == c1.strip() and a3 != " " and b2 != " "and c1 != " ":
        print(f"Player {player} wins!")
        return True
    
    elif a1 != " " and a2 != " " and a3 != " " and b1 != " " and b2 != " " and b3 != " " and c1 != " " and c2 != " " and c3 != " ":
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
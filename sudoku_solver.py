import numpy as np
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))
n4 = int(input("n4: "))
n5 = int(input("n5: "))
n6 = int(input("n6: "))
n7 = int(input("n7: "))
n8 = int(input("n8: "))
n9 = int(input("n9: "))
n10 = int(input("n10: "))
n11 = int(input("n11: "))
n12 = int(input("n12: "))
n13 = int(input("n13: "))
n14 = int(input("n14: "))
n15 = int(input("n15: "))
n16 = int(input("n16: "))
n17 = int(input("n17: "))
n18 = int(input("n18: "))
n19 = int(input("n19: "))
n20 = int(input("n20: "))
n21 = int(input("n21: "))
n22 = int(input("n22: "))
n23 = int(input("n23: "))
n24 = int(input("n24: "))
n25 = int(input("n25: "))
n26 = int(input("n26: "))
n27 = int(input("n27: "))
n28 = int(input("n28: "))
n29 = int(input("n29: "))
n30 = int(input("n30: "))
n31 = int(input("n31: "))
n32 = int(input("n32: "))
n33 = int(input("n33: "))
n34 = int(input("n34: "))
n35 = int(input("n35: "))
n36 = int(input("n36: "))
n37 = int(input("n37: "))
n38 = int(input("n38: "))
n39 = int(input("n39: "))
n40 = int(input("n40: "))
n41 = int(input("n41: "))
n42 = int(input("n42: "))
n43 = int(input("n43: "))
n44 = int(input("n44: "))
n45 = int(input("n45: "))
n46 = int(input("n46: "))
n47 = int(input("n47: "))
n48 = int(input("n48: "))
n49 = int(input("n49: "))
n50 = int(input("n50: "))
n51 = int(input("n51: "))
n52 = int(input("n52: "))
n53 = int(input("n53: "))
n54 = int(input("n54: "))
n55 = int(input("n55: "))
n56 = int(input("n56: "))
n57 = int(input("n57: "))
n58 = int(input("n58: "))
n59 = int(input("n59: "))
n60 = int(input("n60: "))
n61 = int(input("n61: "))
n62 = int(input("n62: "))
n63 = int(input("n63: "))
n64 = int(input("n64: "))
n65 = int(input("n65: "))
n66 = int(input("n66: "))
n67 = int(input("n67: "))
n68 = int(input("n68: "))
n69 = int(input("n69: "))
n70 = int(input("n70: "))
n71 = int(input("n71: "))
n72 = int(input("n72: "))
n73 = int(input("n73: "))
n74 = int(input("n74: "))
n75 = int(input("n75: "))
n76 = int(input("n76: "))
n77 = int(input("n77: "))
n78 = int(input("n78: "))
n79 = int(input("n79: "))
n80 = int(input("n80: "))
n81 = int(input("n81: "))
sudoku_grid = [[n1,n2,n3,n4,n5,n6,n7,n8,n9],
               [n10,n11,n12,n13,n14,n15,n16,n17,n18],
               [n19,n20,n21,n22,n23,n24,n25,n26,n27],
               [n28,n29,n30,n31,n32,n33,n34,n35,n36],
               [n37,n38,n39,n40,n41,n42,n43,n44,n45],
               [n46,n47,n48,n49,n50,n51,n52,n53,n54],
               [n55,n56,n57,n58,n59,n60,n61,n62,n63],
               [n64,n65,n66,n67,n68,n69,n70,n71,n72],
               [n73,n74,n75,n76,n77,n78,n79,n80,n81]]
print(sudoku_grid)
print(np.matrix(sudoku_grid)) 
def viable(y,x,n):
    global sudoku_grid
    for i in range(0,9):
        if sudoku_grid[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku_grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_grid[y0+i][x0+i] == n:
                return False
    return True
def solveGrid():
    global sudoku_grid
    for y in range(9):
        for x in range(9):
            if sudoku_grid[y][x] == 0:
                for n in range(1,10):
                    if viable(y,x,n) :
                        sudoku_grid[y][x] = n
                        solveGrid()
                        sudoku_grid[y][x] = 0
                return
    print(np.matrix(sudoku_grid))
    input("Resolve?: ")
solveGrid()

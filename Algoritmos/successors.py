# 1 2 3
# 4 5 6 
# 7 8 9

def x3(n):
	if (n == 1): return [2, 4, 5]
	elif (n == 2): return [1, 3, 4, 5, 6]
	elif (n == 3): return [2, 5, 6]
	elif (n == 4): return [1, 2, 5, 7, 8]
	elif (n == 5): return [1, 2, 3, 4, 6, 7, 8, 9]
	elif (n == 6): return [2, 3, 5, 8,9]
	elif (n == 7): return [4, 5, 8]
	elif (n == 8): return [4, 5, 6, 7, 9]
	elif (n == 9): return [5, 6, 8]
	else: return None
	
# 1  2  3  4
# 5  6  7  8 
# 9  10 11 12
# 13 14 15 16

def x4(n):
    if (n == 1): return [2, 5, 6]
    elif (n == 2): return [1, 3, 5, 6, 7]
    elif (n == 3): return [2, 4, 6, 7, 8]
    elif (n == 4): return [3, 7, 8]
    elif (n == 5): return [1, 2, 6, 9, 10]
    elif (n == 6): return [1, 2, 3, 5, 7, 9, 10, 11]
    elif (n == 7): return [2, 3, 4, 6, 8, 10, 11, 12]
    elif (n == 8): return [3, 4, 7, 11, 12]
    elif (n == 9): return [5, 6, 10, 13, 14]
    elif (n == 10): return [5, 6, 7, 9, 11, 13, 14, 15]
    elif (n == 11): return [6, 7, 8, 10, 12, 14, 15, 16]
    elif (n == 12): return [7, 8, 11, 15, 16]
    elif (n == 13): return [9, 10, 14]
    elif (n == 14): return [9, 10, 11, 13, 15]
    elif (n == 15): return [10, 11, 12, 14, 16]
    elif (n == 16): return [11, 12, 15]
    else: return None

def custom(n):
    if (n == 1): return [2, 3, 4]
    elif (n == 2): return [1, 4, 5]
    elif (n == 3): return [1, 4, 6]
    elif (n == 4): return [1, 2, 3, 5, 6, 7]
    elif (n == 5): return [2, 4, 7]
    elif (n == 6): return [3, 4, 7]
    elif (n == 7): return [4, 5, 6]
    else: return None
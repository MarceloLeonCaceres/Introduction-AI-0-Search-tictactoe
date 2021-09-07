"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    conteo_X = 0
    conteo_O = 0
    for fila in board:
        for celda in fila:
            if celda == X:
                conteo_X +=1
            if celda == O:
                conteo_O +=1
    #print( 'Número de X: ',  conteo_X)
    #print( 'Número de O: ',  conteo_O)
    if conteo_X == conteo_O:
        #print('Juega X')
        return X
    else:
        #print('Juega O')
        return O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    j = 0
    posibles = []
    for fila in board:
        j = 0
        for celda in fila:
            if celda == EMPTY:
                posibles.append((i,j))
            j+=1
        i+=1
    return posibles
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultado = copy.deepcopy(board)
    i, j = action
    if resultado[i][j] != EMPTY:
        raise NotImplementedError
    else:
        resultado[i][j] = player(board)
    return resultado
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    j=0
    for j in range(0,3):
        if board[0][j] == board[1][j] and board[0][j] == board[2][j] and board[0][j] != EMPTY:
            return board[0][j]
            #print ('ganó ', board[0][j])
    i=0
    for i in range(0,3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
            #print ('ganó ', board[i][0])
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] != EMPTY:
        return board[1][1]
        #print ('ganó ', board[1][1])
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    contador = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                contador +=1
    if contador == 0:
        return True

    if winner(board) == None:
        return False
    else:
        return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    posibles = actions(board)
    mejor_movida = copy.deepcopy(posibles[0])

    if player(board) == X:    
        v_mejor_movida = Min_Value(result(board,mejor_movida))
        for jugada in posibles:
            if jugada != mejor_movida:
                v_jugada = Min_Value(result(board,jugada))
                if  v_jugada > v_mejor_movida:
                    mejor_movida = jugada
                    v_mejor_movida = v_jugada

    if player(board) == O:    
        v_mejor_movida = Max_Value(result(board,mejor_movida))
        for jugada in posibles:
            if jugada != mejor_movida:
                v_jugada = Max_Value(result(board,jugada))
                if v_jugada < v_mejor_movida:
                    mejor_movida = jugada
                    v_mejor_movida = v_jugada
    
    return mejor_movida
    #raise NotImplementedError

def Max_Value(board):
    if terminal(board):
        #print('jugó X: ', board, '     Max_value     utility =', utility(board))
        return utility(board)
    else:
        v = -100
        #print('Max_Value: Opciones:', actions(board))
        for action in actions(board):
            v = max(v, Min_Value(result(board,action)))
        return v

def Min_Value(board):
    if terminal(board):
        #print('jugó O: ', board, '     Min_value   utility =', utility(board))
        return utility(board)
    else:
        v = 100
        #print('\ntablero: ', board,' Min_Value: Opciones:', actions(board))
        for action in actions(board):
            v = min(v, Max_Value(result(board,action)))
        return v
import numpy as np

def bingo_card(n, min_entry=1, max_entry=50):
    '''
        Create a (n, n, 2) matrix whose layer (:, :, 0) is the entries on a bingo card and layer (:, :, 1) stores
        whether an entry has been called (1) or uncalled (0.)

        n : int
            The length of the square bingo card. 

        min_entry=1 : int
            The minimum integer an entry can be.

        max_entry=1 : int
            The maximum integer (inclusive) an entry can be.

        return : arraylike
            Bingo card.
    '''
    entries_layer = np.random.randint(low=min_entry, high=max_entry+1, size=(n, n))
    called_layer = np.zeros((n, n))
    return np.dstack((entries_layer, called_layer))

def check_bingo(bc):
    '''
        Given a bingo card matrix bc, check if the bingo card has a valid bingo entry. Since we assume all bingo cards
        are n x n, there are n "n in a row," n "n in a column," and 2 diagonals, totaling to 2n + 2 win conditions.

        bc : arraylike
            A bingo card object to be checked.

        return : bool
            Whether a bingo card has won (True), otherwise False.
    '''
    called = bc[:, :, 1]
    n = called.shape[0]
    win_vector = np.ones(n)
    if (called @ win_vector).max() >= n:
        return 1
    elif (called.T @ win_vector).max() >= n:
        return 1
    elif np.trace(called) >= n:
        return 1
    elif np.trace(np.fliplr(called)) >= n:
        return 1
    else:
        return 0

def round_pick(bc_arr, min_entry=1, max_entry=50):
    '''
        Pick a random integer between min_entry and max_entry and a random integer between 1 and n 
        (the length of the bingo card.) If a bingo card has the random integer
        as an entry, change the corresponding entry in the called layer to a 1.

        bc : arraylike
            Bingo card.
        min_entry=1 : int
            The minimum integer an entry can be.

        max_entry=1 : int
            The maximum integer (inclusive) an entry can be.

        return : (?)
    '''
    pass

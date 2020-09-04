def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}  

    for i in range(length):
        x = limit - weights[i]

        if x in cache:
            return(max(i, cache[x]), min(i, cache[x]))

        else:
            cache[weights[i]] = i

    return None

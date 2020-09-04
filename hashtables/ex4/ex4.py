def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for x in a:
        if abs(x) in cache:
            result.append(abs(x))

        else:
            cache[abs(x)] = 1


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

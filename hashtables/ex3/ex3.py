def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for x in arrays:
        for n in x:
            if n in cache:
                cache[n] += 1

            else:
                cache[n] = 1

    for n in cache:
        if cache[n] == len(arrays):
            result.append(n)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

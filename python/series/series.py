def slices(series, length):

    # length cannot be longer than the series, and must be natural number
    if len(series) < length or length < 1:
        raise ValueError("input not valid")

    # subsets of series
    subset = []

    for i in range(len(series)-(length-1)):
        subset.append(series[i:i+length])

    return subset

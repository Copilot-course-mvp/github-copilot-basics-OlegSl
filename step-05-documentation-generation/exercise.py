def chunk_list(values: list[int], size: int) -> list[list[int]]:
    """Split a list of integers into chunks of a given size.

    Parameters:
        values (list[int]): The list of integers to be divided into chunks.
        size (int): The size of each chunk. Must be a positive integer.

    Returns:
        list[list[int]]: A list containing sublists, where each sublist is a chunk
            of the specified size from the original list. The last chunk may be
            smaller if the list length is not evenly divisible by the chunk size.

    Raises:
        ValueError: If size is less than or equal to 0.
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    return [values[index : index + size] for index in range(0, len(values), size)]


def moving_average(values: list[float], window: int) -> list[float]:
    """Computes the moving average of a list of values over a specified window size.

    Parameters:
        values (list[float]): The list of numerical values to compute moving averages for.
        window (int): The size of the moving average window. Must be a positive integer.

    Returns:
        list[float]: A list containing the moving averages. If the window size is larger
            than the length of the input list, an empty list is returned.

    Raises:
        ValueError: If window is less than or equal to 0.
    """
    if window <= 0:
        raise ValueError("window must be > 0")
    if window > len(values):
        return []
    result: list[float] = []
    for index in range(len(values) - window + 1):
        current = values[index : index + window]
        result.append(sum(current) / window)
    return result
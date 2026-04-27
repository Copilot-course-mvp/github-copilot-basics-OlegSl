# Usage Guide

This document provides usage examples and documentation for the `chunk_list` and `moving_average` functions.

## chunk_list

Splits a list of integers into chunks of a specified size.

### Parameters

| Parameter | Type       | Description                          |
|-----------|------------|--------------------------------------|
| values    | list[int]  | The list of integers to be chunked.  |
| size      | int        | The size of each chunk (must be > 0).|

### Return Value

Returns a `list[list[int]]` containing sublists where each sublist is a chunk of the specified size. The last chunk may be smaller if the list length is not evenly divisible by the chunk size.

### Examples

**Example 1: Basic chunking**
```python
from exercise import chunk_list

data = [1, 2, 3, 4, 5, 6, 7]
result = chunk_list(data, 3)
print(result)  # Output: [[1, 2, 3], [4, 5, 6], [7]]
```

**Example 2: Chunking with uneven division**
```python
from exercise import chunk_list

data = [1, 2, 3, 4, 5]
result = chunk_list(data, 2)
print(result)  # Output: [[1, 2], [3, 4], [5]]
```

## moving_average

Computes the moving average of a list of values over a specified window size.

### Parameters

| Parameter | Type         | Description                                      |
|-----------|--------------|--------------------------------------------------|
| values    | list[float]  | The list of numerical values to compute averages for. |
| window    | int          | The size of the moving average window (must be > 0). |

### Return Value

Returns a `list[float]` containing the moving averages. If the window size is larger than the input list length, returns an empty list.

### Examples

**Example 1: Basic moving average**
```python
from exercise import moving_average

data = [1.0, 2.0, 3.0, 4.0, 5.0]
result = moving_average(data, 3)
print(result)  # Output: [2.0, 3.0, 4.0]
```

**Example 2: Moving average with larger window**
```python
from exercise import moving_average

data = [1.0, 2.0, 3.0]
result = moving_average(data, 2)
print(result)  # Output: [1.5, 2.5]
```

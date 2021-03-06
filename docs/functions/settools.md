[Source](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

## Set Basics

Tools for basic set usages.

### `addtoset`

`addtoset(s, x)` checks whether adding `x` to set `s` is successful.

``` python
s = set()

addtoset(s, 1)
# True

addtoset(s, 1)
# False
```

## Set Matching

Tools for matching sets.

### `bestsubset`

`bestsubset(a, key)` finds the best sub-set of `a` that maximizes the key function `key`.

``` python
bestsubset({1, -2, 3, -4, 5, -6}, sum)
#          {1,     3,     5}
```

### `setcover`

`setcover(whole, covered, key=len)` solves the [set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) by covering the universe set `whole` as best as possible, using a subset of the covering sets `covered`.

- In default, the size of each set `len` is used as key function `key` to measure the coverage.

!!! warning
    This is an approximate algorithm, which means the returned result is not always the best.

``` python
list(setcover(
    { 1, 2, 3,         4,         5},
    [{1, 2, 3}, {2, 3, 4}, {2, 4, 5}]
))
# [frozenset({1, 2, 3}), frozenset({2, 4, 5})]
```

## Set Similarity

Tools for set similarities.

### `jaccard`

`jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

### `multisetjaccard`

`multisetjaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two multi-sets (Counters) `a` and `b`.

### `weightedjaccard`

`weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

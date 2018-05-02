[![PyPI version](https://img.shields.io/pypi/v/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/extratools.svg)](https://pypi.python.org/pypi/extratools/)
[![PyPI license](https://img.shields.io/pypi/l/extratools.svg)](https://pypi.python.org/pypi/extratools/)

Extra functional tools that go beyond standard libraries `itertools`, `functools`, etc. and popular third-party libraries like [`toolz`](https://github.com/pytoolz/toolz), [`fancy`](https://github.com/Suor/funcy), and [`more-itertools`](https://github.com/erikrose/more-itertools).

- Like `toolz` and others, most of the tools are designed to be efficient, pure, and lazy.

- Several useful yet non-functional tools are also included.

- While `toolz` and others target basic scenarios, many tools in this library target more advanced and complete scenarios.

This library is under active development, and new functions will be added on regular basis.

- Any idea or contribution is highly welcome.

- Currently adopted by [TopSim](https://github.com/chuanconggao/TopSim) and [PrefixSpan-py](https://github.com/chuanconggao/PrefixSpan-py).

# Installation

This package is available on PyPI. Just use `pip3 install -U extratools` to install it.

# Available Tools

[`seqtools`](#seqtools)
[`sortedtools`](#sortedtools)
[`strtools`](#strtools)
[`rangetools`](#rangetools)
[`dicttools`](#dicttools)
[`settools`](#settools)
[`tabletools`](#tabletools)
[`mathtools`](#mathtools)
[`stattools`](#stattools)
[`disjointsets`](#disjointsets)
[`misctools`](#misctools)
[`printtools`](#printtools)
[`debugtools`](#debugtools)

<a name="seqtools"></a>
## [`seqtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/seqtools.py)

Tools for matching sequences (including strings), with or without gaps allowed between matching items. Note that empty sequence is always a sub-sequence of any other sequence.

- `findsubseq(a, b)` returns the first position where `a` is a sub-sequence of `b`, or `-1` when not found.

- `issubseq(a, b)` checks if `a` is a sub-sequence of `b`.

- `findsubseqwithgap(a, b)` returns the matching positions where `a` is a sub-sequence of `b`, where gaps are allowed, or `None` when not found.

- `issubseqwithgap(a, b)` checks if `a` is a sub-sequence of `b`, where gaps are allowed.

Tools for comparing sequences (including strings).

- `productcmp(x, y)` compares two sequences `x` and `y` with equal length according to [product order](https://en.wikipedia.org/wiki/Product_order). Returns `-1` if smaller, `0` if equal, `1` if greater, and `None` if not comparable.

    - Throw exception if `x` and `y` have different lengths.

Tools for sorting sequences.

- `sortedbyrank(data, ranks, reverse=False)` returns the sorted list of `data`, according to the respective rank of each individual element in `ranks`.

Tools for encoding/decoding sequences.

- `compress(data, key=None)` compresses the sequence by encoding continuous identical `Item` to `(Item, Count)`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

    - Different from [`itertools.compress`](https://docs.python.org/3.6/library/itertools.html#itertools.compress).

``` python
list(compress([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [(1, 1), (2, 2), (3, 3), (4, 4)]
```

- `decompress(data)` decompresses the sequence by decoding `(Item, Count)` to continuous identical `Item`, according to [run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding).

- `todeltas(data, op=operator.sub)` compresses the sequence by encoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

    - For custom type of item, either define the `-` operator or specify the `op` function computing the difference.

``` python
list(todeltas([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
```

- `fromdeltas(data, op=operator.add)` decompresses the sequence by decoding the difference between previous and current items, according to [delta encoding](https://en.wikipedia.org/wiki/Delta_encoding).

    - For custom type of item, either define the `+` operator or specify the `op` function merging the difference.

<a name="sortedtools"></a>
## [`sortedtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/sortedtools.py)

Tools for sorted sequences.

- `sortedcommon(a, b, key=None)` returns the common elements between `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) & set(b))` but more efficient.

- `sortedalone(a, b, key=None)` returns the elements not in both `a` and `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted((set(a) | set(b)) - (set(a) & set(b)))` but more efficient.

- `sorteddiff(a, b, key=None)` returns the elements only in `a` and not in `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `sorted(set(a) - set(b))` but more efficient.

- `issubsorted(a, b, key=None)` checks if `a` is a sorted sub-sequence of `b`.

    - When both `a` and `b` are sorted sets with no duplicate element, equal to `set(a) <= set(b)` but more efficient.

<a name="strtools"></a>
## [`strtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/strtools.py)

Tools for string transformations.

- `str2grams(s, n, pad=None)` returns the ordered [`n`-grams](https://en.wikipedia.org/wiki/N-gram) of string `s`.

    - Optional padding at the start and end can be added by specifying `pad`. `\0` is usually a safe choice for `pad` when not displaying.

Tools for checksums.

- `sha1sum(f)`, `sha256sum(f)`, `sha512sum(f)`, `md5sum(f)` compute the respective checksum, accepting string, bytes, text file object, and binary file object.

Tools for string matching.

- `tagstats(tags, lines, separator=None)` efficiently computes the number of lines containing each tag.

    - [TagStats](https://github.com/chuanconggao/TagStats) is used to compute efficiently, where the common prefixes among tags are matched only once.

    - `separator` is a regex to tokenize each string. In default when `separator` is `None`, each string is not tokenized.

``` python
tagstats(
    ["a b", "a c", "b c"],
    ["a b c", "b c d", "c d e"]
)
# {'a b': 1, 'a c': 0, 'b c': 2}
```

<a name="rangetools"></a>
### [`rangetools`](https://github.com/chuanconggao/extratools/blob/master/extratools/rangetools.py)

Tools for statistics over ranges. Note that each range is closed on the left side, and open on the right side.

- `histogram(thresholds, data, leftmost=-inf)` computes the [histogram](https://en.wikipedia.org/wiki/Histogram) over all the floats in `data`.

    - The search space is divided by the thresholds of bins specified in `thresholds`.

    - Each bin of the histogram is labelled by its lower threshold.

        - All values in the bin are no less than the current threshold and less than the next threshold.

        - The first bin is labelled by `leftmost`, which is `-inf` in default.

``` python
histogram(
    [0.1, 0.5, 0.8, 0.9],
    [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
)
# {-inf: 1, 0.1: 4, 0.5: 3, 0.8: 1, 0.9: 2}
```

Tools for querying ranges.

- `rangequery(keyvalues, query, func=min)` finds the best value from the covered values in `keyvalues`, if each key in `keyvalues` is within the query range `query`.

    - Implemented by [RangeMinQuery](https://github.com/chuanconggao/RangeMinQuery) to solve the [range minimum query](https://en.wikipedia.org/wiki/Range_minimum_query) problem.

    - `func` defines how the best value is computed, and defaults to `min` for minimum value.

``` python
rangequery(
    {0.1: 1, 0.2: 3, 0.3: 0},
    (0.2, 0.4)
)
# 0
```

Tools for transformations over ranges. Note that each range is closed on the left side, and open on the right side.

- `covers(covered)` merges the covered ranges `covered` to resolve any overlap.

    - Covered ranges in `covered` are sorted by the left side of each range.

``` python
list(covers([(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)]))
# [(-inf, 0), (0.1, 0.2), (0.5, 0.9)]
```

- `gaps(covered, whole=(-inf, inf))` computes the uncovered ranges of the whole range `whole`, given the covered ranges `covered`.

    - Covered ranges in `covered` are sorted by the left side of each range.

    - Overlaps among covered ranges `covered` are resolved, like `covers(covered)`.

``` python
list(gaps(
    [(-inf, 0), (0.1, 0.2), (0.5, 0.7), (0.6, 0.9)],
    (0, 1)
))
# [(0, 0.1), (0.2, 0.5), (0.9, 1)]
```

<a name="dicttools"></a>
### [`dicttools`](https://github.com/chuanconggao/extratools/blob/master/extratools/dicttools.py)

Tools for inverting dictionaries.

- `invertdict(d)` inverts `(Key, Value)` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invertdict_multiple(d)` inverts `(Key, List[Value])` pairs to `(Value, Key)`.

    - If multiple keys share the same value, the inverted directory keeps last of the respective keys.

- `invertdict_safe(d)` inverts `(Key, Value)` pairs to `(Value, List[Key])`.

    - If multiple keys share the same value, the inverted directory keeps a list of all the respective keys.

Tools for remapping elements.

- `remap(data, mapping, key=None)` remaps each unique element in `data` according to function `key`.

    - `mapping` is a dictionary recording all the mappings, optionally containing previous mappings to reuse.

    - In default, `key` returns integers starting from `0`.

``` python
wordmap = {}
db = [list(remap(doc, wordmap)) for doc in docs]
```

<a name="settools"></a>
## [`settools`](https://github.com/chuanconggao/extratools/blob/master/extratools/settools.py)

Tools for set operations.

- `addtoset(s, x)` checks whether adding `x` to set `s` is successful.

Tools for set similarities.

- `jaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`.

- `multisetjaccard(a, b)` computes the [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two multi-sets (Counters) `a` and `b`.

- `weightedjaccard(a, b, key=sum)` computes the weighted [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index) between two sets `a` and `b`, using function `key` to compute the total weight of the elements within a set.

<a name="tabletools"></a>
## [`tabletools`](https://github.com/chuanconggao/extratools/blob/master/extratools/tabletools.py)

Tools for tables.

- `transpose(data)` returns the transpose of table `data`, i.e., switch rows and columns.

    - Useful to switch table `data` from row-based to column-based and backwards.

``` python
transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]
```

- `loadcsv(path)` loads a CSV file, from either a file path or a file object.

- `dumpcsv(path, data)` dumps a table `data` in CSV, to either a file path or a file object.

<a name="mathtools"></a>
## [`mathtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/mathtools.py)

Tools for math.

- `safediv(a, b)` avoids the `division by zero` exception, by returning infinite with proper sign.

    - Closely referring [IEEE Standard 754](https://en.wikipedia.org/wiki/IEEE_754).

<a name="stattools"></a>
## [`stattools`](https://github.com/chuanconggao/extratools/blob/master/extratools/stattools.py)

Tools for statistics.

- `medianabsdev(data)` computes the [median absolute deviation](https://en.wikipedia.org/wiki/Median_absolute_deviation) of a list of floats.

- `entropy(data)` computes the [entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of a list of any items.

    - You can also pass a dictionary of `(item, frequency)` as frequency distribution to `data`.

- `histogram` is alias of a tool in `rangetools`.

<a name="disjointsets"></a>
## [`disjointsets`](https://github.com/chuanconggao/extratools/blob/master/extratools/disjointsets.py)

[Disjoint sets](https://en.wikipedia.org/wiki/Disjoint_sets) with path compression, based a lot on this [implementation](https://www.ics.uci.edu/~eppstein/PADS/UnionFind.py). After `d = DisjointSets()`:

- `d.add(x)` adds a new disjoint set containing `x`.

- `d[x]` returns the representing element of the disjoint set containing `x`.

- `d.disjoints()` returns all the representing elements and their respective disjoint sets.

- `d.union(*xs)` union all the elements in `xs` into a single disjoint set.

<a name="misctools"></a>
## [`misctools`](https://github.com/chuanconggao/extratools/blob/master/extratools/misctools.py)

Tools for miscellaneous purposes.

- `cmp(a, b)` restores the useful `cmp` function previously in Python 2.

    - Implemented according to [What's New in Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html#ordering-comparisons).

- `parsebool(s)` parses a string to boolean, if its lowercase equals to either `1`, `true`, or `yes`.

<a name="printtools"></a>
## [`printtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/printtools.py)

Tools for non-functional but useful printing purposes.

- `print2(*args, **kwargs)` redirects the output of `print` to standard error.

    - The same parameters are accepted.

<a name="debugtools"></a>
## [`debugtools`](https://github.com/chuanconggao/extratools/blob/master/extratools/debugtools.py)

Tools for non-functional but useful debugging purposes.

- `stopwatch()` returns both the duration since program start and the duration since last call in seconds.

    - Technically, the stopwatch starts when `debugtools` is imported.

- `peakmem()` returns the peak memory usage since program start.

    - In bytes on macOS, and in kilobytes on Linux.

#! /usr/bin/env python3

from typing import *

T = TypeVar('T')

from heapq import merge
from itertools import groupby, zip_longest

from toolz.itertoolz import count, unique, sliding_window

from .__join import __sortedjoin, sortedjoin

def sortedcommon(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key
        ):
        yield from (v for v, _ in zip(m, n))


def sortedalone(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    sentinel = object()

    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key,
            leftdefault=sentinel, rightdefault=sentinel
        ):
        yield from (
            v if w is sentinel else w
            for v, w in zip_longest(m, n, fillvalue=sentinel)
            if v != w
        )


def sorteddiff(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> Iterable[T]:
    sentinel = object()

    for m, n in __sortedjoin(
            a, b,
            leftkey=key, rightkey=key,
            rightdefault=sentinel
        ):
        yield from (
            v for v, w in zip_longest(m, n, fillvalue=sentinel)
            if w is sentinel
        )


def issubsorted(
        a: Iterable[T], b: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    sentinel = object()

    return next(iter(sorteddiff(a, b, key=key)), sentinel) is sentinel


def sortedmatch(
        a: List[T], b: List[T],
        default: T = None
    ) -> Tuple[List[T], List[T]]:
    for m, n in __sortedjoin(
            a, b,
            leftdefault=default, rightdefault=default
        ):
        yield from zip_longest(m, n, fillvalue=default)


def issorted(
        seq: Iterable[T],
        key: Callable[[T], Any] = None
    ) -> bool:
    if key is None:
        key = lambda v: v

    return all(
        key(prev) <= key(curr)
        for prev, curr in sliding_window(2, seq)
    )


def matchingfrequencies(*seqs: Iterable[T], key=None) -> Iterable[Tuple[T, int]]:
    for k, g in groupby(merge(
            *[unique(seq, key=key) for seq in seqs],
            key=key
        )):
        yield (k, count(g))

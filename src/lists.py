"""Linked lists."""

from __future__ import annotations
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class L(Generic[T]):
    """
    A single link in a linked list.

    The `head` attribute gives you the value at the head of
    this list while `tail` gives you the rest of the list,
    or None if the rest is the empty list.

    >>> L(1, L(2, L(3, None)))
    L(1, L(2, L(3, None)))
    """

    head: T
    tail: List[T]

    def __repr__(self) -> str:
        """Representation of this object."""
        return f"L({self.head}, {self.tail})"


List = Optional[L[T]]  # A list is an L() constructor or None


# length

def length(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    return 0 if x is None else 1 + length(x.tail)

def length_tr(x: List[T], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> length_tr(None)
    0
    >>> length_tr(L(1, None))
    1
    >>> length_tr(L(1, L(2, L(3, None))))
    3
    """
    return acc if x is None else length_tr(x.tail, acc + 1)

def length_loop(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length_loop(None)
    0
    >>> length_loop(L(1, None))
    1
    >>> length_loop(L(1, L(2, L(3, None))))
    3
    """
    acc = 0
    while x:
        acc += 1
        x = x.tail
    return acc

# add

def add(x: List[int]) -> int:
    """
    Compute the sum of elements in x.

    >>> add(None)
    0
    >>> add(L(1, None))
    1
    >>> add(L(1, L(2, L(3, None))))
    6
    """
    return 0 if x is None else x.head + add(x.tail)

def add_tr(x: List[int], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> add_tr(None)
    0
    >>> add_tr(L(1, None))
    1
    >>> add_tr(L(1, L(2, L(3, None))))
    6
    """
    return acc if x is None else add_tr(x.tail, acc + x.head)

def add_loop(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add_loop(None)
    0
    >>> add_loop(L(1, None))
    1
    >>> add_loop(L(1, L(2, L(3, None))))
    6
    """
    acc = 0
    while x:
        acc += x.head
        x = x.tail
    return acc

# contains

def contains(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains(L(1, L(2, L(3, None))), 4)
    False
    >>> contains(L(1, L(2, L(3, None))), 2)
    True
    """
    if x.head == e:
        return True
    elif x.tail == None:
        return False
    return contains(x.tail, e)

def contains_tr(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_tr(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_tr(L(1, L(2, L(3, None))), 2)
    True
    """
    return contains(x, e) #same for recursive and tail-recursive

def contains_loop(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_loop(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_loop(L(1, L(2, L(3, None))), 2)
    True
    """
    x_bool = False
    while x:
        if x.head == e:
            x_bool = True
        x = x.tail
    return x_bool

# drop

def drop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop(x, 3)
    L(4, None)
    """
    if k == 0:
        return x
    else:
        return drop(x.tail, k-1)

def drop_tr(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_tr(x, 3)
    L(4, None)
    """
    return drop(x, k) # same for recursive and tail-recursive

def drop_loop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_loop(x, 3)
    L(4, None)
    """
    if k == 0:
        return x
    while k>0:
        x = x.tail
        k-=1
    return x

# keep

def keep(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep(x, 0) # returns None but doesn't print
    >>> keep(x, 1)
    L(1, None)
    >>> keep(x, 3)
    L(1, L(2, L(3, None)))
    """
    if k == 0:
        return None
    return L(x.head, keep(x.tail, k-1))
    
def keep_tr(x: List[T], k: int, acc: List[T] = None) -> List[T]:
    """
    Keep only the first k elements.

    # >>> x = L(1, L(2, L(3, L(4, None))))
    # >>> keep_tr(x, 0) # returns None but doesn't print
    # >>> keep_tr(x, 1)
    # L(1, None)
    # >>> keep_tr(x, 3)
    # L(1, L(2, L(3, None)))
    """
    if k == 0:
        return rev_tr(acc)
    else:
        return keep_tr(x.tail, k-1, L(x.head, acc))

def keep_loop(x: List[T], k: int, acc: List[T] = None) -> List[T]:
    """
    Keep only the first k elements.

    # >>> x = L(1, L(2, L(3, L(4, None))))
    # >>> keep_loop(x, 0) # returns None but doesn't print
    # >>> keep_loop(x, 1)
    # L(1, None)
    # >>> keep_loop(x, 3)
    # L(1, L(2, L(3, None)))
    """
    while k>0:
        acc = append_loop(acc, x.head)
        x = x.tail
        k-=1
    return acc

# concat

def concat(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    if x == None:
        return y
    else:
        return L(x.head, concat(x.tail, y))

def concat_tr(x: List[T], y: List[T], acc: List[T] = None) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_tr(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    if x == None:
        return rev_tr(acc, y)
    else:
        acc = L(x.head, acc)
        return concat_tr(x.tail, y, acc)

def concat_loop(x: List[T], y: List[T], acc: List[T] = None) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_loop(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    return rev_tr(rev_loop(x), y)

# append

def append(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat(x, L(e, None))
    
def append_tr(x: List[T], e: T, acc: List[T] = None) -> List[T]:
    """
    Append e to x.

    >>> append_tr(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat_tr(x, L(e, None))

def append_loop(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_loop(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat_loop(x, L(e, None))

# rev

def rev(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    if x == None:
        return None
    else:
        return append(rev(x.tail), x.head)

def rev_tr(x: List[T], acc: List[T] = None) -> List[T]:
    """
    Reverse a list.

    >>> rev_tr(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    if x == None:
        return acc
    else:
        acc = L(x.head, acc)
        return rev_tr(x.tail, acc)

def rev_loop(x: List[T], acc: List[T] = None) -> List[T]:
    """
    Reverse a list.

    >>> rev_loop(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    while x:
        acc = L(x.head, acc)
        x = x.tail
    return acc

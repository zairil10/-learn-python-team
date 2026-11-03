"""Lists.

# @see: https://www.learnpython.org/en/Lists
# @see: https://docs.python.org/3/tutorial/introduction.html
# @ee: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

Python knows a number of compound data types, used to group together
other values. The most versatile is the list, which can be written as a
list of comma-separated values (items) between square brackets. Lists
might contain items of different types, but usually the items all have
the same type.
"""

import pytest


def test_list_type():
    """List type."""

    # Lists are very similar to arrays. They can contain any type of variable, and they can contain
    # as many variables as you wish. Lists can also be iterated over in a very simple manner.
    # Here is an example of how to build a list.
    squares = [1, 4, 9, 16, 25]

    assert isinstance(squares, list)

    # Like strings (and all other built-in sequence type), lists can be
    # indexed and sliced:
    assert squares[0] == 1  # indexing returns the item
    assert squares[-1] == 25
    assert squares[-3:] == [9, 16, 25]  # slicing returns a new list

    # All slice operations return a new list containing the requested elements.
    # This means that the following slice returns a new (shallow) copy of
    # the list:
    assert squares[:] == [1, 4, 9, 16, 25]

    # Lists also support operations like concatenation:
    assert squares + [36, 49, 64, 81, 100] == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    # Unlike strings, which are immutable, lists are a mutable type, i.e. it
    # is possible to change their content:
    cubes = [1, 8, 27, 65, 125]  # something's wrong here, the cube of 4 is 64!
    cubes[3] = 64  # replace the wrong value
    assert cubes == [1, 8, 27, 64, 125]

    # You can also add new items at the end of the list, by using
    # the append() method
    cubes.append(216)  # add the cube of 6
    cubes.append(7 ** 3)  # and the cube of 7
    assert cubes == [1, 8, 27, 64, 125, 216, 343]

    # Assignment to slices is also possible, and this can even change the size
    # of the list or clear it entirely:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    letters[2:5] = ['C', 'D', 'E']  # replace some values
    assert letters == ['a', 'b', 'C', 'D', 'E', 'f', 'g']
    letters[2:5] = []  # now remove them
    assert letters == ['a', 'b', 'f', 'g']
    # clear the list by replacing all the elements with an empty list
    letters[:] = []
    assert letters == []

    # The built-in function len() also applies to lists
    letters = ['a', 'b', 'c', 'd']
    assert len(letters) == 4

    # It is possible to nest lists (create lists containing other lists),
    # for example:
    list_of_chars = ['a', 'b', 'c']
    list_of_numbers = [1, 2, 3]
    mixed_list = [list_of_chars, list_of_numbers]
    assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]
    assert mixed_list[0] == ['a', 'b', 'c']
    assert mixed_list[0][1] == 'b'


def test_list_methods():
    """Test list methods."""

    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.append(x)
    # Add an item to the end of the list.
    # Equivalent to a[len(a):] = [x].
    fruits.append('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

    # list.remove(x)
    # Remove the first item from the list whose value is equal to x.
    # It raises a ValueError if there is no such item.
    fruits.remove('grape')
    assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    with pytest.raises(Exception):
        fruits.remove('not existing element')

    # list.insert(i, x)
    # Insert an item at a given position. The first argument is the index of the element
    # before which to insert, so a.insert(0, x) inserts at the front of the list,
    # and a.insert(len(a), x) is equivalent to a.append(x).
    fruits.insert(0, 'grape')
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.index(x[, start[, end]])
    # Return zero-based index in the list of the first item whose value is equal to x.
    # Raises a ValueError if there is no such item.
    # The optional arguments start and end are interpreted as in the slice notation and are used
    # to limit the search to a particular subsequence of the list. The returned index is computed
    # relative to the beginning of the full sequence rather than the start argument.
    assert fruits.index('grape') == 0
    assert fruits.index('orange') == 1
    assert fruits.index('banana') == 4
    assert fruits.index('banana', 5) == 7  # Find next banana starting a position 5

    with pytest.raises(Exception):
        fruits.index('not existing element')

    # list.count(x)
    # Return the number of times x appears in the list.
    assert fruits.count('tangerine') == 0
    assert fruits.count('banana') == 2

    # list.copy()
    # Return a shallow copy of the list. Equivalent to a[:].
    fruits_copy = fruits.copy()
    assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    # list.reverse()
    # Reverse the elements of the list in place.
    fruits_copy.reverse()
    assert fruits_copy == [
        'banana',
        'apple',
        'kiwi',
        'banana',
        'pear',
        'apple',
        'orange',
        'grape',
    ]

    # list.sort(key=None, reverse=False)
    # Sort the items of the list in place (the arguments can be used for sort customization,
    # see sorted() for their explanation).
    fruits_copy.sort()
    assert fruits_copy == [
        'apple',
        'apple',
        'banana',
        'banana',
        'grape',
        'kiwi',
        'orange',
        'pear',
    ]

    # list.pop([i])
    # Remove the item at the given position in the list, and return it. If no index is specified,
    # a.pop() removes and returns the last item in the list. (The square brackets around the i in
    # the method signature denote that the parameter is optional, not that you should type square
    # brackets at that position.)
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    assert fruits.pop() == 'banana'
    assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

    # list.clear()
    # Remove all items from the list. Equivalent to del a[:].
    fruits.clear()
    assert fruits == []


def test_del_statement():
    """The del statement

    There is a way to remove an item from a list given its index instead of its value: the del
    statement. This differs from the pop() method which returns a value. The del statement can also
    be used to remove slices from a list or clear the entire list (which we did earlier by
    assignment of an empty list to the slice).
    """

    numbers = [-1, 1, 66.25, 333, 333, 1234.5]

    del numbers[0]
    assert numbers == [1, 66.25, 333, 333, 1234.5]

    del numbers[2:4]
    assert numbers == [1, 66.25, 1234.5]

    del numbers[:]
    assert numbers == []

    # del can also be used to delete entire variables:
    del numbers
    with pytest.raises(Exception):
        # Referencing the name a hereafter is an error (at least until another
        # value is assigned to it).
        assert numbers == []  # noqa: F821


def test_list_comprehensions():
    """List Comprehensions.

    List comprehensions provide a concise way to create lists. Common applications are to make new
    lists where each element is the result of some operations applied to each member of another
    sequence or iterable, or to create a subsequence of those elements that satisfy a certain
    condition.

    A list comprehension consists of brackets containing an expression followed by a for clause,
    then zero or more for or if clauses. The result will be a new list resulting from evaluating
    the expression in the context of the for and if clauses which follow it.
    """

    # For example, assume we want to create a list of squares, like:
    squares = []
    for number in range(10):
        squares.append(number ** 2)

    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Note that this creates (or overwrites) a variable named "number" that still exists after
    # the loop completes. We can calculate the list of squares without any side effects using:
    squares = list(map(lambda x: x ** 2, range(10)))
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # or, equivalently (which is more concise and readable):
    squares = [x ** 2 for x in range(10)]
    assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # For example, this listcomp combines the elements of two lists if they are not equal.
    combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # and it’s equivalent to:
    combinations = []
    for first_number in [1, 2, 3]:
        for second_number in [3, 1, 4]:
            if first_number != second_number:
                combinations.append((first_number, second_number))

    assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    # Note how the order of the for and if statements is the same in both these snippets.

    # If the expression is a tuple (e.g. the (x, y) in the previous example),
    # it must be parenthesized.

    # Let's see some more examples:

    vector = [-4, -2, 0, 2, 4]

    # Create a new list with the values doubled.
    doubled_vector = [x * 2 for x in vector]
    assert doubled_vector == [-8, -4, 0, 4, 8]

    # Filter the list to exclude negative numbers.
    positive_vector = [x for x in vector if x >= 0]
    assert positive_vector == [0, 2, 4]

    # Apply a function to all the elements.
    abs_vector = [abs(x) for x in vector]
    assert abs_vector == [4, 2, 0, 2, 4]

    # Call a method on each element.
    fresh_fruit = ['  banana', '  loganberry ', 'passion fruit  ']
    clean_fresh_fruit = [weapon.strip() for weapon in fresh_fruit]
    assert clean_fresh_fruit == ['banana', 'loganberry', 'passion fruit']

    # Create a list of 2-tuples like (number, square).
    square_tuples = [(x, x ** 2) for x in range(6)]
    assert square_tuples == [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # Flatten a list using a listcomp with two 'for'.
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten_vector = [num for elem in vector for num in elem]
    assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_nested_list_comprehensions():
    """Nested List Comprehensions

    The initial expression in a list comprehension can be any arbitrary expression, including
    another list comprehension.
    """

    # Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    # The following list comprehension will transpose rows and columns:
    transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
    assert transposed_matrix == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # As we saw in the previous section, the nested listcomp is evaluated in the context of the
    # for that follows it, so this example is equivalent to:
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # which, in turn, is the same as:
    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    assert transposed == [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12],
    ]

    # In the real world, you should prefer built-in functions to complex flow statements.
    # The zip() function would do a great job for this use case:
    assert list(zip(*matrix)) == [
        (1, 5, 9),
        (2, 6, 10),
        (3, 7, 11),
        (4, 8, 12),
    ]

    def test_list_sorting():
    """Sorting lists with sorted() and list.sort()."""

    numbers = [5, 2, 9, 1, 7]

    # sorted() returns a new sorted list and leaves the original unchanged.
    assert sorted(numbers) == [1, 2, 5, 7, 9]
    assert numbers == [5, 2, 9, 1, 7]

    # The reverse argument sorts in descending order.
    assert sorted(numbers, reverse=True) == [9, 7, 5, 2, 1]

    # The key argument customizes the sort. Here we sort words by length.
    # The sort is stable, so equal-length words keep their original order.
    words = ['banana', 'kiwi', 'apple', 'fig']
    assert sorted(words, key=len) == ['fig', 'kiwi', 'apple', 'banana']

    # list.sort() sorts in place and returns None.
    assert numbers.sort() is None
    assert numbers == [1, 2, 5, 7, 9]


def test_list_filtering_and_slicing():
    """Filtering with comprehensions/filter() and slicing with steps."""

    numbers = list(range(1, 11))
    assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Filtering with a list comprehension...
    evens = [x for x in numbers if x % 2 == 0]
    assert evens == [2, 4, 6, 8, 10]

    # ...is equivalent to using the built-in filter() function.
    assert list(filter(lambda x: x % 2 == 0, numbers)) == evens

    # Slicing supports a step: list[start:stop:step].
    assert numbers[2:5] == [3, 4, 5]
    assert numbers[::2] == [1, 3, 5, 7, 9]  # every second item
    assert numbers[1::2] == [2, 4, 6, 8, 10]  # every second item, starting at index 1
    assert numbers[-3:] == [8, 9, 10]  # last three items

    # A negative step reverses the list (returning a new list).
    assert numbers[::-1] == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def test_list_comprehension_extras():
    """More list comprehension patterns and built-in helpers."""

    # A conditional expression (if/else) goes BEFORE the for clause,
    # unlike a filtering if, which goes after it.
    labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
    assert labels == ['even', 'odd', 'even', 'odd', 'even']

    # Combine enumerate() with a comprehension to work with indexes.
    names = ['Ann', 'Ben', 'Cy']
    numbered = [f'{i}: {name}' for i, name in enumerate(names, start=1)]
    assert numbered == ['1: Ann', '2: Ben', '3: Cy']

    # Combine two lists element by element with zip().
    prices = [2, 3, 5]
    quantities = [10, 20, 30]
    totals = [p * q for p, q in zip(prices, quantities)]
    assert totals == [20, 60, 150]

    # Built-in functions that work on lists.
    scores = [88, 92, 75, 64]
    assert sum(scores) == 319
    assert max(scores) == 92
    assert min(scores) == 64
    assert sum(scores) / len(scores) == 79.75

    def test_list_aliasing_and_shallow_copy():
    """Aliasing vs. copying: assignment shares a list, copies share nested items."""

    # Assignment does not copy a list; both names refer to the same object.
    original = [1, 2, 3]
    alias = original
    alias.append(4)
    assert original == [1, 2, 3, 4]
    assert alias is original

    # A slice (or list.copy()) creates a new, independent outer list.
    clone = original[:]
    clone.append(5)
    assert original == [1, 2, 3, 4]
    assert clone == [1, 2, 3, 4, 5]
    assert clone is not original

    # ...but the copy is shallow: nested lists are still shared.
    nested = [[1, 2], [3, 4]]
    shallow = nested.copy()
    shallow[0].append(99)
    assert nested == [[1, 2, 99], [3, 4]]

    # Build independent nested lists with a comprehension (or copy.deepcopy()).
    independent = [row[:] for row in nested]
    independent[0].append(100)
    assert nested == [[1, 2, 99], [3, 4]]
    assert independent == [[1, 2, 99, 100], [3, 4]]

    # Beware: multiplying a list of lists repeats references to the same inner list.
    shared_rows = [[0]] * 3
    shared_rows[0].append(1)
    assert shared_rows == [[0, 1], [0, 1], [0, 1]]

    separate_rows = [[0] for _ in range(3)]
    separate_rows[0].append(1)
    assert separate_rows == [[0, 1], [0], [0]]

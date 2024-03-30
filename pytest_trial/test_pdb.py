# test_pdb.py
import pdb
import pytest

pytestmark = pytest.mark.skip


def integers_counter(data):
    integers_found = 0
    for item in data:
        if not isinstance(item, bool) and isinstance(item, int):
            integers_found += 1
    return integers_found


def test_counter():
    # Произвольные данные для анализа.
    data = [False, 1.0, "some_string", 3, True, 1, [], False]
    # Вызываем функцию:
    integers = integers_counter(data)
    # Целых чисел должно быть 2.
    assert integers == 2

# test_pdb.py
def transform_list(x):
    x.append(1)
    x.extend([2, 3])
    return x


def test_list():
    a = []
    a = transform_list(a)
    a = [4] + a
    assert a == [1, 2, 3, 4] 
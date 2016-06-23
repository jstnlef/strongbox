import random
import string
import threading

import pytest

from lru_cache import LRUCache


def test_setitem():
    cache = LRUCache(2)
    cache['test'] = 2
    assert cache['test'] == 2


def test_setitem_wrap():
    cache = LRUCache(1)
    cache['test'] = 1
    assert cache['test'] == 1
    cache['test2'] = 4
    with pytest.raises(KeyError):
        assert cache['test'] == 1


def test_getitem():
    cache = LRUCache(1)
    cache['test'] = 2
    assert cache['test'] == 2
    with pytest.raises(KeyError):
        cache['not_here']


def test_getitem_reorder():
    cache = LRUCache(3)
    for i in range(3):
        cache[i] = i
    assert list(cache._cache) == [0, 1, 2]
    assert cache[0] == 0
    assert list(cache._cache) == [1, 2, 0]
    assert cache[2] == 2
    assert list(cache._cache) == [1, 0, 2]


def test_peek():
    cache = LRUCache(3)
    for i in range(3):
        cache[i] = i
    assert list(cache._cache) == [0, 1, 2]
    assert cache.peek(0) == 0
    assert list(cache._cache) == [0, 1, 2]


def test_get_with_default():
    cache = LRUCache(1)
    cache['test'] = 2
    assert cache['test'] == 2
    assert cache.get('not_around') is None
    assert cache.get('also_not_around', 4) == 4


def test_cache_maintains_max_size():
    cache = LRUCache(5)
    assert len(cache) == 0
    for i in range(20):
        cache['test{}'.format(i)] = i

    assert len(cache) == 5

    for i in range(15):
        assert 'test{}'.format(i) not in cache
    for i in range(15, 20):
        assert 'test{}'.format(i) in cache


def set_and_pop(cache_instance):
    for i in xrange(100):
        key = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        cache_instance[key] = 'abc123'
        # It is possible but unlikely that the key we just set has already been evicted. In that
        # unlikely case, we may raise a KeyError from inside this thread, but the exception won't
        # bubble up to the parent thread, so the test will still pass.
        assert cache_instance[key] == 'abc123'


def test_threaded_cache():
    cache = LRUCache(128)
    num_threads = 8
    threads = []
    for _ in xrange(num_threads):
        t = threading.Thread(target=set_and_pop, args=(cache,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert len(cache) == 128

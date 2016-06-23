from structbox import structbox


class LRUCache:
    def __init__(self, max_capacity):
        """
        :param int max_capacity: Max number of items saved in the cache
        """
        # self._cache = structbox.LruCache_new(max_capacity)
        print(len(self))

    def __contains__(self, key):
        """
        :param key: Key to check for cache containment
        :return bool: Existance of key in cache
        """
        n = structbox.LruCache_contains_key(key)
        return bool(n)

    def __setitem__(self, key, value):
        """
        Sets a key/value pair into the cache while maintaining the max_capacity invariant.
        :param key: Key to be stored in the cache
        :param value: Value to be stored at the key in the cache
        """
        raise NotImplementedError

    def __getitem__(self, key):
        """
        Retrieve an item from the cache. Moves the value to the front of the cache order.
        :param key: Key to fetch the value stored in the cache
        :return: Item stored at the given key
        """
        raise NotImplementedError

    def get(self, key, default=None):
        """
        Retrieve an item from the cache. Moves the value to the front of the cache order. If the item
        doesn't exist, return the default argument.
        :param key: Key to fetch the value stored in the cache
        :return: Item stored at the given key
        """
        try:
            return self[key]
        except KeyError:
            return default

    def peek(self, key):
        """
        Retrieve an item from the cache without affecting the cache order.
        :param key: Key to fetch the value stored in the cache
        :return: Item stored at the given key
        """
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.__dict__)

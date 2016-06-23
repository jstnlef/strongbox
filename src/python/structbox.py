from sys import platform

from cffi import FFI


def initialize_dynamic_lib():
    if platform.startswith('darwin'):
        prefix = 'lib'
        ext = 'dylib'
    elif platform.startswith('win32'):
        prefix = ''
        ext = 'dll'
    elif platform.startswith('linux'):
        prefix = 'lib'
        ext = 'so'
    else:
        raise RuntimeError("OS Platform not supported.")

    ffi = FFI()
    ffi.cdef('''
        size_t lru_cache(size_t);
        bool LruCache_contains_key(int);
        void* LruCache_new(size_t);
        size_t LruCache_len(void*);
    ''')

    return ffi.dlopen("../../target/release/{}structbox.{}".format(prefix, ext))


structbox = initialize_dynamic_lib()

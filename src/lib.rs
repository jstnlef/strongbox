#[macro_use] extern crate cpython;
extern crate libc;
extern crate lru_cache;
extern crate linked_hash_map;

use cpython::PyObject;
use libc::c_void;
use lru_cache::LruCache;

// #[no_mangle]
// pub extern fn LruCache_new(max_capacity: usize) -> *mut c_void {
//     let cache: Box<LruCache<*mut c_void, *mut c_void>> = Box::new(LruCache::new(max_capacity));
//     cache as *mut c_void;
// }

#[no_mangle]
pub extern fn LruCache_contains_key(target: *mut LruCache<*mut PyObject, *mut PyObject>, key: i32) -> bool {
    true
}

#[no_mangle]
pub extern fn LruCache_insert(target: *mut LruCache<*mut PyObject, *mut PyObject>, key: i32) -> bool {
    true
}

#[no_mangle]
pub extern fn LruCache_get_mut(target: *mut LruCache<*mut PyObject, *mut PyObject>, key: i32) -> bool {
    true
}

#[no_mangle]
pub extern fn LruCache_len(target: *mut c_void) -> usize {
    let target: &mut LruCache<*mut c_void, *mut c_void> = unsafe {
        &mut *(target as *mut LruCache<*mut c_void, *mut c_void>)
    };
    target.len()
}

extern crate lru_cache;

use lru_cache::LruCache;

fn main() {
    let mut cache: LruCache<i32, i32> = LruCache::new(1);
    cache.insert(1, 2);
    cache.insert(2, 3);
    assert_eq!(cache.get_mut(&1), None);
    assert_eq!(cache.get_mut(&2), Some(&mut 3));
}

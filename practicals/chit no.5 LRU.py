from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def refer(self, page):
        if page in self.cache:
            # Move the page to the end to mark it as most recently used
            self.cache.move_to_end(page)
        else:
            # Check if the cache is full
            if len(self.cache) >= self.capacity:
                # Remove the least recently used page (the first item in the ordered dictionary)
                self.cache.popitem(last=False)
            # Add the new page to the cache
            self.cache[page] = None

def lru_page_replacement(pages, capacity):
    lru_cache = LRUCache(capacity)
    page_faults = 0

    for page in pages:
        if page not in lru_cache.cache:
            print(f"Page {page} is loaded into the memory.")
            lru_cache.refer(page)
            page_faults += 1
        else:
            print(f"Page {page} is already in the memory.")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example usage
    page_references = [2, 3, 4, 2, 1, 3, 7, 5, 4, 3]
    memory_capacity = 3

    lru_page_replacement(page_references, memory_capacity)

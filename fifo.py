from collections import deque

def fifo_page_replacement(pages, capacity):
    page_queue = deque(maxlen=capacity)
    page_faults = 0

    for page in pages:
        if page not in page_queue:
            print(f"Page {page} is loaded into the memory.")
            page_queue.append(page)
            page_faults += 1
        else:
            print(f"Page {page} is already in the memory.")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example usage
    page_references = list(map(int,input("enter the refrences : ").split()))
    memory_capacity = int(input("enter memory capcity"))

    fifo_page_replacement(page_references, memory_capacity)

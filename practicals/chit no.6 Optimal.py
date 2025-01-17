def optimal_page_replacement(pages, capacity):
    page_faults = 0
    page_frames = [-1] * capacity

    for i in range(len(pages)):
        if pages[i] not in page_frames:
            if -1 in page_frames:
                # If there is an empty frame, place the page in it
                index = page_frames.index(-1)
                page_frames[index] = pages[i]
            else:
                # Find the page that will not be used for the longest period in the future
                future_occurrences = {page: float('inf') for page in page_frames}
                for j in range(i + 1, len(pages)):
                    if pages[j] in future_occurrences:
                        future_occurrences[pages[j]] = j

                page_to_replace = max(future_occurrences, key=future_occurrences.get)
                index = page_frames.index(page_to_replace)
                page_frames[index] = pages[i]

            print(f"Page {pages[i]} is loaded into the memory.")
            page_faults += 1
        else:
            print(f"Page {pages[i]} is already in the memory.")

    print(f"\nTotal Page Faults: {page_faults}")

if __name__ == "__main__":
    # Example usage
    page_references = [2, 3, 4, 2, 1, 3, 7, 5, 4, 3]
    memory_capacity = 3

    optimal_page_replacement(page_references, memory_capacity)

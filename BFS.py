from collections import deque

# Example of Breadth-First Search

def search(name, graph=None):
    if graph is None:
        return False

    search_queue = deque()
    search_queue += graph.get(name, [])
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller")
                return True
            else:

                search_queue += graph.get(person, [])
                searched.append(person)
    return False

def person_is_seller(name):
    # stupid example
    return name[1:5] == 'avid'

ex_graph = {
    "me": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Bob"],
    "David": ["Bob", "Emily"],
    "Emily": ["David"],
}

search("me", ex_graph)

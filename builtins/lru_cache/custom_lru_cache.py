from functools import wraps

from linked_list import Node, DoublyLinkedList


def lru_cache(max_size: int = 128):
    cache = {}
    linked_list = DoublyLinkedList()

    def decorator_lru_cache(func):
        @wraps(func)
        def wrapper_lru_cache(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                # move node to tail
                used_node = cache[key]
                linked_list.remove(used_node)
                linked_list.append(used_node)

                return used_node.value

            # if size over maxsize remove head node
            if len(linked_list) > max_size:
                old_node = linked_list.popleft()
                del cache[old_node.key]

            result = func(*args, **kwargs)

            # add node to cache and linked_list
            node = Node(key=key, value=result)
            cache[key] = node
            linked_list.append(node)
            return result

        return wrapper_lru_cache

    return decorator_lru_cache

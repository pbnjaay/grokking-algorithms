from collections import deque


def binary_search(list, item):
    length = len(list) - 1
    mid = round(length / 2)

    while mid <= length and mid >= 0:
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            mid = mid + 1
        else:
            mid = mid - 1
    return None


"""
Recursion
"""


def binary_search_r(list, item):
    mid = round(len(list) / 2)
    if (list[mid] == item):
        return mid

    if (len(list) == 0):
        return None

    return binary_search_r(list[mid:], item) \
        if list[mid] > item \
        else binary_search_r(list[:mid], item)


def fact(n):
    if (n == 1):
        return n
    return n * fact(n-1)


def sum(arr):
    if (len(arr) == 0):
        return 0
    return arr[0] + sum(arr[1:])


def count(arr):
    if (len(arr) == 1):
        return 1
    return 1 + count(arr[1:])


def max_r(arr):
    if (len(arr) == 2):
        return arr[0] if arr[0] > arr[1] else arr[1]

    return arr[0] if arr[0] > max_r(arr[1:]) else max_r(arr[1:])

# pivot as the fisrt element
# time complexity average O(nlogn)
# space complexity O(n)


def quick_sort(arr):
    if (len(arr) < 2):
        return arr

    pivot = arr[0]

    greater = [i for i in arr[1:] if i > pivot]
    lesser = [i for i in arr[1:] if i <= pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


print(binary_search([i for i in range(100)], 980))


print(quick_sort([3, 2, 9, 2, 1, 0, -1, 33, 8]))


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'{person} is a seller !')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False


print(search('you'))


def earliest_ancestor(ancestors, starting_node):
    # convert input to edges
    parents = {}
    for parent, child in ancestors:
        if child in parents:
            parents[child].add(parent)
        else:
            parents[child] = {parent}
    print(f'parents: {parents}')

    # find the longest path
    result = []
    paths = [[starting_node]]
    visited = []
    while paths:
        path = paths.pop(0)
        child = path[-1]
        if child in visited:
            continue

        if child in parents:
            for p in parents[child]:
                path_new = path.copy()
                path_new.append(p)
                paths.append(path_new)
        elif len(path) > len(result) \
        or (len(path)==len(result) and path[-1] < result[-1]):
            result = path

    print(f'longest path: {result}\n')
    return result[-1] if len(result)>1 else -1


if __name__ == '__main__':
    '''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
    '''
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    earliest_ancestor(ancestors, 1)
    earliest_ancestor(ancestors, 6)
    earliest_ancestor(ancestors, 2)
    earliest_ancestor(ancestors, 9)
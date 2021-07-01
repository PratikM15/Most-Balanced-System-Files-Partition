def mostBalancedPartition(parent, files_size):
    def helper(node, adj, files_size):
        queue = [node]
        weight = 0
        while queue:
            index = queue.pop()
            weight += files_size[index]
            if index in adj:
                queue.extend(adj[index])
        return weight

    adj = {}
    edges = []
    for index, p in enumerate(parent):
        edges.append((p, index))
        if p in adj:
            adj[p].append(index)
        else:
            adj[p] = [index]
    
    total_weight = sum(files_size)
    min_diff = sum(files_size)
    for e in edges:
        p,c = e
        adj[p].remove(c)
        w1 = helper(c, adj, files_size)
        min_diff = min(min_diff, abs(total_weight - 2*w1))
        adj[p].append(c)

    return min_diff

if __name__ == '__main__':
    parent_count = int(input("Enter No of Nodes: ").strip())
    parent = []
    print("Enter Values: ")
    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)
    files_size_count = int(input("Enter File Size Count: ").strip())
    files_size = []
    print("Enter Values: ")
    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)
    result = mostBalancedPartition(parent, files_size)
    print("Most Balanced System Files Partition Difference: ", result)

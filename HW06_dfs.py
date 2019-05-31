import json
tree = json.loads('[{"name": "B", "parents": ["A", "C"]}, '
                  '{"name": "C", "parents": ["A"]},'
                  '{"name": "A", "parents": []},'
                  '{"name": "D", "parents": ["C", "F"]},'
                  '{"name": "E", "parents": ["D"]},'
                  '{"name": "F", "parents": []}]')

#I

d = dict()

for ch in tree:

    if len(ch["parents"]) > 0:
        for p in ch["parents"]:
            if p not in d:
                d[p] = [ch["name"]]
            else:
                d[p].append(ch["name"])

print("\nParents: childs \n", d)

nodes_all = [n["name"] for n in tree]
nodes_all.sort()

#II


def dfs_all(d, start):
    viz = dict.fromkeys(nodes_all, False)

    def dfs(node):
        viz[node] = True
        if node in d:
            for ch in d[node]:
                if not viz[ch]:
                    dfs(ch)
    dfs(start)

    return sum(viz.values())


#III
d_values = dict()
for node in nodes_all:
    d_values[node] = dfs_all(d, node)

print(d_values)

def expand(node, _map):
	return [next for next in _map[node] if _map[node][next] is not None]

def depth_first_search(_map, start, end):
	visited = [start]
	def helper(_map, start, end, visited):
		if start == end:
			return [start]
		landmarks = expand(start, _map)
		
		while len(landmarks):
			if len(landmarks) == 0:
				return []
			landmark = landmarks.pop()
			if landmark not in visited:
				visited.append(landmark)
				next_path = helper(_map, landmark, end, visited)
				if next_path!= []:
					return [start] + next_path
		return []
	help_dfs = helper(_map, start, end, visited)
	return help_dfs, visited


def breadth_first_search(_map, start, end):
	visited = {"start":start}
	queue = []
	while start!=end:
		if start not in visited:
			visited[start] = expand(start, _map)
			queue += visited[start]
		if len(queue) == 0: break
		start = queue.pop(0) 

	def get_full_path(end, visited):
		if end==visited["start"]: return [end]
		for key, val in visited.items():
			if end in val: return get_full_path(key, visited) + [end]
		return []

	help_bfs = get_full_path(end, visited)
	v = []
	for key, values in visited.items():
		if type(values) == str: v.append(values)
		else: v = v + values
	v = list(set(v))
	return help_bfs, v
			


		
			

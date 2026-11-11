"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    if ctx.start == ctx.goal:
        return [ctx.start]

    frontier = deque([ctx.start])
    parent = {ctx.start: None}
    discovered = {ctx.start}

    while frontier:
        current = frontier.popleft()
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        neighbours = ctx.expand(current, len(frontier) + 1)
        for n in neighbours:
            if n not in discovered:
                discovered.add(n)
                parent[n] = current
                frontier.append(n)

    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    if ctx.start == ctx.goal:
        return [ctx.start]

    frontier = [ctx.start]
    parent = {ctx.start: None}
    discovered = {ctx.start}

    while frontier:
        current = frontier.pop()
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        neighbours = ctx.expand(current, len(frontier) + 1)
        for n in reversed(neighbours):
            if n not in discovered:
                discovered.add(n)
                parent[n] = current
                frontier.append(n)

    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    if ctx.start == ctx.goal:
        return [ctx.start]

    depth = 0
    while True:
        stack = [(ctx.start, 0, [ctx.start])]

        while stack:
            current, d, path = stack.pop()

            if current == ctx.goal:
                return path

            if d < depth:
                neighbours = ctx.expand(current, len(stack) + 1)
                for n in reversed(neighbours):
                    if n not in path:
                        stack.append((n, d + 1, path + [n]))

        depth += 1


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    if ctx.start == ctx.goal:
        return [ctx.start]

    start_h = ctx.heuristic(ctx.start)
    frontier = [(start_h, 0, ctx.start)]
    best_g = {ctx.start: 0}
    parent = {ctx.start: None}

    while frontier:
        f, g, current = heappop(frontier)

        if g > best_g.get(current, float('inf')):
            continue

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        neighbours = ctx.expand(current, len(frontier) + 1)
        for n in neighbours:
            new_g = g + 1
            if new_g < best_g.get(n, float('inf')):
                best_g[n] = new_g
                parent[n] = current
                h = ctx.heuristic(n)
                heappush(frontier, (new_g + h, new_g, n))

    return []

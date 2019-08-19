#!/usr/bin/python3

import sys
import plotly.offline as py
import plotly.graph_objs as go


def add_slash(path):
    """Adds slash to the path if it's not there"""
    if path.endswith('/'):
        return path
    return path + '/'


def split_path(path, all_paths):
    """Splits path into parent and current folder"""
    idx = path.rfind('/', 0, -1)
    if idx == -1:
        return '', path
    parent, label = (path[0:idx + 1], path[idx+1:-1])
    if not parent in all_paths:
        return '', path
    return parent, label


def main():
    """Main script function"""
    sizes, paths = zip(*[line.rstrip().split() for line in sys.stdin])
    sizes, paths = list(map(int, sizes)), list(map(add_slash, paths))
    paths_set = set(paths)
    parents, labels = zip(*[split_path(path, paths_set) for path in paths])

    trace = go.Sunburst(
            ids = paths,
            labels = labels,
            parents = parents,
            values = sizes,
            branchvalues = 'total')
    fig = go.Figure([trace])
    py.plot(fig, filename = 'temp_pie.html')


main()

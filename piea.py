#!/usr/bin/python3

import argparse
import sys
import plotly.graph_objs as go
import plotly.offline as py


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


def plot(open_browser, filename):
    """Plots sunburst chart from data given in stdin"""
    sizes, paths = zip(*[line.rstrip().split() for line in sys.stdin])
    sizes, paths = list(map(int, sizes)), list(map(add_slash, paths))
    paths_set = set(paths)
    parents, labels = zip(*map(lambda p: split_path(p, paths_set), paths))

    trace = go.Sunburst(
            ids = paths,
            labels = labels,
            parents = parents,
            values = sizes,
            branchvalues = 'total')
    fig = go.Figure([trace])
    py.plot(fig,
            auto_open = open_browser,
            filename = filename)


def main():
    """Main script function"""
    parser = argparse.ArgumentParser(
            description = 'Plot sunburst chart for given tree')

    parser.add_argument('--hide',
            action = 'store_true',
            help = "don't open browser (default: open browser)")
    parser.add_argument('--file',
            default = 'temp_pie.html',
            help = "name of output html file")

    args = parser.parse_args()
    plot(not args.hide, args.file)

main()

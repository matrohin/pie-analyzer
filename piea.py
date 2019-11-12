#!/usr/bin/python3
"""Plot sunburst chart for given tree."""

import argparse
import sys
import plotly.graph_objs as go


def add_slash(path):
    """Add slash to the path if it's not there."""
    if path.endswith('/'):
        return path
    return path + '/'


def split_path(path, all_paths):
    """Split path into parent and current folder."""
    idx = path.rfind('/', 0, -1)
    if idx == -1:
        return '', path
    parent, label = path[0:idx + 1], path[idx+1:-1]
    if parent not in all_paths:
        return '', path
    return parent, label


def find_whitespace(string):
    """Find index of first whitespace in s."""
    for idx, char in enumerate(string):
        if char.isspace():
            return idx
    return -1


def split_line(line):
    """Split line into size and path."""
    line = line.strip()
    idx = find_whitespace(line)
    if idx == -1:
        return 0, line
    return int(line[0:idx]), add_slash(line[idx + 1:len(line)].strip())


def plot(filename):
    """Plot sunburst chart from data given in stdin."""
    sizes, paths = zip(*map(split_line, sys.stdin))
    paths_set = set(paths)
    parents, labels = zip(*map(lambda p: split_path(p, paths_set), paths))

    trace = go.Sunburst(
        ids=paths,
        labels=labels,
        parents=parents,
        values=sizes,
        branchvalues='total')
    fig = go.Figure([trace])

    if filename.endswith('html'):
        fig.write_html(filename)
    else:
        fig.write_image(filename)


def main():
    """Main script function."""
    parser = argparse.ArgumentParser(
        description='Plot sunburst chart for given tree')

    parser.add_argument(
        '--file',
        default='temp_pie.html',
        help='name of output file, for image support'
             'see https://plot.ly/python/static-image-export/')

    args = parser.parse_args()
    plot(args.file)


main()

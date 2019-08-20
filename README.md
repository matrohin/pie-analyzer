# Pie Analyzer (piea)
Tree (e.g. directory tree) sunburst (a.k.a. multilevel-pie) chart plotter

## Typical usage

It's intended to be used with du
([unix](https://en.wikipedia.org/wiki/Du_%28Unix%29),
[windows](https://docs.microsoft.com/en-us/sysinternals/downloads/du))
utility like this:

```
du folder/to/analyze | python3 piea.py
```

`temp_pie.html` will be created with interactive sunburst chart of your folder.
Also your default browser will open this file.

### du hints

If there are too many directories, browser can be slow in rendering the chart.

It can be solved by passing some thresholds to du.

This command will show only folders that are bigger than 10KB:
```
du --threshold=10K folder/to/analyze | python3 piea.py
```

This command will show only folders that are 3 levels deep:
```
du --max-depth=3 folder/to/analyze | python3 piea.py
```

## But can you do this?

Yes, you can plot any tree-like structure. Just pass input in following form to `piea.py`.
```
<size1> root/parent
<size2> root/parent/child
...
<sizeN> root
```

## Command-line arguments

```
usage: piea.py [-h] [--hide] [--file FILE]

Plot sunburst chart for given tree

optional arguments:
  -h, --help   show this help message and exit
  --hide       don't open browser (default: open browser)
  --file FILE  name of output html file
```

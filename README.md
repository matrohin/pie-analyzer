# Pie Analyzer (piea)
Tree (e.g. directory tree) sunburst (a.k.a. multilevel-pie) chart plotter

[![Build Status](https://travis-ci.org/matrohin/pie-analyzer.svg?branch=master)](https://travis-ci.org/matrohin/pie-analyzer)

## Install

Run `pip3 install -r requirements/prod.txt` to install all requirements.

## Example

Command `du -ab | ./piea.py --file example/piea.html`
produces [this html](<example/piea.html>).

## Typical usage

It's intended to be used with du
([unix](https://en.wikipedia.org/wiki/Du_%28Unix%29),
[windows](https://docs.microsoft.com/en-us/sysinternals/downloads/du))
utility.

## Typical usage (unix)

Run this command:

``` bash
du folder/to/analyze | python3 piea.py
```

File `temp_pie.html` will be created with interactive sunburst chart of your folder.
Also your default browser will open this file.

### du hints

If there are too many directories, browser can be slow in rendering the chart.

It can be solved by passing some thresholds to du.

This command will show only folders that are bigger than 10KB:
``` bash
du --threshold=10K folder/to/analyze | python3 piea.py
```

This command will show only folders that are 3 levels deep:
``` bash
du --max-depth=3 folder/to/analyze | python3 piea.py
```

## Typical usage (windows)

I suggest using WSL (Windows Subsystem for Linux), but if you can't, do this in PowerShell:

``` powershell
du.exe -nobanner -c -v folder\to\analyze | ConvertFrom-Csv | % {$_.DirectorySize + " " + ($_.Path -replace "\\","/")} | python.exe piea.py
```

Maybe I will find an easier way to do this. If not, it will probably be encapsulated in a script later.

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

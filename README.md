# fuzzydirfilter
Fuzzy Directory Filter

## Description

This is a filter that fetches partial matching rows from
search_string from a list consisting of paths of directories on each line.

Matching is done as follows.

* Extract the last part separated by `/` of the directory path
* Find the partial ratio with retrieved substring and search_string using `partial_ratio` function of FuzzyWuzzy
* Match if ratio > threshold. 

## Usage

```terminal
fuzzydirfilter [-h] [--threshold THRESHOLD]
                      search_string [file [file ...]]

positional arguments:
  search_string
  file

optional arguments:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
```

## Environment

| VARIABLE | DESCRIPTION |
|----------|-------------|
| FUZZYDIRFILTER_THRESHOLD | Set threshold value when no `--threshold` option is given |

## Install

```bash
pip install git+https://github.com/crhg/fuzzydirfilter.git
```

## Example to replace fuzzy filter of `enhancd`

(In `.zshrc` after loading `enhancd`)

```zsh
__enhancd::filter::fuzzy() # redefine 
{
    if [[ -z $1 ]]; then
        cat <&0
    else
        if [[ $ENHANCD_USE_FUZZY_MATCH == 1 ]]; then
            if (( ${+commands[fuzzydirfilter]} )); then
                fuzzydirfilter "$1"
            else
                awk \
                    -f "$ENHANCD_ROOT/src/share/fuzzy.awk" \
                    -v search_string="$1"
            fi
        else
            # Case-insensitive (don't use fuzzy searhing)
            awk '$0 ~ /\/.?'"$1"'[^\/]*$/{print $0}' 2>/dev/null
        fi
    fi
}
```

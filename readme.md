# catsay

A cuter alternative to cowsay.

```
$ ./catsay.py --help
usage: catsay.py [-h] [--eyes string] [--mouth string] [--border-h string]
                 [--border-v string]
                 [string ...]

positional arguments:
  string             a list of strings which will be separated by spaces, if omitted
                     stdin is used

options:
  -h, --help         show this help message and exit
  --eyes string      eyes, may be two characters long (default: 'o')
  --mouth string     mouth (default: '-')
  --border-h string  horizontal border (default: '-')
  --border-v string  vertical border (default: '|')

$ ./catsay.py Hello :3
  /\_/\      ----------
 ( o o )    | Hello :3 |
 ( >-< )     ----------
/  , ,  \  /
|| | | ||     _
\| | | |/____//
 (_)-(_)------

$ fortune | ./catsay.py --eyes "><" --mouth w
  /\_/\      -----------------------
 ( > < )    | I can relate to that. |
 ( >w< )     -----------------------
/  , ,  \  /
|| | | ||     _
\| | | |/____//
 (_)-(_)------
```

(newlines added afterwards)

## To do

- Options for wrapping or truncating long lines

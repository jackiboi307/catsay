# catsay

A cuter alternative to cowsay.

```
$ ./catsay.py --help
usage: catsay.py [-h] [--eyes string] [--mouth string] [--border-h string] [--border-v string]
                 [--tab-size int]
                 [string ...]

positional arguments:
  string             a list of strings which will be separated by spaces, if omitted stdin is used

options:
  -h, --help         show this help message and exit
  --eyes string      eyes, may be two characters long (default: 'O')
  --mouth string     mouth (default: 'w')
  --border-h string  horizontal border (default: '-')
  --border-v string  vertical border (default: '|')
  --tab-size int     tab size in spaces (default: 4)

$ ./catsay.py Hello :3
  /\_/\      ----------
 ( O O )    | Hello :3 |
 ( >w< )     ----------
/  , ,  \  /
|| | | ||     _
\| | | |/____//
 (_)-(_)------

$ fortune | ./catsay.py --eyes ">O" --mouth u
             ------------------------------------------------------------
  /\_/\     | When you die, you lose a very important part of your life. |
 ( > O )    |         -- Brooke Shields                                  |
 ( >u< )     ------------------------------------------------------------
/  , ,  \  /
|| | | ||     _
\| | | |/____//
 (_)-(_)------
```

(newlines added afterwards)

## Why?

- Cowsay sucks
- This cat is way cuter than any other ASCII-cat
- It is proper ASCII
- Sorry, I take that back, cowsay is actually okay

## To do

- Options for wrapping or truncating long lines
- An AI-generated translation to some language like Go, Rust or C

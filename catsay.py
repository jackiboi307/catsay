#!/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--eyes',     type=str, metavar="string", dest="eyes",    default='o',
                    help="eyes, may be two characters long (default: 'o')")
parser.add_argument('--mouth',    type=str, metavar="string", dest="mouth",   default='-',
                    help="mouth (default: '-')")
parser.add_argument('--border-h', type=str, metavar="string", dest="borderh", default='-',
                    help="horizontal border (default: '-')")
parser.add_argument('--border-v', type=str, metavar="string", dest="borderv", default='|',
                    help="vertical border (default: '|')")

parser.add_argument('message', nargs='*', type=str, metavar="string",
                    help="a list of strings which will be separated by spaces, if omitted stdin is used")

args = parser.parse_args()

eyes    = args.eyes
mouth   = args.mouth
borderh = args.borderh
borderv = args.borderv
message = args.message

assert len(eyes) in (1, 2)
assert len(mouth) == 1
assert len(borderh) == 1
assert len(borderv) == 1

if len(message) == 0:
    message = []
    while True:
        try:
            message.append(input())
        except EOFError:
            break

else:
    message = " ".join(message).splitlines()

# cat = f"""
#  /\\/\\
# /    \\  {message}
# | oo  | /           _
# \\> - <\\______       \\\\
#  \\           \\      //
#   \\___________X====/
# """[1:-1]

longest = 0
for line in message:
    if longest < len(line):
        longest = len(line)

borderh = borderh * (longest+2)

cat = r"""
  /\_/\
 ( R R )
 ( >R< )     R
/  , ,  \  /
|| | | ||     _
\| | | |/____//
 (_)-(_)------
"""[1:-1].replace("R", "{}").format(
    eyes if len(eyes) == 1 else eyes[0],
    eyes if len(eyes) == 1 else eyes[1],
    mouth,
    borderh,
)

cat = "\n" * (len(message) - 1) + cat
cat = cat.splitlines()


for i in range(len(message) + 1):
    if len(cat[i]) < 12:
        cat[i] += " " * (12 - len(cat[i]))

    if i != 0:
        cat[i] += borderv + " " + message[i-1] + \
            " " * (longest - len(message[i-1])) + " " + borderv

cat[0] += " " + borderh

for i, line in enumerate(message):
    pass

cat = "\n".join(cat)

print(cat)

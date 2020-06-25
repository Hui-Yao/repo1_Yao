import argparse
parser = argparse.ArgumentParser()

parser.add_argument("echo", help="ehco info")
parser.add_argument("number", help="integer", type=int)
parser.add_argument("--verb", help="optional number", type=str)

args = parser.parse_args()
echo = args.echo
num  = args.number
verb = args.verb

print( type(echo), echo )
print( type(num), num )
print( type(verb), verb )

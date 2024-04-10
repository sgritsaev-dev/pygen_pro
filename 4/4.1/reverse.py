import sys
from datetime import *
lines_list=[line for line in sys.stdin if line.strip().startswith('#')]
print(len(lines_list))

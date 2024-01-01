import datetime
import sys

e = datetime.datetime.now()
print(f"processed data at {e}\n")

for line in sys.stdin:
  print(line)

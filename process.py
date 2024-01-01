import datetime
import sys

e = datetime.datetime.now()
print(f"processed data at {e}")

for line in sys.stdin:
  print(line)

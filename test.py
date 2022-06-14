import subprocess
import sys

from tests_parse import test_parse
from tests_correctness import test_correctness1

process = subprocess.run(['bash', './kompiluj.sh'], cwd='..')

tests = [
	test_parse,
	test_correctness1
	]

debug = False
if len(sys.argv) > 1:
	if sys.argv[1] == "debug":
		debug = True

print("")
print("")
print("")
print("-------------------------TESTY-----------------------------")
print("")
for t in tests:
	t(debug)

from sys import argv, exit


if len(argv) != 2:
    print "Usage: python sorter <hashtag_file>"
    exit()


f = open(argv[1])
file_content = f.read()
f.close()

lines = file_content.split("\n")
results = []

for line in lines:
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    results.append((parts[0], parts[1]))

sorted_results = sorted(results, key=lambda x: int(x[1]))
sorted_results = sorted_results[::-1]

f = open("sorted_" + argv[1], 'w')
for result in sorted_results:
    f.write(result[0] + " " + result[1] + "\n")
f.close()

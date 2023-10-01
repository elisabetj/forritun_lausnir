import sys

line = sys.stdin.readline().rstrip('\n')
cnt = 0
s = line.split('-')
cnt += int(s[1]) - int(s[0])

sys.stdout.write("%d\n" % cnt)

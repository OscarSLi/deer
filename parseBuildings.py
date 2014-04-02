import re
import sys
import fileinput

def main():
    pattern = re.compile('placemark">[\w\- ,\'()]*</a')
    p = re.compile('\d+')
    for line in fileinput.input():
        list =  pattern.findall(line)
        for elem in list:
            print elem[11:-3]
main()

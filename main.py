import threading
from queue import Queue

from fake_sender import FakeSender
from syntax_analyzer import SyntaxAnalyzer


def main():
    global fs
    fs = FakeSender()
    analyzer = SyntaxAnalyzer()
    analyzer.percent_analyzer([2,2,2,2,3,3,3],8)


#print(fs.get_queue().qsize())

if __name__ == "__main__":
    main()

from analyzer import Analyzer
from fake_sender import FakeSender
from list_parser import ListParser


def main():
    global fs, analyzer
    fs = FakeSender()
    analyzer = Analyzer(fs.get_queue(), 11)

#print(fs.get_queue().qsize())

if __name__ == "__main__":
    main()

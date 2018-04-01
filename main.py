from analyzer import Analyzer
from fake_sender import FakeSender
from list_parser import ListParser
from interface import Interface


def main():
    global fs, analyzer
    fs = FakeSender()
    analyzer = Analyzer(fs.get_queue(), 11)
    interface = Interface()

#print(fs.get_queue().qsize())

if __name__ == "__main__":
    main()

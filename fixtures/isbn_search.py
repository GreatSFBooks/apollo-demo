import sys
import json
import isbnlib

if __name__ == "__main__":

    values = set()

    if len(sys.argv) != 2:
        print("Usage: isbn_search.py books.json\n")
        sys.exit(1)

    new_data = []
    for item in json.loads(open(sys.argv[1], 'r').read()):
        isbn = isbnlib.isbn_from_words("%s %s" % (item['title'], item['author']))
        item['isbn'] = isbn
        print("%s - %s" % (item['title'], item['isbn']))
        new_data.append(item)

    out_file = open('test.json', 'w')
    out_file.write(json.dumps(new_data, indent=4))
    out_file.close()
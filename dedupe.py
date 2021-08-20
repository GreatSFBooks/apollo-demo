import sys
import json

if __name__ == "__main__":

    values = set()

    if len(sys.argv) != 3:
        print("Usage: dedupe.py filename.json key_name\n")
        sys.exit(1)

    key_to_test = sys.argv[2]
    new_data = []

    for item in json.loads(open(sys.argv[1], 'r').read()):
        for k, v in item.items():
            if k == key_to_test:
                if v in values:
                    # Dupe, skip it
                    continue
                else:
                    values.add(v)
                    new_data.append(item)


    # Re write file with new data.

    out_file = open(sys.argv[1], 'w')
    out_file.write(json.dumps(new_data, indent=4))
    out_file.close()


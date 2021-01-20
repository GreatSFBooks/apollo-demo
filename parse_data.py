import csv
import json
import wikipedia
import re

date_range = re.compile(r'\(([A-Za-z]+) ([0-9]{1,2}), ([0-9]{4}) – ([A-Za-z]+) ([0-9]{1,2}), ([0-9]{4})\)')
born_on = re.compile(r'\(born ([A-Za-z]+) ([0-9]{1,2}), ([0-9]{4})\)')

books = []
awards = []
authors = []

other_source1 = json.loads(open('award_data_1.json').read())
other_source1_db = {}

# Index by work title
for work in other_source1:
    other_source1_db[work['title']] = work


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:

            extra_data = None
            try:
                extra_data = other_source1_db[row[0]]
            except:
                print("Extra data miss: %s" % row[0])
                pass

            books.append({
                'title': row[0],
                'author': row[1],
                'published_date': row[2]
            })

            author_data = {
                'name': row[1],
                'whereBorn': '',
                'yearBorn': None,
                'yearDied': None
            }

            try:
                author = wikipedia.page("%s (author)" % row[1])
                print("Found wikipedia page: ", author.title)
                author_data['biography'] = author.summary

                age_range = date_range.search(author.content)
                if age_range:
                    print("Match age range.")
                    author_data['yearBorn'] = int(age_range.group(3))
                    author_data['yearDied'] = int(age_range.group(6))
                else:
                    born = born_on.search(author.content)
                    if born:
                        author_data['yearBorn'] = int(born.group(3))
            except:
                pass


            authors.append(author_data)

            if row[3] == '1':
                yearWon = None
                if extra_data is not None:
                    if "Hugo" in extra_data['winner']:
                        yearWon = int(extra_data['year'])
                awards.append({
                    'bookTitle': row[0],
                    'year': yearWon,
                    'authorName': row[1],
                    'awardName': 'Hugo Award',
                    'awardTitle': 'Best Novel'

                })
            if row[4] == '1':
                
                yearWon = None
                if extra_data is not None:
                    if "Nebula" in extra_data['winner']:
                        yearWon = int(extra_data['year'])
                awards.append({
                    'bookTitle': row[0],
                    'year': yearWon,
                    'authorName': row[1],
                    'awardName': 'Nebula Award',
                    'awardTitle': 'Best Novel'
                })
            if row[5] == '1':
                yearWon = None
                if extra_data is not None:
                    if "Locus" in extra_data['winner']:
                        yearWon = int(extra_data['year'])
                awards.append({
                    'bookTitle': row[0],
                    'year': yearWon,
                    'authorName': row[1],
                    'awardName': 'Locus Award',
                    'awardTitle': 'Best Novel'
                })
            
            line_count += 1


    print(f'Processed {line_count} lines.')

with open('authors/authors.json', 'w') as authors_file:
    authors_file.write(json.dumps(authors, indent=4))

with open('awards-graphene/awards.json', 'w') as awards_file:
    awards_file.write(json.dumps(awards, indent=4))

with open('books/books.json','w') as books_file:
    books_file.write(json.dumps(books, indent=4))
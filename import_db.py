#!/usr/bin/env python3
import csv
import sys
import sqlite3

f = open(sys.argv[1],'rt')
count = 0
DB_LOCATION='./play.db'
print('Here we go!')
REVIEW_THRESHOLD = 700

try:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        count += 1
        if (count % 100 == 0):
            print('Reading: %s' % count)
        if count == 1:
            continue # Skip label line
        #if count == 10000:
        #    break
        name = row[0]
        developer = row[1]
        developerurl = row[3]
        category = row[5]
        isfree = row[6]
        price = row[7]
        reviewers = int(row[8])
        score = row[9]
        #print("%s\t %s\t %s\t %s\t %s\t%s\t %s\t %s\t %s" % (count, name, developer, developerurl, category, isfree, price, reviewers, score))
        #if isinstance(reviewers, str):
            #print ('skipping')
        #    continue
        if int(reviewers) < REVIEW_THRESHOLD:
            #print ('skipping due to low reviewers')
            continue
        db = sqlite3.connect(DB_LOCATION) 
        cursor = db.cursor()
        try:
            cursor.execute('''INSERT INTO
                apps(name, developer, developerurl, category, isfree, price, reviewers, score) VALUES(?,?,?,?,?,?,?,?)''',
                (name, developer, developerurl, category, isfree, price, reviewers, score) )
            #print('Added to database: ' + name)
            db.commit()
        except sqlite3.IntegrityError:
            print('.')
            sys.stdout.write('.')
            sys.stdout.flush() # Prints a dot without the newline
        db.close()

finally:
    f.close()
print('Done. No of records read: ' + count)

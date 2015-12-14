# Google Play App Stats

* Scripts to do some simple analysis of apps in Google Play
* Requires a dump of crawled Google Play data. Get it here: https://github.com/MarcelloLins/GooglePlayAppsCrawler

## Howto
1. Get raw data dump
1. Generate local sqlite database with `import_db.py <RAW DATA DUMP CSV>`
2. Generate outputs with: `sqlite3 play.db < export.sql`



Create initial DB table with
```
CREATE TABLE "main"."apps" (
    "name" TEXT unique,
    "developer" TEXT,
    "developerurl" TEXT,
    "category" TEXT,
    "isfree" TEXT,
    "price" REAL,
    "reviewers" INTEGER,
    "score" REAL
);
```

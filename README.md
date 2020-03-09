# wordwise-dict
Amazon Kindle Wordwise dictionary extract from WordWise.kll.en.en.db

This work based on research of @tmilovanov at https://github.com/tmilovanov/wisecreator/ , his research on Amazon Kindle Wordwise is excellent

Just clone this project and run db2csv.py (Python 2.7) for extract Wordwise Dictionary from WordWise.kll.en.en.db
you can copy new WordWise.kll.en.en.db from your Android phone at path /data/data/com.amazon.kindle/databases/wordwise/WordWise.kll.en.en.db

Preprocessed file wordwise-dict.csv is output of script above with headers:

id, word, full_def, short_def, example_sentence, hint_level

word and short_def is what Amazon Kindle Wordwise show on its books

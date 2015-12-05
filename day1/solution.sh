expr $(grep "(" input_1.txt --only-matching | wc -l) - $(grep ")" input_1.txt --only-matching | wc -l)

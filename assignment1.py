#assignment 1 - Store the unique words and their count in the document collection in a file wordCount.txt.


form parse-xml import parsexml

from word-counter import word_count

final_string = ""

final_string = parsexml('hindi-document-00001.xml') + " " + parsexml('hindi-document-00002.xml') + " " + parsexml('hindi-document-00003.xml')

print word_count(final_string)
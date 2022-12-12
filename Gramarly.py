# import TextBlob
from textblob import TextBlob

a = TextBlob("CampK12 is a goud compny and alays valule thier imployeez")

# using Textblob.correct() method
a = a.correct()

print(a)
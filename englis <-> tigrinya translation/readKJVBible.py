from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

import re
openEnglish = open('new_kJV.txt', 'r')
readEnglish = openEnglish.read()
# readLine = openEnglish.readlines()

# chapters = ["ምዕራፍ 1", "ምዕራፍ 2", "ምዕራፍ 3", "ምዕራፍ 4", "ምዕራፍ 5", "ምዕራፍ 6", "ምዕራፍ 7", "ምዕራፍ 8", "ምዕራፍ 9", "ምዕራፍ 10", "ምዕራፍ 11", "ምዕራፍ 12", "ምዕራፍ 13", "ምዕራፍ 14", "ምዕራፍ 15", "ምዕራፍ 16", "ምዕራፍ 17", "ምዕራፍ 18", "ምዕራፍ 19", "ምዕራፍ 20", "ምዕራፍ 21", "ምዕራፍ 22", "ምዕራፍ 23", "ምዕራፍ 24", "ምዕራፍ 25", "ምዕራፍ 26", "ምዕራፍ 27", "ምዕራፍ 28", "ምዕራፍ 29", "ምዕራፍ 30", "ምዕራፍ 31", "ምዕራፍ 32", "ምዕራፍ 33", "ምዕራፍ 34", "ምዕራፍ 35", "ምዕራፍ 36", "ምዕራፍ 37", "ምዕራፍ 38", "ምዕራፍ 39", "ምዕራፍ 40", "ምዕራፍ 41", "ምዕራፍ 42", "ምዕራፍ 43", "ምዕራፍ 44", "ምዕራፍ 45", "ምዕራፍ 46", "ምዕራፍ 47", "ምዕራፍ 48", "ምዕራፍ 49", "ምዕራፍ 50", "ምዕራፍ 51", "ምዕራፍ 52", "ምዕራፍ 53", "ምዕራፍ 54", "ምዕራፍ 55", "ምዕራፍ 56", "ምዕራፍ 57", "ምዕራፍ 58", "ምዕራፍ 59", "ምዕራፍ 60", "ምዕራፍ 61", "ምዕራፍ 62", "ምዕራፍ 63", "ምዕራፍ 64", "ምዕራፍ 65", "ምዕራፍ 66", "ምዕራፍ 67", "ምዕራፍ 68",  "ምዕራፍ 69", "ምዕራፍ 70", "ምዕራፍ 71", "ምዕራፍ 72", "ምዕራፍ 73", "ምዕራፍ 74", "ምዕራፍ 75", "ምዕራፍ 76", "ምዕራፍ 77", "ምዕራፍ 78", "ምዕራፍ 79", "ምዕራፍ 80", "ምዕራፍ 81", "ምዕራፍ 82", "ምዕራፍ 83", "ምዕራፍ 84", "ምዕራፍ 85", "ምዕራፍ 86", "ምዕራፍ 87", "ምዕራፍ 88", "ምዕራፍ 89", "ምዕራፍ 90", "ምዕራፍ 91", "ምዕራፍ 92", "ምዕራፍ 93", "ምዕራፍ 94", "ምዕራፍ 95", "ምዕራፍ 96", "ምዕራፍ 97", "ምዕራፍ 98", "ምዕራፍ 99", "ምዕራፍ 100", "ምዕራፍ 101", "ምዕራፍ 102", "ምዕራፍ 103", "ምዕራፍ 104", "ምዕራፍ 105", "ምዕራፍ 106", "ምዕራፍ 107", "ምዕራፍ 108", "ምዕራፍ 109", "ምዕራፍ 110", "ምዕራፍ 111", "ምዕራፍ 112", "ምዕራፍ 113", "ምዕራፍ 114", "ምዕራፍ 115", "ምዕራፍ 116", "ምዕራፍ 117", "ምዕራፍ 118", "ምዕራፍ 119", "ምዕራፍ 120", "ምዕራፍ 121", "ምዕራፍ 122", "ምዕራፍ 123", "ምዕራፍ 124", "ምዕራፍ 125", "ምዕራፍ 126", "ምዕራፍ 127", "ምዕራፍ 128", "ምዕራፍ 129", "ምዕራፍ 130", "ምዕራፍ 131", "ምዕራፍ 132", "ምዕራፍ 133", "ምዕራፍ 134", "ምዕራፍ 135", "ምዕራፍ 136", "ምዕራፍ 137", "ምዕራፍ 138", "ምዕራፍ 139", "ምዕራፍ 140", "ምዕራፍ 141", "ምዕራፍ 142", "ምዕራፍ 143", "ምዕራፍ 144", "ምዕራፍ 145", "ምዕራፍ 146", "ምዕራፍ 147", "ምዕራፍ 148", "ምዕራፍ 149", "ምዕራፍ 150"]
# books = ["ኦሪት ዘፍጥረት", "ኦሪት ዘጸአት", "ኦሪት ዘሌዋውያን", "ኦሪት ዘህልቍ", "ኦሪት ዘዳግም", "መጽሓፍ ኢያሱ ወልደ ነዌ", "መጽሓፍ መሣፍንቲ", "መጽሓፍ ሩት", "1ይ መጽሓፍ ሳሙኤል", "2ይ መጽሓፍ ሳሙኤል", "1ይ መጽሓፍ ነገስታት", "2ይ መጽሓፍ ነገስታት", "1ይ መጽሓፍ ዜና መዋዕል", "2ይ መጽሓፍ ዜና መዋዕል", "መጽሓፍ ዕዝራ", "መጽሓፍ ነህምያ", "መጽሓፍ ኣስቴር", "መጽሓፍ ኢዮብ", "መዝሙር ዳዊት", "መጽሓፍ ምሳሌ", "መጽሓፍ መክብብ", "መኃልየ መኃልየ ዘሰሎሞን", "ትንቢት ኢሳይያስ", "ትንቢት ኤርምያስ", "ድጒዓ ኤርምያስ", "ትንቢት ሕዝቅኤል", "ትንቢት ዳንኤል", "ትንቢት ሆሴዕ", "ትንቢት ኢዮኤል", "ትንቢት አሞጽ", "ትንቢት አብድዩ", "ትንቢት ዮናስ", "ትንቢት ሚክያስ", "ትንቢት ናሆም", "ትንቢት ዕንባቆም", "ትንቢት ሶፎንያስ", "ትንቢት ሐጌ", "ትንቢት ዘካርያስ", "ወንጌል ማቴዎስ", "ወንጌል ማርቆስ", "ወንጌል ሉቃስ", "ወንጌል ዮሐንስ", "ግብሪ ሃዋርያት", "መልእኽቲ ፓውሎስ ናብ ሰብ ሮሜ", "1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ቆሮንቶስ", "2ይ መልእኽቲ ፓውሎስ ናብ ሰብ ቆሮንቶስ", "መልእኽቲ ፓውሎስ ናብ ሰብ ገላትያ", "መልእኽቲ ፓውሎስ ናብ ሰብ ኤፌሶን", "መልእኽቲ ፓውሎስ ናብ ሰብ ፊሊጲ", "መልእኽቲ ፓውሎስ ናብ ሰብ ቆሎሴ", "1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ተሰሎንቄ", "2ይ መልእኽቲ ፓውሎስ ናብ ሰብ ተሰሎንቄ", "1ይ መልእኽቲ ፓውሎስ ናብ ሰብ ጢሞቴዎስ", "2ይ መልእኽቲ ፓውሎስ ናብ ሰብ ጢሞቴዎስ", "መልእኽቲ ፓውሎስ ናብ ሰብ ቲቶ", "መልእኽቲ ፓውሎስ ናብ ሰብ ፊልሞና", "መልእኽቲ ፓውሎስ ናብ ሰብ ዕብራውያን", "መልእኽቲ ያዕቆብ", "1ይ መልእኽቲ ጴጥሮስ", "2ይ መልእኽቲ ጴጥሮስ", "1ይ መልእኽቲ ዮሐንስ", "2ይ መልእኽቲ ዮሐንስ", "3ይ መልእኽቲ ዮሐንስ", "መልእኽቲ ይሁዳ", "ራእይ ዮሐንስ"]
books = ["GENESIS #", "EXODUS #", "LEVITICUS #", "NUMBERS #", "DEUTERONOMY #", "JOSHUA #", "JUDGES #", "RUTH #", "# SAMUEL", "# KINGS", "# CHRONICLES", "EZRA #", "NEHEMIAH #", "ESTHER #", "JOB #", "PSALMS #", "PROVERBS #", "ECCLESIASTES #", "SONG OF SOLOMON #", "ISAIAH #", "JEREMIAH #", "LAMENTATIONS #", "EZEKIEL #", "DANIEL #", "HOSEA #", "JOEL #", "AMOS #", "OBADIAH #", "JONAH #", "MICAH #", "NAHUM #", "HABAKKUK #", "ZEPHANIAH #", "HAGGAI #", "ZECHARIAH #", "MALACHI #", "MATTHEW #", "MARK #", "LUKE #", "JOHN #", "ACTS OF THE APOSTLES #", "ROMANS #", "# CORINTHIANS", "GALATIANS #", "EPHESIANS #", "PHILIPPIANS #", "COLOSSIANS #", "# THESSALONIANS", "# TIMOTHY", "# TIMOTHY", "TITUS #", "PHILEMON #", "HEBREWS #", "JAMES #", "# PETER", "# JOHN", "JUDE #", "REVELATION #"]
# for chapter in chapters:
# 	if chapter in readEnglish:
# 		readEnglish = readEnglish.replace(chapter, '')
# for book in books:
# 	if book in readEnglish:
# 		readEnglish = readEnglish.replace(book, '')

#replace all words with # tag
# readEnglish = readEnglish.lower()
chapters = []
for i in range (151):
	chapters.append(str(i))

for number in chapters:
	if number in readEnglish:
		readEnglish = readEnglish.replace(number, "#")

for book in books:
	if book in readEnglish:
		readEnglish = readEnglish.replace(book, '')

normalizedT = re.sub(r"[^a-zA-Z.]", " ", readEnglish)



split_by_dot = normalizedT.split(".")
remove_stop_word = [word for word in split_by_dot if word not in stopwords.words("english")]
print("length of english sentences: ", len(split_by_dot))
getText = open('write_english.txt', 'w')
# getText.writelines(list1)
getText.write('\n'.join(str(val.strip()) for val in remove_stop_word))
# print(split_by_dot)
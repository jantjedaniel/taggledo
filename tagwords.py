file = open("tagwords.txt")
tag_words_map = {} # Map of tags to words.
for line in file:
    # Skip comments and empty lines.
    line = line.strip()
    if len(line) == 0 or line.startswith("#"):
        continue
    tag = ""
    
    # Is there a word followed by a colon? If so, it is the tag, but don't include the tag in the value words.
    words_split_by_colon = line.split(":")
    if (len(words_split_by_colon) == 2):
        tag = words_split_by_colon[0]
        word_string = words_split_by_colon[1].strip()
    elif (len(words_split_by_colon) == 1):
        word_string = words_split_by_colon[0]
    else:
        continue
    
    # Get the value words. They are comma separated. If we don't have a tag yet, it is the zeroth value word.
    value_words = word_string.split(",")
    if tag == "":
        tag = value_words[0]
    
    # Add the tag->words pair to the dictionary (i.e. to the map).
    tag_words_map[tag] = value_words
file.close()
print(tag_words_map)
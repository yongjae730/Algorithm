word = input().upper()
word_list = list(set(word))

word_count = []
for i in word_list:
  count = word.count
  word_count.append(count(i))

if word_count.count(max(word_count)) > 1:
  print("?")

else:
  print(word_list[(word_count.index(max(word_count)))])
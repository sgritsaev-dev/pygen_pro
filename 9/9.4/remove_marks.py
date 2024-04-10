def remove_marks(text, marks):
    remove_marks.count+=1
    for mark in marks:
        text = text.replace(mark, '')
    return text
remove_marks.count=0
marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))
    
print(remove_marks.count)
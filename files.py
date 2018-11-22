# how to open a new file
# open is the method and it takes the path to the file and then the mode.
# in our case the mode is w for "write"
# WRITE to files
fo = open('text.txt', 'w')
print('Name: ', fo.name)
print('is closed: ', fo.closed)
print('opening mode: ', fo.mode)
fo.write('Python is great ')
fo.write(', JavaScript is awesome, ')
fo.close()

# if we close the file above and then reopen with write mode on it overwrites everyhting in the file. if we change ht emode to "a" for append then it will re-open the file and add the string without overwriting everything that was previously there
# fo = open('text.txt', 'w')

# APPEND files with 'a'
fo = open('text.txt', 'a')
fo.write('and php is super!')
fo.close()

# READ files into our script 'r+'
fo = open('text.txt', 'r+')
# text = fo.read()
text = fo.read(10)
#will get us jsut the first 10 characters
print(text)
fo.close()

# CREATE a file 'w+'
fo = open('test2.txt', 'w+')
fo.write('This is my new file')
fo.close()

filenames = ['1.doc', '1.report', '1.represatation']
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)

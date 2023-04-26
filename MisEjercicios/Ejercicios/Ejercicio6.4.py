filenames = [r"C:\Users\enio2\Downloads\Cursos\Python\a.txt",
             r"C:\Users\enio2\Downloads\Cursos\Python\a.txt",
             r"C:\Users\enio2\Downloads\Cursos\Python\a.txt"]
for filename in filenames:
    file = open(filename, "r")
    content = file.read()
    print(content)
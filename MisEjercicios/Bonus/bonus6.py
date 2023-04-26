contents = ["Los carros bajan muy rápido por la calle",
            "La comida de acá me gusta más porque la siento como en casa",
            "El calor de acá es insoportable"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filenames in zip(contents, filenames):
    file = open(f"../Ejercicios/ModulosImportantesYAnexos/{filenames}", "w")
    file.write(content)

a = "Hola buenas tardes" \
    "cómo estás, Dios te bendiga" \
    "bella dama"
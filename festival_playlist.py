def agregar_canciones(nombres, artistas, duraciones, popularidades):
    n = int(input("¿Cuántas canciones deseas agregar? "))
    for _ in range(n):
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración en minutos: "))
        popularidad = int(input("Popularidad (1-100): "))
        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

def ver_reportes(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return
    print("Total de canciones:", len(nombres))
    print("Duración total:", sum(duraciones), "minutos")
    max_pop = max(popularidades)
    min_pop = min(popularidades)
    idx_max = popularidades.index(max_pop)
    idx_min = popularidades.index(min_pop)
    print("Canción más popular:", nombres[idx_max], "-", artistas[idx_max], "(", max_pop, ")")
    print("Canción menos popular:", nombres[idx_min], "-", artistas[idx_min], "(", min_pop, ")")
    print("Promedio de popularidad:", sum(popularidades) / len(popularidades))

def buscar_canciones(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return
    print("1. Buscar por artista")
    print("2. Buscar por rango de popularidad")
    op = input("Elige una opción: ")
    if op == "1":
        art = input("Artista a buscar: ")
        encontrado = False
        for i in range(len(nombres)):
            if artistas[i].lower() == art.lower():
                print(nombres[i], "-", artistas[i], "| Popularidad:", popularidades[i])
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones.")
    elif op == "2":
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))
        encontrado = False
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print(nombres[i], "-", artistas[i], "| Popularidad:", popularidades[i])
                encontrado = True
        if not encontrado:
            print("No se encontraron canciones.")

def playlist_recomendada(nombres, artistas, duraciones, popularidades):
    if len(nombres) == 0:
        print("No hay canciones registradas.")
        return
    prom = sum(popularidades) / len(popularidades)
    print("Playlist recomendada (popularidad > promedio):")
    encontrado = False
    for i in range(len(nombres)):
        if popularidades[i] > prom:
            print(nombres[i], "-", artistas[i], "| Popularidad:", popularidades[i])
            encontrado = True
    if not encontrado:
        print("No hay canciones que superen el promedio.")

def menu():
    nombres = []
    artistas = []
    duraciones = []
    popularidades = []
    while True:
        print("\n--- FESTIVAL PLAYLIST ---")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "2":
            ver_reportes(nombres, artistas, duraciones, popularidades)
        elif opcion == "3":
            buscar_canciones(nombres, artistas, duraciones, popularidades)
        elif opcion == "4":
            playlist_recomendada(nombres, artistas, duraciones, popularidades)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()

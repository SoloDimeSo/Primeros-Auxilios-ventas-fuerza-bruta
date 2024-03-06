def primeros_auxilios():
    respuesta_estimulo = input("¿Responde a estímulos? (Si/No): ").lower()
    
    if respuesta_estimulo == "si":
        necesidad_hospital = input("¿Valorar la necesidad de llevarlo al hospital? (Si/No): ").lower()
        if necesidad_hospital == "si":
            print("Llevar al hospital.")
    else:
        respira = input("¿Abre la vía aérea? ¿Respira? (Si/No): ").lower()
        if respira == "si":
            print("Permitirle posición de suficiente ventilación")
        else:
            administrar_ventilaciones = input("No respira. ¿Administrar 5 ventilaciones y llamar a la ambulancia? (Si/No): ").lower()
            if administrar_ventilaciones == "si":
                print("Administrar 5 ventilaciones y llamar a la ambulancia.")
                signos_vida = input("¿Signos de vida? (Si/No): ").lower()
                if signos_vida == "no":
                    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
                    print("LLAMAR A UN FAMILIAR QUE LO VENGA A BUSCARS")
                else:
                    print("Reevaluar a la espera de la ambulancia.")
                    llego_ambulancia = input("¿Llegó la ambulancia? (Si/No): ").lower()
                    if llego_ambulancia == "si":
                        print("MANTENER LA CALMA. Esperar la llegada de la ambulancia.")
                    else:
                        print("Esperar la llegada de la ambulancia.")
            else:
                print("LLAMAR URGENTE A LA AMBULANCIA!")


# Ejecutar la función principal
primeros_auxilios()
def aggiungi_libro(titolo, copie, libreria):
    libreria[titolo]=copie #come chiave usiamo titolo e come vlaore usiamo le copie

def visualizza_libri(libreria):
    print("Elenco dei libri disponibili:")
    for titolo, copie in libreria.items():
        print(f"{titolo}:{copie} copie")

def cerca_libro(titolo, libreria):
    if titolo in libreria:
        return libreria [titolo]
    else:
        return 0

def rimuovi_libro(titolo, libreria):
    if titolo in libreria:
        del libreria [titolo]
        print(f"il libro'{titolo}' è stato rimosso dalla libreria")
    else:
        print(f"il libro'{titolo}' non è presente nella libreria")







def main():
    libreria = {}

    while True: 
      print ("\nMenu:")
      print("1. Aggiungi libro")
      print("2. Visualizza libri")
      print("3. Cerca libro")
      print("4. Rimuovi libro")
      print ("5. Esci")

      scelta=int(input("cosa vuoi fare ?"))

      if scelta== 1:
        titolo=input("Inserisci il titolo del libro: ")
        copie = int(input("Inserisci il numero di copie disponibili: "))
        aggiungi_libro(titolo, copie, libreria)   
      elif scelta==2:
        visualizza_libri(libreria)
      elif scelta==3:
        titolo=input("Inserisci il titolo del libro da cercare :")
        copie== cerca_libro (titolo)
        #print
      elif scelta==4:
        titolo=input("Inserisci il titolo del libro da eliminare: ")
        rimuovi_libro(titolo,libreria)
      elif scelta==5:
        print("Arrivederci !")
        break
      else:                
        print("scelta non valida. Riprova")



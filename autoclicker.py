import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pyautogui
import time

def lancer_script():
    try:
        # Récupère la valeur entrée
        valeur = entry.get()
        if valeur.strip() == "":
            status_label.config(text="Veuillez entrer un nombre valide", foreground="red")
            return
        
        nombre_de_clique = int(valeur)
        
        if nombre_de_clique <= 20000:
            status_label.config(text="Le script va se lancer dans 3 sec", foreground="white")
            root.update()  # Met à jour l'interface avant la pause
            time.sleep(3)
            pyautogui.click(clicks=nombre_de_clique, interval=0.0, button='left')
            status_label.config(text="Script terminé!", foreground="lightgreen")
        else:
            status_label.config(text="La limite est de 20000 clics", foreground="red")
    except ValueError:
        status_label.config(text="Veuillez entrer un nombre valide", foreground="red")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Auto-Clicker")
root.geometry("250x150")  # Taille de la fenêtre
root.configure(bg="#2E2E2E")  # Couleur de fond gris foncé

# URL de l'image d'icône
icon_url = 'https://i.pinimg.com/564x/da/b8/26/dab826d26a5b505a0e037ad9d762db80.jpg'  # Remplacez par le lien vers votre image d'icône

# Télécharger l'image depuis l'URL
response = requests.get(icon_url)
img_data = BytesIO(response.content)
image = Image.open(img_data)
icon = ImageTk.PhotoImage(image)

# Changer l'icône
root.iconphoto(True, icon)

# Permettre la transparence
root.attributes('-alpha', 0.9)  # Transparence de 90%

# Style des widgets
style = ttk.Style()
style.configure("TButton", background="#4CAF50", foreground="white", padding=6, relief="flat", font=("Helvetica", 10))
style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 10))

# Label pour les instructions
label = ttk.Label(root, text="Entrez le nombre de clics :")
label.pack(pady=10)

# Champ d'entrée pour le nombre de clics
entry = ttk.Entry(root)
entry.pack(pady=10)

# Bouton pour lancer le script
button = ttk.Button(root, text="Lancer", command=lancer_script)
button.pack(pady=10)

# Label pour afficher le statut
status_label = ttk.Label(root, text="", font=("Helvetica", 10))
status_label.pack(pady=10)

# Démarre la boucle principale de l'application
root.mainloop()

from tkinter import *

INPUT_WIDTH = 60

main_window = Tk()  # Crée la fenêtre principale
main_window.title("Vige'n'R")  # Titre de la fenêtre
main_window.geometry("800x600")  # Dimensions de la fenêtre


main_frame = Frame(main_window)
# TITLES
under_title = Label(main_frame, text="La cryptographie, c'est comme la magie !")
message_title = Label(main_frame, text="Inserer le message à encrypter ou décrypter")
encrypt_input_title = Label(main_frame, text="Inserer la d'encryptage")
# INPUTS
message_input = Text(main_frame, width=INPUT_WIDTH, height=10)
encrypt_key_input = Entry(main_frame, width=INPUT_WIDTH)


main_frame.pack(padx=40, pady=2)
under_title.pack(padx=10, pady=15)
message_title.pack(padx=10, pady=30)
message_input.pack()
encrypt_input_title.pack(padx=10, pady=20)
encrypt_key_input.pack()

main_window.mainloop()

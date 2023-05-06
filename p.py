import tkinter as tk

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chat")

        # Panel de mensajes
        self.message_frame = tk.Frame(master)
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        # Botón de enviar y cuadro de texto para ingresar mensaje
        self.input_frame = tk.Frame(master, bg="#eeeeee", pady=10)
        self.input_frame.pack(fill=tk.X)

        self.message_entry = tk.Entry(self.input_frame)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        self.send_button = tk.Button(self.input_frame, text="Enviar", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        # Lista de mensajes
        self.message_list = []

    def send_message(self):
        message = self.message_entry.get()

        # Agregar el mensaje enviado al panel de mensajes
        self.add_message(message, "right")
        self.add_message(message, "left")
        # Restablecer el cuadro de texto de entrada de mensajes
        self.message_entry.delete(0, tk.END)

    def add_message(self, message, justify):
        # Agregar el mensaje al panel de mensajes
        message_label = tk.Label(self.message_frame, text=message, justify=justify, wraplength=300, anchor= "e" if justify=="right" else "w", bg="#eeeeee", padx=5, pady=5)
        message_label.pack(side=tk.TOP, fill=tk.X, expand=True)

        # Agregar el mensaje a la lista de mensajes
        self.message_list.append((message, justify))

root = tk.Tk()
chat = ChatGUI(root)
root.mainloop()
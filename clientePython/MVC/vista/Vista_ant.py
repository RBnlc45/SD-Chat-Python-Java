import tkinter as tk

class Vista:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Cliente 2")

        self.listbox_chat = tk.Text(self.window, height=20, width=50)
        self.listbox_chat.pack()

        self.entry_message = tk.Entry(self.window, width=50)
        self.entry_message.pack()

        self.button_send = tk.Button(self.window, text="Enviar", command=self.send_message)
        self.button_send.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_message(self, message, justify="left"):
        self.listbox_chat.tag_configure(justify, justify=justify)
        self.listbox_chat.insert(tk.END, message +"\n", justify)

    def get_message(self):
        message = self.entry_message.get()
        self.entry_message.delete(0, tk.END)
        return message

    def send_message(self):
        message = self.get_message()
        if message:
            self.controller.enviarMensaje(message)
            self.add_message(message,justify="right")

    def on_close(self):
        self.controller.close_connection()
        self.window.destroy()

    def run(self):
        self.window.mainloop()

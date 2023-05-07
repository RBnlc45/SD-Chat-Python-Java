import tkinter as tk
import queue
import pika
import threading

class Vista:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Cliente 1")

        self.listbox_chat = tk.Text(self.window, height=20, width=50)
        self.listbox_chat.pack()

        self.entry_message = tk.Entry(self.window, width=50)
        self.entry_message.pack()

        self.button_send = tk.Button(self.window, text="Enviar", command=self.send_message)
        self.button_send.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_message(self, message, justify="left"):
        self.listbox_chat.tag_configure(justify, justify=justify)
        self.listbox_chat.insert(tk.END, message + "\n", justify)

    def get_message(self):
        message = self.entry_message.get()
        self.entry_message.delete(0, tk.END)
        return message

    def send_message(self):
        message = self.get_message()
        if message:
            self.controller.send_message(message)
            self.add_message(message, justify="right")

    def on_close(self):
        self.controller.close_connection()
        self.window.destroy()

    def run(self):
        self.window.mainloop()
        queue.put(None)


class Modelo:
    def __init__(self, cola,view=None, host='localhost', name="cliente1"):
        self.view = view
        self.host=host
        self.name=name
        #Yo cliente 1
        #establecer una conexión con el servidor RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel_receive = self.connection.channel()  # Canal para recibir mensajes
        self.channel_send = self.connection.channel()  # Canal para enviar mensajes

        # declarar una cola recibir en el servidor RabbitMQ
        self.channel_receive.queue_declare(queue="cliente1")
        #Cola para enviar los mensajes a cliente 2
        self.channel_send.queue_declare(queue="cliente2")

        def start_consuming(cola):
            #Recibir los mensajes colocados en mi queu cliente1
            self.channel_receive.basic_consume(queue='cliente1', on_message_callback=self.callback, auto_ack=True)
            try:
                self.channel_receive.start_consuming()
            except KeyboardInterrupt:
                self.channel_receive.stop_consuming()

            # Enviar un mensaje especial a la cola para indicar que la suscripción ha sido detenida
            cola.put(None)

        threading.Thread(target=start_consuming,args=(cola,),daemon=True).start()

    def callback(self,ch, method, properties, body):
        self.view.add_message(body.decode('utf-8'))

    def send_message(self, mensaje):
        #publicar mensaje en cola chat
        self.channel_send.basic_publish(exchange='', routing_key='cliente2', body=mensaje.encode('utf-8'))
        #self.view.add_message(mensaje)

    """def receive_message(self, channel, method, properties, body):
        print('pappa')
        #self.view.add_message(body.decode('utf-8'))
        #channel.basic_ack(delivery_tag=method.delivery_tag)*/"""
    def get_users(self):
        url = f'http://{self.host}:{15672}/api/queues'
        response = requests.get(url, auth=("guest", "guest"))
        queues = response.json()
        users=list()
        for queue in queues:
            user=queue['name'] 
            if user!= self.name: users.append(user)
        return user
    
    def close_connection(self):
        self.connection.close()

class Controlador:
    def __init__(self):
        self.view = Vista(self)
        self.queue=queue.Queue()
        self.model = Modelo(cola=self.queue,view=self.view)

    def send_message(self, message):
        self.model.send_message(message)

    def close_connection(self):
        self.model.close_connection()

    def run(self):
        self.view.run()

if __name__ == '__main__':
    controller = Controlador()
    controller.run()
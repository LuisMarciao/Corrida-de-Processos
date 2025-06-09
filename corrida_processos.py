import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time

class Processo:
    def __init__(self, nome, tempo_cpu):
        self.nome = nome
        self.tempo_cpu = tempo_cpu
        self.progresso = 0

class CorridaDeProcessosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("corrida de processos")
        self.processos = []
        self.barras = []
        self.politica = tk.StringVar(value="FIFO")

        self.setup_ui()

    def setup_ui(self):
        
        politicas = ["FIFO", "Round Robin"]
        tk.Label(self.root, text="escolha a política de escalonamento:").pack(pady=5)
        for p in politicas:
            tk.Radiobutton(self.root, text=p, variable=self.politica, value=p).pack()

        
        tk.Button(self.root, text="iniciar Corrida", command=self.iniciar_corrida).pack(pady=10)

        
        self.frame_barras = tk.Frame(self.root)
        self.frame_barras.pack(pady=10)

    def iniciar_corrida(self):
        
        for widget in self.frame_barras.winfo_children():
            widget.destroy()
        self.processos.clear()
        self.barras.clear()


        nomes = ["🐢 Tartaruga", "🐇 Coelho", "🚀 Foguete", "🏎️ Fórmula 1", "🦥 Bicho-Preguiça"]
        random.shuffle(nomes)
        n_processos = random.randint(3, 5)

        for i in range(n_processos):
            tempo_cpu = random.randint(5, 10)
            processo = Processo(nomes[i], tempo_cpu)
            self.processos.append(processo)

            tk.Label(self.frame_barras, text=processo.nome).pack()
            pb = ttk.Progressbar(self.frame_barras, length=300, maximum=tempo_cpu)
            pb.pack(pady=2)
            self.barras.append(pb)

        
        t = threading.Thread(target=self.executar_politica)
        t.start()

    def executar_politica(self):
        if self.politica.get() == "FIFO":
            self.fifo()
        else:
            self.round_robin()

        vencedor = min(self.processos, key=lambda p: p.progresso)
        messagebox.showinfo("vencedor!", f"o vencedor é: {vencedor.nome} ")

    def atualizar_barras(self):
        for i, p in enumerate(self.processos):
            self.barras[i]["value"] = p.progresso

    def fifo(self):
        for p in self.processos:
            while p.progresso < p.tempo_cpu:
                p.progresso += 1
                self.atualizar_barras()
                time.sleep(0.3)

    def round_robin(self, quantum=2):
        terminados = 0
        while terminados < len(self.processos):
            for p in self.processos:
                if p.progresso < p.tempo_cpu:
                    for _ in range(quantum):
                        if p.progresso < p.tempo_cpu:
                            p.progresso += 1
                            self.atualizar_barras()
                            time.sleep(0.3)
                    if p.progresso == p.tempo_cpu:
                        terminados += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = CorridaDeProcessosApp(root)
    root.mainloop()

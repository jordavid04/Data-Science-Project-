
# Autor: Jorge David Bolognesi 
# Matrícula: 2024001052
# Turma: 2
# Trabalho Final - Análise de Dados Eleitorais
import tkinter as tk
from tkinter import filedialog, messagebox

class InterfacePython:
    def __init__(self):
        # Configuração da janela principal
        self.janela = tk.Tk()
        self.janela.title("Análise de Dados Eleitorais")

        # Layout
        tk.Label(self.janela, text="Arquivo:").grid(row=0, column=0, sticky="w")
        self.arquivo_entry = tk.Entry(self.janela, width=40)
        self.arquivo_entry.grid(row=0, column=1, padx=5)
        tk.Button(self.janela, text="Procurar", command=self.selecionar_arquivo).grid(row=0, column=2, padx=5)

        # Checkboxes
        self.check_vars = {}
        for i in range(1, 7):
            var = tk.BooleanVar()
            self.check_vars[f"Funcao{i}"] = var
            tk.Checkbutton(self.janela, text=f"Função {i}", variable=var).grid(row=i, column=0, sticky="w")

        # Botões
        tk.Button(self.janela, text="Realizar", command=self.realizar).grid(row=7, column=0, pady=5)
        tk.Button(self.janela, text="Marcar todos", command=self.marcar_todos).grid(row=7, column=1, pady=5)
        tk.Button(self.janela, text="Desmarcar todos", command=self.desmarcar_todos).grid(row=7, column=2, pady=5)

    def selecionar_arquivo(self):
        """Abre o explorador de arquivos para selecionar um arquivo."""
        caminho = filedialog.askopenfilename(title="Selecione um arquivo")
        self.arquivo_entry.delete(0, tk.END)
        self.arquivo_entry.insert(0, caminho)

    def marcar_todos(self):
        """Marca todos os checkboxes."""
        for var in self.check_vars.values():
            var.set(True)

    def desmarcar_todos(self):
        """Desmarca todos os checkboxes."""
        for var in self.check_vars.values():
            var.set(False)

    def realizar(self):
        """Executa a ação com as funções selecionadas."""
        funcoes_selecionadas = [
            nome for nome, var in self.check_vars.items() if var.get()
        ]
        if funcoes_selecionadas:
            messagebox.showinfo("Funções Selecionadas", f"Você selecionou: {', '.join(funcoes_selecionadas)}")
        else:
            messagebox.showwarning("Nenhuma Função", "Nenhuma função foi selecionada.")

    def iniciar(self):
        """Inicia o loop da janela."""
        self.janela.mainloop()

# Executar a interface
if __name__ == "__main__":
    interface = InterfacePython()
    interface.iniciar()


''''              
import csv

caminho_arquivo = "C:/Users/INTEL/Desktop/Universidad pues mol/PG II/Projeto/dados.csv"


with open(caminho_arquivo, mode='r', encoding='latin-1') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')
        
        numero_colunas = 0
        # Obter os nomes das colunas (primeira linha do arquivo)
        nomes_colunas = next(leitor_csv)
        
        # Contar o número de linhas
        numero_linhas = sum(1 for _ in leitor_csv)
        
    # Relatório
print(f"Número total de linhas: {numero_linhas}")
print("Nomes das colunas:")
for coluna in nomes_colunas:
        print(f"- {coluna}")
        numero_colunas += 1
print(f"Numero de colunas: {numero_colunas}")
'''
    
''''
arquivo = open("dados","w")
for linha in range(1,101):
    arquivo.write(f"{linha}\n")
arquivo.close    
'''
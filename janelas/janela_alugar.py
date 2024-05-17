import customtkinter as ctk
from janelas.cadastro_cliente import CadastroCliente
class AlugarVeiculo(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Alugar Veículo")
        self.geometry('900x600')
        self.resizable(False, False)

        self.frameTitulo = ctk.CTkFrame(self, width=800, height=100, corner_radius=0)
        self.frameTitulo.pack(fill= 'both', expand=False)
        self.frameTitulo.pack_propagate(False)

        self.frameItens = ctk.CTkFrame(self, width=800, height=600, corner_radius=0)
        self.frameItens.pack(fill='both', expand= False)
        self.frameItens.pack_propagate(False)

        self.labelTitulo = ctk.CTkLabel(self.frameTitulo, text='Alugar Veículo', font=('Open Sans', 26, 'bold'))
        self.labelTitulo.pack(side='bottom')  

        self.labelPlaca = ctk.CTkLabel(self.frameItens, text='Placa:', font=('Open Sans', 16, 'bold'))
        self.labelPlaca.grid(row=0, column=0, padx= 10, pady=(100, 10), sticky='w')
        self.comboPlaca = ctk.CTkComboBox(self.frameItens, font=('Open Sans', 16))
        self.comboPlaca.grid(row=0, column=1, padx=10, pady=(100, 10), sticky='w')
        
        
        self.labelModelo = ctk.CTkLabel(self.frameItens, text='Modelo:', font=('Open Sans', 16, 'bold'))
        self.labelModelo.grid(row=1, column=0, padx= 10, pady=10, sticky='w')
        self.entryModelo = ctk.CTkEntry(self.frameItens, font= ('Open Sans', 16), width=300, state='disabled')
        self.entryModelo.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.labelAno = ctk.CTkLabel(self.frameItens, text= 'Ano:', font=('Open Sans', 16, 'bold'))
        self.labelAno.grid(row=1, column=2, padx= 10, pady=10, sticky='w')
        self.entryAno = ctk.CTkEntry(self.frameItens, font= ('Open Sans', 16), width=300, state='disabled')
        self.entryAno.grid(row=1, column=3, padx=10, pady=10, sticky='w')

        self.labelCliente = ctk.CTkLabel(self.frameItens, text='Cliente', font=('Open Sans', 16, 'bold'))
        self.labelCliente.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.comboCliente = ctk.CTkComboBox(self.frameItens, font=('Open Sans', 16), width=300)
        self.comboCliente.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        self.botãoCadCliente = ctk.CTkButton(self.frameItens, text='Cadastro Cliente', font=('open Sans', 16, 'bold'), command=self.cadastrar_cliente)
        self.botãoCadCliente.grid(row=2, column=3, padx=10, pady=10, sticky='ew')

        self.labelDataInicio = ctk.CTkLabel(self.frameItens, text= 'Data inicio:', font=('Open Sans', 16, 'bold'))
        self.labelDataInicio.grid(row=3, column=0, padx= 10, pady=10, sticky='w')
        self.entryDataInicio = ctk.CTkEntry(self.frameItens, font= ('Open Sans', 16), placeholder_text='dd/mm/aaaa')
        self.entryDataInicio.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        self.labelDataFim = ctk.CTkLabel(self.frameItens, text= 'Data Fim:', font=('Open Sans', 16, 'bold'))
        self.labelDataFim.grid(row=3, column=2, padx= 10, pady=10, sticky='w')
        self.entryDataFim = ctk.CTkEntry(self.frameItens, font= ('Open Sans', 16), placeholder_text= 'dd/mm/aaaa')
        self.entryDataFim.grid(row=3, column=3, padx=10, pady=10, sticky='w')

        self.botãoAlugar = ctk.CTkButton(self.frameItens, text='Alugar', font=('Open Sans', 16, 'bold'))
        self.botãoAlugar.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

    def cadastrar_cliente(self):
        janela_cadastro = CadastroCliente(self)
        janela_cadastro.grab_set()

from tkinter import messagebox

class DesbastePCmds:

    txt = 'Escolha um nome de pasta para salvar o seu ciclo/projeto:'

    def __init__(self, master):
        self.__master = master

    # Método responsável por fazer a chamada da tela de parâmetros de corte
    def call_parameters(self):
        try:
            from src.view.parameters import Parameters

            self.__parameters = Parameters()
            self.__parameters.mainloop()

        except Exception as e:
            print(f'Erro na chamada da tela de parâmetros de corte:\n\n{e}')

    # Método responsável por gerar o g-code
    def up_gcode(self):
        try:
            from src.model.assents import Assents
            from src.model.cy_desbastep import CyDesbasteP

            self.__assents = Assents(self.__master)

            self._dii = float(self.__master.entry_dii.get()) # Conversão do campo de entry - diâmetro inicial
            self._dif = float(self.__master.entry_dif.get()) # Conversão do campo de entry - diâmetro final
            self._esp = float(self.__master.entry_esp.get()) # Conversão do campo de entry - espessura

            self._ip = self.__assents.criar_inputdialog('Compilador G-Code', DesbastePCmds.txt)

            self.__desbastep = CyDesbasteP(self._dii, self._dif, self._esp)

            self.__desbastep.rotacao(100.0)

            self.__desbastep.initialize_files()
            self.__desbastep.generate_gcode(self._ip.get_input())

        except Exception as e:
            messagebox.showerror('Compilador G-Code', 'Erro na geração do g-code, revise os campos e tente novamente!')
            print(f'Erro na geração do g-code final:\n\n{e}')
        
        else:
            messagebox.showinfo('Compilador G-Code', f'Ciclo de desbaste parametrizado gerado com sucesso e salvo nos seus arquivos.')
            print(' - Ciclo de desbaste parametrizado gerado com sucesso e salvo nos seus arquivos.')
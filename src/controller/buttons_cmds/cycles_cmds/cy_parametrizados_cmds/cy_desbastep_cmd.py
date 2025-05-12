class DesbastePCmds:

    def __init__(self):
        pass

    # Método responsável por fazer a chamada da tela de parâmetros de corte
    def call_parameters(self):
        try:
            from src.view.parameters import Parameters

            self.__parameters = Parameters()
            self.__parameters.mainloop()

        except Exception as e:
            print(f'Erro na chamada da tela de parâmetros de corte:\n\n{e}')
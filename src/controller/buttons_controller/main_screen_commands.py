from src.view.view_cycles.main_cycles import MainCycles

class MainScreenCommands:

    def __init__(self):
        pass

    def call_maincycles(self):

        self.main_cycles = MainCycles()
        self.main_cycles.mainloop()
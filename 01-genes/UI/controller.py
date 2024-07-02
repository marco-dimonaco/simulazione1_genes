import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._selected_gene = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        grafo = self._model.buildGraph()
        if grafo:
            self._view.txt_result.controls.append(ft.Text(self._model.printGraphDetails()))
            self.fillDDGenes()
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text("Errore nella creazione del grafo!", color='red'))
            self._view.update_page()
            return

    def handle_geni_adiacenti(self, e):
        origine = self._selected_gene
        if origine is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona un gene!"))
            self._view.update_page()
            return
        else:
            vicini_ordinati = self._model.getAdiacentiOrdinati(origine)
            self._view.txt_result.controls.append(ft.Text(f"Geni adiacenti a: {self._selected_gene.GeneID}"))
            for k, v in vicini_ordinati.items():
                self._view.txt_result.controls.append(ft.Text(f"{k} {v}"))
            self._view.update_page()

    def handle_simulazione(self, e):
        pass

    def fillDDGenes(self):
        allNodes = self._model.getNodes()
        for n in allNodes:
            self._view.ddGenes.options.append(ft.dropdown.Option(text=n.GeneID, data=n, on_click=self.readDDGenes))
        self._view.update_page()

    def readDDGenes(self, e):
        if e.control.data is None:
            self._selected_gene = None
        else:
            self._selected_gene = e.control.data

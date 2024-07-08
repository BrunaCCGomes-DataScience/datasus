class DBCProcessor:
    def __init__(self, dataframes):
        self.dataframes = dataframes
        

    def process(self):
        processed_data = []
        for df in self.dataframes:
            # Implementar o processamento específico dos dados aqui
            # Por exemplo, limpar, transformar, filtrar, etc.
            processed_data.append(df)
        return processed_data

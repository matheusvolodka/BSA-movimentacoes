
from extraction import Extraction
from transform import Transform

def main():
    # Etapa 1 - Extração
    extractor = Extraction()
    json_path = extractor.run()  # Aqui ele retorna o caminho do JSON salvo
    # Etapa 2 - Transformação
    transformer = Transform(json_path)
    transformer.run()

if __name__ == '__main__':
    main()

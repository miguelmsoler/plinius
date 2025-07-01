# src/plinius/main.py

import argparse
from plinius.core.directory_listener import DirectoryLister

def main():
    parser = argparse.ArgumentParser(description='Plinius: Herramienta de Documentación de Código')
    parser.add_argument('source', type=str, help='Ruta al directorio fuente para documentar')
    parser.add_argument('-o', '--output', type=str, help='Ruta al directorio de salida para la documentación generada', required=False)

    args = parser.parse_args()

    directory_lister = DirectoryLister(args.source)
    directory_lister.document_directory(args.source)

if __name__ == "__main__":
    main()

from sys import argv, exit

from core import Printer


def main():
    """
    Função principal do script. Imprime o conteúdo de uma URL como pdf.

    Utiliza dois argumentos da linha de comando:
    - Argv[1]: URL a ser impressa.
    - Argv[2]: Destino da impressão.
    """
    printer = Printer()
    try:
        printer.Print_url(rf"{argv[1]}", rf"{argv[2]}")
    except Exception as e:
        exit(e)

if __name__ == "__main__":
    main()
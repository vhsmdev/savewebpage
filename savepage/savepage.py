import argparse
from core import save_page


if __name__ == "__main__":
    # Configurar argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Capture full page screenshot of a given URL and convert to PDF or PNG")
    parser.add_argument("url", type=str, help="URL of the webpage to capture")
    parser.add_argument("output_format", type=str, choices=['pdf', 'png'], help="Output format (pdf or png)")
    parser.add_argument("--output", "-o", type=str, default="full_page_screenshot", help="Output base path (without extension)")

    # Parse os argumentos da linha de comando
    args = parser.parse_args()

    # Capturar a captura de tela da página da web e converter para o formato especificado
    save_page(args.url, args.output, args.output_format)
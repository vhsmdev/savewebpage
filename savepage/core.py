from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from webdriver_manager.chrome import ChromeDriverManager


def save_page(url, output_path, output_format):
    # Configurar as opções do Chrome para capturar a captura de tela
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')  # Executar o navegador em modo headless (sem janela visível)
    chrome_options.add_argument("--log-level=3") # Remover mensagens de baixo nivel do Chrome

    chrome_service = ChromeService(ChromeDriverManager().install())

    try:
        # Iniciar o driver do Chrome
        with webdriver.Chrome(service=chrome_service, options=chrome_options) as driver:
            # Carregar a página da web
            driver.get(url)
            
            # Esperar até que a página esteja totalmente carregada
            driver.implicitly_wait(10)  # Espera implícita por até 10 segundos

            # Obter a altura total da página
            total_height = driver.execute_script("return document.body.scrollHeight")

            # Rolar até o final da página
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Rolar de volta para o topo da página
            driver.execute_script("window.scrollTo(0, 0);")

            # Definir a altura da janela de visualização como a altura total da página para capturar toda a página
            driver.set_window_size(1200, total_height)  # Ajuste conforme necessário

            # Capturar uma captura de tela da página
            screenshot = driver.get_screenshot_as_png()
            img = Image.open(BytesIO(screenshot))

            if output_format == 'pdf':
                # Converter a captura de tela para PDF
                convert_to_pdf(img, f"{output_path}.pdf")
                print(f"Captura de tela convertida para PDF: {output_path}.pdf")
            elif output_format == 'png':
                # Salvar a captura de tela como PNG
                img.save(f"{output_path}.png")
                print(f"Captura de tela da página inteira salva como: {output_path}.png")

    except Exception as e:
        print(f"Erro ao capturar a captura de tela da página inteira: {e}")


def convert_to_pdf(image, output_path):
    # Criar um documento PDF usando reportlab
    c = canvas.Canvas(output_path, pagesize=(image.width, image.height))
    c.drawInlineImage(image, 0, 0, width=image.width, height=image.height)
    c.save()


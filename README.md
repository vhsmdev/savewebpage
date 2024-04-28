### Captura de Tela de Página Inteira e Conversor para PDF

Este script em Python efetua uma captura de tela em uma página inteira de uma URL fornecida usando o Selenium WebDriver e, opcionalmente, converte a captura de tela para PDF ou PNG.

#### Dependências

- Python 3.x
- Selenium
- Pillow (PIL)
- ReportLab
- WebDriver Manager

Use o comando `git clone` seguido da URL do repositório para clonar o código-fonte para sua máquina local.

```bash
git clone https://github.com/vhsmdev/savewebpage.git
```

Instale as dependências usando pip:

```bash
pip install selenium Pillow reportlab webdriver_manager
```

#### Uso

Execute o script a partir da linha de comando com os seguintes argumentos:

```bash
python savepage.py <url> <output_formato> [--output <caminho_saida>]
```

- `<url>`: URL da página da web que será capturada.
- `<output_formato>`: Formato de saída para a captura de tela (`pdf` ou `png`).
- `--output <caminho_saida>` (opcional): Caminho base para o arquivo de saída (sem extensão). Padrão: `full_page_screenshot`.

#### Exemplos de Uso

Capturar uma captura de tela de página inteira de `https://example.com` e salvar como PDF:

```bash
python savepage.py https://example.com pdf
```

Capturar uma captura de tela de página inteira de `https://example.com` e salvar como PNG:

```bash
python savepage.py https://example.com png
```

Especificar um caminho de saída personalizado (sem extensão):

```bash
python savepage.py https://example.com pdf --output minha_captura
```

#### Detalhes do Script

- O script utiliza o Selenium WebDriver para controlar um navegador Chrome sem interface gráfica (headless) e capturar a captura de tela de página inteira.
- Ele rola até o final da página para garantir que todo o conteúdo seja carregado antes de capturar a tela.
- A captura de tela é salva como PDF ou PNG, dependendo do formato de saída especificado.
- Para a conversão para PDF, a biblioteca `reportlab` é utilizada para criar um documento PDF e incorporar a imagem capturada.

#### Observações

- Certifique-se de que o navegador Chrome está instalado no seu sistema.
- O script requer uma conexão com a internet para baixar o WebDriver necessário.
- Ajuste o tamanho da janela (`driver.set_window_size()`) de acordo com suas necessidades para capturar toda a página.

Agradeço suas contribuições para melhorar este projeto e ficamos ansiosos para revisar suas propostas de melhoria!

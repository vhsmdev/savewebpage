### Salvar pagina de Web

Este script em Python efetua uma captura de tela em uma página inteira de uma URL fornecida usando as funções proprias dos navegadores que possuem chromium, versão disponibiliza apenas formato PDF.

#### Dependências
- python 3+

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
python savepage.py <url> <nome_do_arquivo>
```

- `<url>`: URL da página da web que será capturada, não se esqueça de usar "https:\\".
- `<nome_do_arquivo>`: nome que será atribuido ao arquivo, não inserir a extensão.

#### Exemplos de Uso

Capturar uma captura de tela de página inteira de `https://example.com` e salvar como PDF:

```bash
python savepage.py https://example.com my_exemple_page
```

#### Detalhes do Script

- O script utiliza parâmetros padrões de navegadores chromium, não necessitando estar vinculado somente ao navegador chrome ou depender do selenium.
- Renderização instantânea por parte do navegador, sem necessitade de tempo de espera.
- A captura de tela é salva como PDF, formato PNG não foi implementado nessa versão.
- O gerador de pdf é recurso do navegador e não pode ser configurado, exceto pela utilização de parâmetros do navegador, pelo python.

#### Observações

- O software não foi testado nos navegadores Edge e Opera.
- O script não requer conexão com a internet, apenas o caminho correto da pagina HTML.

## Contribuição ✨

Ajude a comunidade tornando este projeto ainda mais incrível. Leia como contribuir clicando **[aqui](https://github.com/vhsmdev/savewebpage/blob/main/CONTRIBUTING.md)**. Estou convencido de que juntos alcançaremos coisas incríveis!

### Membros da comunidade que já contribuiram:
<a href="https://github.com/vhsmdev/savewebpage/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vhsmdev/savewebpage"/>
</a>

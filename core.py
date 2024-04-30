from os import getcwd, sep
from os import system as cli
from platform import system
from subprocess import check_output


class DefaultSystem:
    """
    Classe base para determinar configurações padrão do sistema.

    Obtém o sistema operacional atual e fornece métodos para acessar
    configurações específicas do sistema, como o navegador padrão.
    """

    def __init__(self):
        self.system = system()

    def get_default_browser(self):
        """
        Obtém o navegador padrão do sistema.

        Retorna:
            str: O nome do navegador padrão.
        """
        if self.system == 'Windows':
            _cli = ['powershell',
                    r'(Get-ItemProperty "HKCU:\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice").ProgId',
                    ]
        elif self.system == 'Darwin':
            _cli = ...  # Comando para macOS (ainda precisa ser implementado)
        elif self.system == 'Linux':
            _cli = ...  # Comando para Linux (ainda precisa ser implementado)

        return check_output(_cli).decode().strip()


class Browser(DefaultSystem):
    """
    Classe para obter informações específicas do navegador.

    Herda de DefaultSystem para acessar as configurações padrão do sistema.
    """

    def __init__(self):
        super().__init__()

    def get_local_path(self):
        """
        Obtém o diretório atual.

        Retorna:
            str: O caminho para o diretório atual.
        """
        return getcwd()


class Printer:
    """
    Classe para imprimir uma URL.

    Utiliza o navegador padrão do sistema para renderizar a URL e imprimir em PDF.
    """

    def __init__(self):
        self.browser = Browser()
        self.browser_name = self.browser.get_default_browser().lower()

    def Print_url(self, url, filename):
        """
        Imprime uma URL para um arquivo PDF.

        Args:
            url (str): A URL a ser impressa.
            filename (str): O nome do arquivo PDF de saída.
        """
        _cli = self.instant_render(url, filename)
        _cli = " ".join(_cli)
        cli(f"start {_cli}")

    def instant_render(self, url, filename):
        """
        Prepara os parâmetros para renderizar a URL para PDF.

        Args:
            url (str): A URL a ser impressa.
            filename (str): O nome do arquivo PDF de saída.

        Returns:
            list: Lista de argumentos para a linha de comando.
        """
        return [self.choose_browser(),
                "--headless",
                "--disable-gpu",
                f"--print-to-pdf={self.browser.get_local_path()+sep+filename}.pdf",
                url,
                ]

    def choose_browser(self):
        """
        Escolhe o navegador a ser utilizado para renderizar a URL.

        Retorna:
            str: O nome do navegador escolhido.
        """
        for browser in ["brave", "chrome", "firefox"]:
            if browser in self.browser_name:
                return browser
        return ""
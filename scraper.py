import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Inicializar colorama para funcionar bem no Windows
init(autoreset=True)

def buscar_concursos_por_estado(estado):
    url = f'https://www.pciconcursos.com.br/concursos/norte/#{estado}'
    print(f'{Fore.BLUE}🌐 URL gerada: {Fore.RESET}{url}')
    
    # Requisição HTTP para o site
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f'{Fore.GREEN}📊 Status da resposta: {response.status_code}\n')
        
        # Parsear o HTML com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar os concursos - ajuste conforme a estrutura do site
        concursos = soup.find_all('div', class_='na')
        
        # Exibir as informações dos concursos encontrados
        if concursos:
            for concurso in concursos:
                nome_concurso = concurso.find('a').text.strip()
                detalhes_concurso = concurso.find('div', class_='ca').text.strip()

                print(f"{Fore.CYAN}🗂️ Nome do concurso: {Fore.YELLOW}{nome_concurso}")
                print(f"{Fore.GREEN}📄 Detalhes: {Fore.RESET}{detalhes_concurso}")
                print(f"{Fore.MAGENTA}{'-'*40}\n")
        else:
            print(f"{Fore.RED}⚠️ Nenhum concurso encontrado para o estado {estado}.")
    else:
        print(f'{Fore.RED}❌ Erro ao acessar a URL: {response.status_code}')

# Solicitar o estado e buscar concursos
if __name__ == "__main__":
    estado = input(f'{Fore.LIGHTWHITE_EX}Digite a sigla do estado (ex: PA, SP, RN): ').strip().upper()
    print(f'\n{Fore.LIGHTCYAN_EX}🔍 Buscando concursos abertos para {estado}...\n')
    buscar_concursos_por_estado(estado)

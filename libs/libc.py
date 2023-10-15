# Generator which generates a single header version of libc
import pathlib, hashlib

libc = pathlib.Path("romfs/musl/include")

out = ""
for item in libc.iterdir():
    if not item.is_dir() and not ".in" in str(item):
        item = str(item)
        if any([(x in item) for x in ["libc", "complex", "dirent", "fcntl", "ifaddrs", "link", "netdb", "poll", "pty", "resolv", "semaphore", "tgmath", "wait", "crt_arch", "ksigaction"]]): 
            continue
        out += "#include <" + item.replace("romfs/musl/include/", "") + ">\n"

guard = "__" + hashlib.md5(out.encode('utf8')).hexdigest() + "_MUSL_LIB_C__"

with open("romfs/musl/include/libc", "w") as libc:
    libc.write(f"#ifndef {guard}\n#define {guard}\n\n{out}\n#endif //{guard}")
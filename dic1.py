# 在字典每一行插入新内容
#靶场：https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block
with open("aa.txt", "w", encoding="utf-8") as f1:
    with open("pass1.txt", "r+", encoding="utf-8") as f:
        data = f.readlines()
    for line in data:
        lis = line.strip()+"\n"+"peter\n"
        f1.writelines(lis)

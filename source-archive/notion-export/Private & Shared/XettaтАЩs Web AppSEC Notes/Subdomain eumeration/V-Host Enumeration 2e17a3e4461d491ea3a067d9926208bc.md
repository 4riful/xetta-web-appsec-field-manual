# V-Host Enumeration

> Thapa Recon
> 

[https://docs.google.com/presentation/d/1k8A_sjJpMUsVdLY5cmtHxkbikn-WvOzD/edit#slide=id.p1](https://docs.google.com/presentation/d/1k8A_sjJpMUsVdLY5cmtHxkbikn-WvOzD/edit#slide=id.p1) 

> Youtube
> 

[ffuf scripts and tricks [NahamCon 2021]](https://www.youtube.com/watch?v=uwcRBSUl8e4)

> Oneliner
> 

```rust
1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

2. ffuf -c -u http://bolt.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.bolt.htb" -fl 505

3. gobuster vhost -u http://horizontall.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 200

http://ffuf.me/sub/vhost
```

> With Nmap
> 

```jsx
nmap --script http-vhosts -p 80,8080,443 target
```

> With FFUF
> 

```jsx
#figure out response length of false positive

curl -s -H "Host: nonexistent.ffuf.io.fi" http://ffuf.io.fi | wc -c

# result is 612

# then filter out responses of len 612

ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs 612

:)
```

> Vhosts in ssl certificate
> 

```
echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -i dns
```
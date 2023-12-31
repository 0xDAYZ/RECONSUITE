# RECONSUITE

A Linux CLI application with a suite of tools which can be used to perform reconnaissance for threat intelligence.

![Home](https://user-images.githubusercontent.com/109734299/236384182-15b2d1e1-6cf0-421a-8d1d-2d5a2a335d5b.png)

<hr />

![Network](https://user-images.githubusercontent.com/109734299/236384183-80e62f41-b872-4959-8117-7b0fb4520fbc.png)

<h3><strong>Network Attacks:</strong></h3>
<ol>
<li>Change MAC Address</li>
<li>Scan Network for clients</li>
<li>ARP Spoofing</li>
<li>DNS Spoofing</li>
<li>Packet Sniffing</li>
<li>Port Scanning</li>
</ol>

<hr />

![Web](https://user-images.githubusercontent.com/109734299/236384179-c8026db9-a53d-4587-98b8-bfaf538298f3.png)

<h3><strong>Web Application Attacks:</strong></h3>
<ol>
<li>Guess login information of a website (Dictionary Attack)</li>
<li>Crawl website for hidden subdomains</li>
<li>Crawl website for hidden subdirectories</li>
<li>Crawl website for href links</li>
</ol>

<hr />

<h3>Pre-requisites:</h3>
1. Python v3.10+ and Python 2
<br />
2. PIP packages: pyfiglet, colorama, scapy, datetime, requests, netfilterqueue and prettytable
<br />
3. Debian-based Linux OS, preferably Kali Linux
<br />
<h4>OR</h4>
Run the dockerfile to create your own image. Alternatively, you can download it from DockerHub.
<br />
Run: <strong>docker pull zer0dayz/reconsuite</strong>


# cent-nuclei-templates
### A curated compilation of custom nuclei templates.
---
## 🚀 Getting Started
---
### 1. Clone the Repository

```sh
git clone https://github.com/akshayrajs/cent-nuclei-templates.git
cd cent-nuclei-templates
```

### 2. Run Nuclei with Custom Templates

```sh
nuclei -t ~/cent-nuclei-templates/templates/ -u https://example.com
```

You can also target multiple URLs:

```sh
cat urls.txt | nuclei -t ~/cent-nuclei-templates/templates/
```

## 🛠️ Installation
---
### Make sure you have Nuclei installed:

```sh
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```
---
## 📌 Usage Examples
---
### Scan a single target

```sh
nuclei -t templates/ -u https://target.com
```

### Scan multiple targets
```
cat urls.txt | nuclei -t /templates

```
---
## Credits
---
- [hakluke](https://twitter.com/hakluke)
- [Nuclei](https://twitter.com/pdnuclei)
- [Project Discovery](https://twitter.com/pdiscoveryio)
- [sec715](https://twitter.com/sec715)
- [geeknik](https://twitter.com/geeknik)
- [SYSTEM00 SECURITY](https://github.com/System00-Security)
- [clarkvoss](https://github.com/clarkvoss)
- [notnotnotveg](https://github.com/notnotnotveg)
- [Alra3ees - Emad Shanab](https://twitter.com/Alra3ees)
- [Nuclei-Templates-Collection](https://github.com/emadshanab/Nuclei-Templates-Collection)
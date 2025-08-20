
# cent-nuclei-templates
### A curated compilation of custom nuclei templates.

## 🚀 Getting Started
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
### Make sure you have Nuclei installed:

```sh
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

## 📌 Usage Examples

### Scan a single target

```sh
nuclei -t templates/ -u https://target.com
```

### Scan multiple targets
```sh
cat urls.txt | nuclei -t /templates
```

### ZSH Killed Issue (Memory Leak)
```sh
cat urls.txt | nuclei -t ~/cent-nuclei-templates/templates/ -ss host-spray -c 20 -bs 20 -rl 50 -rsr 1048576
```
Explanation:

**-ss host-spray**: Scans all templates against one target before moving on.

**-c 20**: Lower concurrency to reduce CPU and memory usage.

**-bs 20**: Lower bulk size to limit the number of targets processed in parallel.

**-rl 50**: Reduces the rate limit to prevent network saturation.

**-rsr 1048576**: Limits response size read to 1 MB.

## Credits

- [Cent](https://github.com/xm1k3/cent)
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

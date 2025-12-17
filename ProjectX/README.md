# ProjectX — Private Nuclei Templates

> **Disclaimer:** ProjectX is a collection of custom Nuclei templates created by [@melbadry9](https://github.com/melbadry9), [@osamahamad](https://github.com/osamahamad), and [@xElkomy](https://github.com/xElkomy). It is shared publicly for educational and ethical security testing purposes only.

---

## Overview

**ProjectX** is a repository of advanced and private **Nuclei templates** designed to detect vulnerabilities, misconfigurations, and exposures across various platforms and technologies.

All templates are fully compatible with [Nuclei](https://github.com/projectdiscovery/nuclei) and are categorized for ease of use and scalability.

---

## Authors

Developed and maintained by:

* **[@melbadry9](https://github.com/melbadry9)**
* **[@osamahamad](https://github.com/osamahamad)**
* **[@xElkomy](https://github.com/xElkomy)**

Special thanks to the [ProjectDiscovery](https://github.com/projectdiscovery) team for their outstanding open-source tools and contributions to the security community.

---

## Repository Structure

| Category         | Description                                                                           |
| ---------------- | ------------------------------------------------------------------------------------- |
| **`cves/`**      | Exploits and detections for known CVEs.                                               |
| **`detection/`** | Software and behavior detection templates (e.g., Sentry, OpenAM, malware indicators). |
| **`files/`**     | Templates to identify exposed configuration or recovery files.                        |
| **`fuzz/`**      | Fuzzing templates including CRLF and open redirect checks.                            |
| **`headless/`**  | Headless browser-based XSS and Swagger-related detections.                            |
| **`ssrf/`**      | SSRF (Server-Side Request Forgery) related vulnerability detections.                  |
| **`takeover/`**  | DNS and HTTP service takeover detections for various providers.                       |
| **`vuls/`**      | General vulnerabilities and misconfigurations (SQLi, debug pages, cache issues).      |
| **`xss/`**       | XSS-related templates (reflected, DOM-based, prototype pollution).                    |

> Each folder represents a distinct category of vulnerability or detection logic designed to improve scan coverage and accuracy.

---

## Responsible Use

ProjectX is intended **for ethical and authorized testing only**. The maintainers are **not responsible for misuse** or any damage caused by unauthorized scanning.

**Always ensure you have explicit permission** before testing any target.

---

**⭐ If you find ProjectX useful, consider starring the repository to support future updates!**
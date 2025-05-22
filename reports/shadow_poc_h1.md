# ShadowFox Vulnerability Report — Proof of Concept (PoC)

**Target(s):**
- https://kayak.ai
- https://www.momondo.com
- https://www.checkfelix.com
- https://www.swoodoo.com
- https://www.hotelscombined.com

---

## Identified Vulnerabilities

### 1. Reflected XSS
```html
<form><input name='note' value='<img src=x onerror=alert("xss")>'></form>

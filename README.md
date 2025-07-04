# BIP39 → BIP44 Ethereum Key Derivation (MetaMask Compatible)

This minimal project demonstrates end-to-end generation of an Ethereum keypair and address from 128 bits of entropy using the BIP-39 and BIP-44 standards — compatible with MetaMask, Ledger, Trezor, and other HD wallets.

---

## What it does

- Generates 128-bit entropy
- Converts it into a 12-word BIP-39 mnemonic
- Derives a 512-bit seed using PBKDF2-HMAC-SHA512 (per BIP-39)
- Applies BIP-44 path `m/44'/60'/0'/0/0` (Ethereum)
- Outputs:
  - Private key (hex)
  - Public key (compressed hex)
  - Ethereum address (EIP-55)

---

## 🚀 Quick Start

```bash
pip install bip-utils
python3 scripts/e2e.py
```
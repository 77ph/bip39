from bip_utils import Bip39EntropyGenerator, Bip39MnemonicGenerator, Bip39SeedGenerator
from bip_utils import Bip44, Bip44Coins, Bip44Changes

# Step 1: Generate 128-bit entropy
entropy_bytes = Bip39EntropyGenerator(128).Generate()

# Step 2: Generate mnemonic from entropy
mnemonic = Bip39MnemonicGenerator().FromEntropy(entropy_bytes)

# Step 3: Derive seed from mnemonic (no passphrase)
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Step 4: Create BIP44 master key for Ethereum
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)

# Step 5: Derive path m/44'/60'/0'/0/0
bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)
bip44_addr_ctx = bip44_chg_ctx.AddressIndex(0)

# Output results
print("Mnemonic (12 words):", mnemonic)
print("Path m/44'/60'/0'/0/0 private Key:", bip44_addr_ctx.PrivateKey().Raw().ToHex())
print("Path m/44'/60'/0'/0/0 public Key (compressed):", bip44_addr_ctx.PublicKey().RawCompressed().ToHex())
print("Path m/44'/60'/0'/0/0 ethereum Address:", bip44_addr_ctx.PublicKey().ToAddress())


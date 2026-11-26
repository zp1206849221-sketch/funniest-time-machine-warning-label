import os

LABEL = "WARNING: Tampering with your grandfather voids the warranty, your birth certificate, and you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)

if __name__ == "__main__":
    main()

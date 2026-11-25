import os

LINE = "You opened me 14 times after midnight and ate nothing. The yogurt expired two Tuesdays ago; I kept the light on. You're welcome."

def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

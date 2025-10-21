import sys
import xml.etree.ElementTree as ET

def main(path):
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        print(f"[ERROR] XML not well-formed: {e}")
        sys.exit(1)

    root = tree.getroot()
    # Collect rule IDs to ensure uniqueness
    ids = []
    for rule in root.findall("rule"):
        rid = rule.get("id")
        if rid:
            ids.append(rid)
    dupes = {x for x in ids if ids.count(x) > 1}
    if dupes:
        print(f"[ERROR] Duplicate rule IDs: {', '.join(sorted(dupes))}")
        sys.exit(2)

    print("[OK] XML parsed, rule IDs unique.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: validate_rules.py <path-to-xml>")
        sys.exit(1)
    main(sys.argv[1])

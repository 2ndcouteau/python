#!/usr/bin/python3.4
# -*- conding:Utf-8 -*

inventaire = {
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
}


inventaire_inv = [(ez, name) for name, ez in inventaire]
inventaire = [(name, ez) for ez, name in sorted(inventaire_inv, reverse = True)]

print(inventaire)

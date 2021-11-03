"""Constants used in the website."""


import os


AA_TO_FORMULA: dict[str, dict[str, int]] = {
    'A':   {'H': 5, 'C': 3, 'O': 1, 'N': 1},
    'C':   {'H': 5, 'C': 3, 'S': 1, 'O': 1, 'N': 1},
    'D':   {'H': 5, 'C': 4, 'O': 3, 'N': 1},
    'E':   {'H': 7, 'C': 5, 'O': 3, 'N': 1},
    'F':   {'H': 9, 'C': 9, 'O': 1, 'N': 1},
    'G':   {'H': 3, 'C': 2, 'O': 1, 'N': 1},
    'H':   {'H': 7, 'C': 6, 'N': 3, 'O': 1},
    'I':   {'H': 11, 'C': 6, 'O': 1, 'N': 1},
    'J':   {'H': 11, 'C': 6, 'O': 1, 'N': 1},
    'K':   {'H': 12, 'C': 6, 'N': 2, 'O': 1},
    'L':   {'H': 11, 'C': 6, 'O': 1, 'N': 1},
    'M':   {'H': 9, 'C': 5, 'S': 1, 'O': 1, 'N': 1},
    'N':   {'H': 6, 'C': 4, 'O': 2, 'N': 2},
    'P':   {'H': 7, 'C': 5, 'O': 1, 'N': 1},
    'Q':   {'H': 8, 'C': 5, 'O': 2, 'N': 2},
    'R':   {'H': 12, 'C': 6, 'N': 4, 'O': 1},
    'S':   {'H': 5, 'C': 3, 'O': 2, 'N': 1},
    'T':   {'H': 7, 'C': 4, 'O': 2, 'N': 1},
    'V':   {'H': 9, 'C': 5, 'O': 1, 'N': 1},
    'W':   {'C': 11, 'H': 10, 'N': 2, 'O': 1},
    'Y':   {'H': 9, 'C': 9, 'O': 2, 'N': 1},
    'U':   {'H': 5, 'C': 3, 'O': 1, 'N': 1, 'Se' : 1},
    'O':   {'H': 19, 'C': 12, 'O': 2, 'N': 3}
    # 'H-':  {'H': 1},
    # '-OH': {'O': 1, 'H': 1},
}

VALID_AMINO_ACIDS: list[str] = list(AA_TO_FORMULA.keys())
NEW_LINE: str = "\n"

RESULT_CSV_NAME_BEGINNING: str = "result"
RESULT_CSV_PATH_BEGINNING: str = os.path.join("static", "result")
RESULT_CSV_PATH_EXTENSION: str = ".csv"

# CSV Header
AA_SEQUENCE: str = "Amino Acid Sequence"
CARBON: str = "C"
HYDROGEN: str = "H"
OXYGEN: str = "O"
NITROGEN: str = "N"
SULFUR: str = "S"
SELENIUM: str = "Se"
FORMULA: str = "Chemical Formula"

# Limit to retain files
# LENGTH_DAY: int = 86400
# LIMIT_DAYS: int = 0.1
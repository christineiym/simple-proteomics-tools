"""Utilities to convert amino acid sequences to chemical formulas."""


__author__ = "christineiym"


import constants
import csv
from typing import Union
import time
import operator


def read_in_sequences(delimiter: str, input_str: str) -> list[str]:
    """Read in amino acid sequences (separated by the given delimiter) and output a list of valid sequences."""
    split_sequences: list[str]
    if delimiter == "na":
        split_sequences = [input_str]
    else:
        if delimiter == "n":
            delimiter = "\n"
        split_sequences: list[str] = input_str.split(delimiter)
    
    result: list[str] = [sequence for sequence in split_sequences if ((sequence is not None) and (sequence != ""))]

    return result


def sequence_to_atom_totals(sequence: str) -> dict[str, int]:
    """Convert a given amino acid sequence to its atomic composition."""
    atom_totals: dict[str, int] = {}

    for amino_acid in sequence:
        chemical_composition: dict[str, int] = constants.AA_TO_FORMULA[amino_acid]
        for atom in chemical_composition:
            if atom in list(atom_totals.keys()):
                atom_totals[atom] += chemical_composition[atom]
            else:
                atom_totals.update({atom : chemical_composition[atom]})
    
    # Add H- and -OH
    atom_totals.update({'O' : (atom_totals['O'] + 1)})
    atom_totals.update({'H' : (atom_totals['H'] + 2)})

    # Sort alphabetically
    atom_totals = dict(sorted(atom_totals.items(), key=operator.itemgetter(0)))
    
    return atom_totals


def atom_totals_to_str(raw_atom_totals: dict[str, int]) -> dict[str, str]:
    """Format totals as strings."""
    result: dict[str, str] = {}

    for atom in list(raw_atom_totals.keys()):
        result.update({atom : str(raw_atom_totals[atom])})
    
    return result


def atom_totals_to_formula(atom_totals: dict[str, str]) -> str:
    """Use a mapping of atom totals (given in the form of strings) to the appropriate atom to create a formula."""
    formula: str = ""

    for atom in atom_totals:
        formula += atom
        if atom_totals[atom] != "1":
            formula += str(atom_totals[atom])
    
    return formula


def sequences_to_formulas_dict(sequences: list[str]) -> dict[str, str]:
    """Convert a list of amino acid sequences to a dict mapping those sequences to corresponding chemical formulas."""
    result: dict[str, str] = {sequence : atom_totals_to_formula(atom_totals_to_str(sequence_to_atom_totals(sequence))) for sequence in sequences}
    return result


def generate_result_csv(sequences: list[str]) -> str:
    """Generate a detailed result csv from a list of sequences."""
    current_time = time.time()
    csv_path: str = constants.RESULT_CSV_NAME_BEGINNING + str(current_time) + constants.RESULT_CSV_PATH_EXTENSION
    csv_path_with_static: str = constants.RESULT_CSV_PATH_BEGINNING + str(current_time) + constants.RESULT_CSV_PATH_EXTENSION

    with open(csv_path_with_static, "w", newline='', encoding="utf-8") as output_file:
        header: list[str] = [
            constants.AA_SEQUENCE,
            constants.FORMULA,
            constants.CARBON,
            constants.HYDROGEN,
            constants.OXYGEN,
            constants.NITROGEN,
            constants.SULFUR,
            constants.SELENIUM
        ]
        placeholder: list[str] = [""] * len(header)

        writer = csv.DictWriter(output_file, fieldnames=header)
        writer.writeheader()

        for sequence in sequences:
            row: dict[str, str] = dict(zip(header, placeholder))

            row.update({constants.AA_SEQUENCE : sequence})

            atom_totals: dict[str, str] = atom_totals_to_str(sequence_to_atom_totals(sequence))
            row.update(atom_totals)

            formula: str = atom_totals_to_formula(atom_totals)
            row.update({constants.FORMULA : formula})
            writer.writerow(row)
    
    print(csv_path)
    return csv_path
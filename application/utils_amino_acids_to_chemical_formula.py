"""Utilities to convert amino acid sequences to chemical formulas."""


__author__ = "christineiym"


import re
from . import constants


def convert_amino_acids_to_formulas(input_str: str) -> list[str]:
    list_sequences: list[str] = read_in_sequences(input_str)
    list_formulas: list[str] = sequences_to_formulas(list_sequences)
    return list_formulas


def read_in_sequences(input_str: str) -> list[str]:
    """Reads in amino acid sequences (separated by the newline character) and outputs a list of sequences."""
    split_sequences: list[str] = input_str.split("\n")
    # https://stackoverflow.com/questions/34214139/python-keep-only-letters-in-string/34214187
    sequences_to_alpha: list[str] = [str(re.sub('[^a-zA-Z]+', '', sequence)) for sequence in split_sequences]
    result: list[str] = [sequence for sequence in sequences_to_alpha if ((sequence is not None) and (sequence != ""))]

    return result

def sequence_to_formula(sequence: str) -> str:
    """Converts a given amino acid sequence to its chemical formula."""
    atom_totals: dict[str, int] = {}

    for amino_acid in sequence:
        chemical_composition: dict[str, int] = constants.AA_TO_FORMULA[amino_acid]
        for atom in chemical_composition:
            if atom in list(atom_totals.keys()):
                atom_totals[atom] += chemical_composition[atom]
            else:
                atom_totals.update({atom : chemical_composition[atom]})
    
    oxygens_to_remove: int = len(sequence) - 1
    hydrogens_to_remove: int = 2 * oxygens_to_remove

    try:
        atom_totals.update({'O' : (atom_totals['O'] - oxygens_to_remove)})
        atom_totals.update({'H' : (atom_totals['H'] - hydrogens_to_remove)})
    except:
        return constants.NOT_POSSIBLE
    
    formula: str = ""

    for atom in atom_totals:
        formula += atom
        formula += str(atom_totals[atom])
    
    return formula

def sequences_to_formulas(sequences: list[str]) -> list[str]:
    """Converts a list of amino acid sequences to a list of corresponding chemical formulas."""
    result: list[str] = [sequence_to_formula(sequence) for sequence in sequences]
    return result
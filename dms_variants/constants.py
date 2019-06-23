"""
============
constants
============

Defines constants used by package.

"""


import Bio.Alphabet.IUPAC
import Bio.Seq


CBPALETTE = ('#999999', '#E69F00', '#56B4E9', '#009E73',
             '#F0E442', '#0072B2', '#D55E00', '#CC79A7')
"""tuple: Color-blind safe palette.

From http://bconnelly.net/2013/10/creating-colorblind-friendly-figures/
"""

AAS_NO_STOP = tuple(sorted(_aa.upper() for _aa in
                           Bio.Alphabet.IUPAC.IUPACProtein.letters))
"""tuple: Amino-acid one-letter codes alphabetized, doesn't include stop."""

AAS_WITHSTOP = tuple(list(AAS_NO_STOP) + ['*'])
"""tuple: Amino-acid one-letter codes alphabetized plus stop as ``*``."""

NTS = tuple(sorted(_nt.upper() for _nt in
                   Bio.Alphabet.IUPAC.IUPACUnambiguousDNA.letters))
"""tuple: DNA nucleotide one-letter codes, alphabetized."""

CODONS = tuple(f"{_n1}{_n2}{_n3}" for _n1 in NTS for _n2 in NTS for _n3 in NTS)
"""tuple: DNA codons, alphabetized."""

CODON_TO_AA = {_c: str(Bio.Seq.Seq(_c).translate()) for _c in CODONS}
"""dict: Maps codons to amino acids."""

AA_TO_CODONS = {_aa: [_c for _c in CODONS if CODON_TO_AA[_c] == _aa]
                for _aa in AAS_WITHSTOP}
"""dict: Reverse translate amino acid to list of encoding codons."""

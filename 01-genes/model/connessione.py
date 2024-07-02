from model.genes import Gene
from dataclasses import dataclass


@dataclass
class Connessione:
    gene1: Gene
    gene2: Gene
    expr: float

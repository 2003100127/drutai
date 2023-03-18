__author__ = "Jianfeng Sun"
__version__ = "v1.0"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__email__ = "jianfeng.sunmt@gmail.com"
__maintainer__ = "Jianfeng Sun"

import numpy as np
import pandas as pd
from rdkit import Chem
from drutai.Utils import fasta
from drutai import Process


def fetch(
        smile_fpn,
        fasta_fpn,
):
    smile = pd.read_csv(
        smile_fpn,
        sep='\t',
        header=None,
    )
    print(smile)
    mol = Chem.MolFromSmiles(smile.loc[0, 0])
    print(mol)
    v = [[] for _ in range(1)]

    aseq = fasta(fasta_fpn=fasta_fpn)

    cprot_ = Process.cprot(aseq)
    v[0] += list(cprot_.values())

    dprot_ = Process.dprot(aseq)
    for j in range(400):
        v[0].append(np.float32(dprot_[j][1]))

    tprot_ = Process.tprot(aseq)
    for j in range(8000):
        v[0].append(np.float32(tprot_[j][1]))

    ctd_ = Process.pyp(aseq)
    ctd_values = ctd_.values()
    for val in ctd_values:
        v[0].append(np.float32(val))

    pc195 = Process.dsi(mol)
    for _, e in enumerate(pc195):
        v[0].append(np.float32(e))

    pc2 = Process.crippen(mol)
    for _, e in enumerate(pc2):
        v[0].append(np.float32(e))

    fp_morgan = Process.fp1(mol)
    for _, e in enumerate(fp_morgan):
        v[0].append(np.int(e))

    fp_torsion = Process.fp2(mol)
    for _, e in enumerate(fp_torsion):
        v[0].append(np.int(e))
    v = np.array(v)
    return v[:, 0: 11664].astype(np.float32)
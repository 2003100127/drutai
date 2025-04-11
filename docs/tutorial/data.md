# Data

## Drug target pairs

There are 5 drug-target pairs as follows.

| No. | small molecule |   target   |
|:---:|:--------------:|:----------:|
|  1  |     148124     |   C1KC03   |
|  2  |     84093      |   P03901   |
|  3  |      5757      |   Q8N0U8   |
|  4  |      5743      |   O00238   |
|  5  |     84093      | A0A0H2UXE9 |



## Protein targets

:::{note} Fasta
:class: dropdown
Protein sequences in [the Fasta format](https://en.wikipedia.org/wiki/FASTA_format) are required. The file extension must be `.fasta` for recognition of the software.
:::

## Small molecules

Drutai reads the smile strings of small molecules as follows. This needs to be separated by `tab`.

| No. | small molecule |                    smile                     |
|:---:|:--------------:|:--------------------------------------------:|
|  1  |     5743       |            C...(C(=O)CO)O)C)O)F)C            |
|  2  |     84093      | CC1=CN(C(=O)NC1=O)C2CC(C(O2)COP(=O)...[Pt+2] |
|  3  |     148124     |            CC1=C2[...(=O)C)O)C)O             |
|  4  |      5757      |             C[C@]12CC...C(=C4)O              |

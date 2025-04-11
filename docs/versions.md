# Versions

## Change

::::{grid} 2 2 2 2

| Version     |                                  Date                                   |
|:-------------:|:-----------------------------------------------------------------------:|
| `2022-2025` |   ![](https://img.shields.io/badge/past_released-June._2022-red.svg)    |
| `0.0.1`     | ![](https://img.shields.io/badge/latest_released-April._2025-green.svg) |

::::

## Before `0.0.1`

Before the release `0.0.1`, **Drutai** was used to infer a drug-target interaction per instance only. This process is simplified as follows.

### Small molecule 

> Docetaxel (CID: 148124)

```shell
CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@H]3[C@@H]([C@@](C2(C)C)(C[C@@H]1OC(=O)[C@@H]([C@H](C5=CC=CC=C5)NC(=O)OC(C)(C)C)O)O)OC(=O)C6=CC=CC=C6)(CO4)OC(=O)C)O)C)O
```

### Target

> A0A0H2UXE9

```
>A0A0H2UXE9
MDFPQQLEACVKQANQALSRFIAPLPFQNTPVVETMQYGALLGGKRLRPFLVYATGHMFGVSTNTLDAPAAAVECIHAYSLIHDDLPAMDDDDLRRGLPTCHVKFGEANAILAGDALQTLAFSILSDANMPEVSDRDRISMISELASASGIAGMCGGQALDLDAEGKHVPLDALERIHRHKTGALIRAAVRLGALSAGDKGRRALPVLDKYAESIGLAFQVQDDILDVVGDTATLGKRQGADQQLGKSTYPALLGLEQARKKARDLIDDARQALKQLAEQSLDTSALEALADYIIQRNK
```

### Inference

```shell
drutai -m LSTMCNN -d drutai/data/example/148124.txt -t drutai/data/example/A0A0H2UXE9.fasta -mf /the/path/you/prefer/model/lstmcnn -o ./out.drutai
```


## Tensorflow

::::{caution} Major change in deep learing libraries
In Keras 3, the way to call models becomes completely different from that in Keras 2.

:::{table} The way to use models.
:label: tbl1
:align: center

| Item              | TF Keras 2                 | TF Keras 3                       |
|-------------------|----------------------------|----------------------------------|
| model format      | `.h5` or TF `SavedModel`   | `.keras` (new) + `.h5`  (legacy) |
| `subclass` Models | supported via `SavedModel` | `TFSMLayer` for loading          |

:::

::::

### Comparison

Our experience suggests that changes in Python versions have a smaller impact compared to changes in TensorFlow versions.

:::{table} The way to use models.
:label: tbl2
:align: center

| Python  | Tensorflow verisons        | Supported versions     |
|---------|----------------------------|------------------------|
| `3.11`  | 🌟`2.14`🌟, `2.15`, `2.16` | TF Keras 2, TF Keras 3 |
| `3.12`  | `2.17`, `2.18`, `2.19`     | only TF Keras 3        |

:::
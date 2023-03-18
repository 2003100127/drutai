# Drutai
![](https://img.shields.io/badge/drutai-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released-June._2022-green.svg)
![](https://img.shields.io/github/stars/2003100127/drutai?logo=GitHub&color=blue)

###### tags: `protein` `drugs` `interaction`

## Overview
This repository is a standalone package of the Drutai method. Drutai is used to predict interactions between small molecule drugs and protein targets. This program has been made by using 12 leading deep learning frameworks.

## Installation
* ### PyPI
```angular2html
pip install drutai
```

## Overview
```angular2html
drutai [-h]
           --method m
           --smile_fpn d
           --fasta_fpn t
           --model_fp mf
           --output_path o

argument details:
    -h, --help            show this help message and exit
    -m, --method,
            A deep learning method. It can be any below.
            AlexNet | BiRNN | RNN | Seq2Seq |
            CNN | ConvMixer64 | DSConv | LSTMCNN |
            MobileNet | ResNet18 | ResNet50 | SEResNet 


    -d, --smile_fpn, a small molecule drug file that contains only smile strings


    -t, --fasta_fpn, a protein fasta file


    -mf, --model_fp, a model path


    -o, --output_path, outputting drutai predictions
```

## Usage
### Download models
see models https://github.com/2003100127/drutai/releases/tag/model
```shell
drutai_download # this is to download the model in your current folder
```

```
# output messages
downloading...
downloaded!
```
Please use `-mf` of `drutai` then to access to where the models are located.

### Input format
Two example files in Drutai are 148124.txt and A0A0H2UXE9.fasta for a small molecule and a protein molecule.

* #### Docetaxel (small molecule CID: 148124)

![docetaxel](https://github.com/2003100127/drutai/blob/main/img/Docetaxel.png?raw=true)
```shell
# 148124.txt
CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@H]3[C@@H]([C@@](C2(C)C)(C[C@@H]1OC(=O)[C@@H]([C@H](C5=CC=CC=C5)NC(=O)OC(C)(C)C)O)O)OC(=O)C6=CC=CC=C6)(CO4)OC(=O)C)O)C)O
```

* #### A0A0H2UXE9
```
# A0A0H2UXE9.fasta
>A0A0H2UXE9
MDFPQQLEACVKQANQALSRFIAPLPFQNTPVVETMQYGALLGGKRLRPFLVYATGHMFGVSTNTLDAPAAAVECIHAYSLIHDDLPAMDDDDLRRGLPTCHVKFGEANAILAGDALQTLAFSILSDANMPEVSDRDRISMISELASASGIAGMCGGQALDLDAEGKHVPLDALERIHRHKTGALIRAAVRLGALSAGDKGRRALPVLDKYAESIGLAFQVQDDILDVVGDTATLGKRQGADQQLGKSTYPALLGLEQARKKARDLIDDARQALKQLAEQSLDTSALEALADYIIQRNK
```

### Inference
Use two example files in Drutai.
```shell
drutai -m LSTMCNN -d drutai/data/example/148124.txt -t drutai/data/example/A0A0H2UXE9.fasta -mf /the/path/you/prefer/model/lstmcnn -o ./out.drutai
```

## Citation
Please cite our work if you use Drutai in your research.

## Contact
If you have any question, please contact [Jianfeng Sun](jianfeng.sunmt@gmail.com). We highly recommend creating issue pages when you have problems. Your issues will be responded then.


# Prediction

## Overview

You need to decompress the `example data.zip` file in your preferred folder, e.g., `drutai/`.

There are three required files.

* `br_sm_target.txt`
* `br_smile.txt`
* `path` to `*.fasta`

We display 5 relations between small molecules and targets to predict their possible interactions.

```{code}
:linenos:
:emphasize-lines: 2,3,4,5,6

sm	target
148124	C1KC03
84093	P03901
5757	Q8N0U8
5743	O00238
84093	A0A0H2UXE9
```

:::{caution} Model declaration
* For TF `1.15x` models, including `alexnet`, `birnn`, `rnn`, and `seq2seq`, you need to declare them like `alexnet/alexnet`.
* For TF `2.14x` models, including `cnn`, `lstmcnn`, `dsconv`, `convmixer64`, `mobilenet`, `resnet_prea18`, `resnet_prea50`, and `seresnet`, you need to declare them like `lstmcnn`.
:::

## Python

We access **Drutai** by defining the following parameters. 

:::{seealso}
We have `method` defined as **AlexNet**, **BiRNN**, **RNN**, **Seq2Seq**, **CNN**, **ConvMixer64**, **DSConv**, **LSTMCNN**, **MobileNet**, **ResNet18**, **ResNet50**, or **SEResNet**. Please see also [the Drutai paper](https://doi.org/10.1016/j.ejmech.2023.115500) for method details.
:::

```{code} python
params = {
    'br_fpn': '../../data/drutai/example_data/br_sm_target.txt',
    'smile_fpn': '../../data/drutai/example_data/br_smile.txt',
    'method': 'LSTMCNN',
    'fasta_fp': '../../data/drutai/example_data/',
    'model_fp': '../../data/drutai/lstmcnn',
    'sv_fpn': '../../data/drutai/example_data/pred.drutai',
}
```

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} python
import drutai

drutai.predict.sm_target_interaction(
    br_fpn=params['br_fpn'],
    smile_fpn=params['smile_fpn'],
    fasta_fp=params['fasta_fp'],
    method=params['method'],
    model_fp=params['model_fp'],
    sv_fpn=params['sv_fpn'],
)
```
:::
:::{tab-item} Output log
:sync: tab2
```{code} shell
 ____             _        _ 
|  _ \ _ __ _   _| |_ __ _(_)
| | | | '__| | | | __/ _` | |
| |_| | |  | |_| | || (_| | |
|____/|_|   \__,_|\__\__,_|_|
                             

02/04/2025 02:12:30 logger: =>Prediction starts...
02/04/2025 02:12:30 logger: small-molecule and target relations:
       sm      target
0  148124      C1KC03
1   84093      P03901
2    5757      Q8N0U8
3    5743      O00238
4   84093  A0A0H2UXE9
02/04/2025 02:12:30 logger: small-molecule smile map:
       sm                                              smile
0    5743  C[C@@H]1C[C@H]2[C@@H]3CCC4=CC(=O)C=C[C@@]4([C@...
1   84093  CC1=CN(C(=O)NC1=O)C2CC(C(O2)COP(=O)(O)OC3CC(OC...
2  148124  CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@...
3    5757  C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=C3...
[02:12:30] DEPRECATION WARNING: please use MorganGenerator
[02:12:30] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:12:30] DEPRECATION WARNING: please use MorganGenerator
[02:12:30] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:12:30] DEPRECATION WARNING: please use MorganGenerator
[02:12:30] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:12:30] DEPRECATION WARNING: please use MorganGenerator
[02:12:30] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:12:30] DEPRECATION WARNING: please use MorganGenerator
[02:12:30] DEPRECATION WARNING: please use TopologicalTorsionGenerator
     prob_inter        pred_type
0  7.233677e-06  Non-interaction
1  6.156772e-04  Non-interaction
2  6.745233e-08  Non-interaction
3  3.606971e-06  Non-interaction
4  3.974514e-03  Non-interaction
```
:::
::::


## CLI

Drutai can also be used in shell. To know how to use, please type

```{code} shell
drutai -h
```

It shows the usage of different parameters.

```{code} shell
-m, --method,
    A deep learning method. It can be any below.
    AlexNet | BiRNN | RNN | Seq2Seq |
    CNN | ConvMixer64 | DSConv | LSTMCNN |
    MobileNet | ResNet18 | ResNet50 | SEResNet |
-br, --br_fpn, binary relations between small molecules and protein targets
-d, --smile_fpn, map between small molecule IDs and their smile strings
-t, --fasta_fp, protein target fasta file paths
-mf, --model_fp, a model path
-o, --sv_fpn, outputting drutai predictions
```


You can run it using the following code.

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```{code} shell
drutai -m LSTMCNN -br ./data/drutai/example_data/br_sm_target.txt -d ./data/drutai/example_data/br_smile.txt -t ./data/drutai/example_data/ -mf ./data/drutai/lstmcnn -o ./data/drutai/out.drutai
```
:::
:::{tab-item} Output log
:sync: tab2
```{code} shell
 ____             _        _
|  _ \ _ __ _   _| |_ __ _(_)
| | | | '__| | | | __/ _` | |
| |_| | |  | |_| | || (_| | |
|____/|_|   \__,_|\__\__,_|_|


02/04/2025 02:41:27 logger: =>Prediction starts...
02/04/2025 02:41:27 logger: small-molecule and target relations:
       sm      target
0  148124      C1KC03
1   84093      P03901
2    5757      Q8N0U8
3    5743      O00238
4   84093  A0A0H2UXE9
02/04/2025 02:41:27 logger: small-molecule smile map:
       sm                                              smile
0    5743  C[C@@H]1C[C@H]2[C@@H]3CCC4=CC(=O)C=C[C@@]4([C@...
1   84093  CC1=CN(C(=O)NC1=O)C2CC(C(O2)COP(=O)(O)OC3CC(OC...
2  148124  CC1=C2[C@H](C(=O)[C@@]3([C@H](C[C@@H]4[C@]([C@...
3    5757  C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=C3...
[02:41:27] DEPRECATION WARNING: please use MorganGenerator
[02:41:27] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:41:27] DEPRECATION WARNING: please use MorganGenerator
[02:41:27] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:41:27] DEPRECATION WARNING: please use MorganGenerator
[02:41:27] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:41:27] DEPRECATION WARNING: please use MorganGenerator
[02:41:27] DEPRECATION WARNING: please use TopologicalTorsionGenerator
[02:41:28] DEPRECATION WARNING: please use MorganGenerator
[02:41:28] DEPRECATION WARNING: please use TopologicalTorsionGenerator
     prob_inter        pred_type
0  7.233677e-06  Non-interaction
1  6.156772e-04  Non-interaction
2  6.745233e-08  Non-interaction
3  3.606971e-06  Non-interaction
4  3.974514e-03  Non-interaction
```
:::
::::


```{code-cell} python
:tags: [remove-input]
print("This will show output 11111 no input!")
```

```{code} shell
deepsmirud -m LSTMCNN -br ./data/input/br_sm_mirna.txt -d ./data/input/br_smile.txt -t ./data/input/ -mf ./data/model/lstmcnn -o ./data/out.deepsmirud
```
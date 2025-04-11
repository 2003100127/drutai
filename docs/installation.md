# Installation

## Overview

We are striving to make **Drutai** available to use across different versions of Python and Tensorflow. Given conflicts between dependencies, the following versions are recommended most (please see [log 1](./versions#tbl1) and [log 2](./versions#tbl2)).

  * Python `3.11`
  * Tensorflow `2.14`

## Installing

Then, we can follow the step-by-step precedures for installation.

Step 1: Get the most recent version of **Drutai** from GitHub (_clone it at your preferred location_), PyPI, or Conda.

```shell
git clone https://github.com/2003100127/drutai.git
```

Step 2: Create a conda environment in your local machine.

```shell
conda create --name drutai python=3.11

conda activate drutai
```

Step 3: install via pip

::::{tab-set}
:::{tab-item} Command
:sync: tab1
```shell
cd drutai

pip install .
```
:::
:::{tab-item} Installation log
:sync: tab2
```shell
Processing d:\document\programming\python\drutai
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting biopython<2.0,>=1.85 (from drutai==0.0.1)
  Using cached biopython-1.85-cp311-cp311-win_amd64.whl.metadata (13 kB)
Collecting click<9.0.0,>=8.1.8 (from drutai==0.0.1)
  Using cached click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting numpy==1.24.3 (from drutai==0.0.1)
  Using cached numpy-1.24.3-cp311-cp311-win_amd64.whl.metadata (5.6 kB)
Collecting pandas<3.0.0,>=2.2.3 (from drutai==0.0.1)
  Using cached pandas-2.2.3-cp311-cp311-win_amd64.whl.metadata (19 kB)
Collecting pyfiglet<2.0.0,>=1.0.2 (from drutai==0.0.1)
  Using cached pyfiglet-1.0.2-py3-none-any.whl.metadata (7.1 kB)
Collecting rdkit<2025.0.0,>=2024.9.6 (from drutai==0.0.1)
  Using cached rdkit-2024.9.6-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
Collecting tensorflow==2.14 (from drutai==0.0.1)
  Using cached tensorflow-2.14.0-cp311-cp311-win_amd64.whl.metadata (3.3 kB)
Collecting tensorflow-io-gcs-filesystem==0.31.0 (from drutai==0.0.1)
  Using cached tensorflow_io_gcs_filesystem-0.31.0-cp311-cp311-win_amd64.whl.metadata (14 kB)
Collecting tensorflow-intel==2.14.0 (from tensorflow==2.14->drutai==0.0.1)
  Using cached tensorflow_intel-2.14.0-cp311-cp311-win_amd64.whl.metadata (4.8 kB)
Collecting absl-py>=1.0.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached absl_py-2.2.1-py3-none-any.whl.metadata (2.4 kB)
Collecting astunparse>=1.6.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached astunparse-1.6.3-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting flatbuffers>=23.5.26 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached flatbuffers-25.2.10-py2.py3-none-any.whl.metadata (875 bytes)
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached gast-0.6.0-py3-none-any.whl.metadata (1.3 kB)
Collecting google-pasta>=0.1.1 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached google_pasta-0.2.0-py3-none-any.whl.metadata (814 bytes)
Collecting h5py>=2.9.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached h5py-3.13.0-cp311-cp311-win_amd64.whl.metadata (2.5 kB)
Collecting libclang>=13.0.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached libclang-18.1.1-py2.py3-none-win_amd64.whl.metadata (5.3 kB)
Collecting ml-dtypes==0.2.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached ml_dtypes-0.2.0-cp311-cp311-win_amd64.whl.metadata (20 kB)
Collecting opt-einsum>=2.3.2 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting packaging (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
Collecting protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached protobuf-4.25.6-cp310-abi3-win_amd64.whl.metadata (541 bytes)
Requirement already satisfied: setuptools in d:\programming\anaconda3\envs\drutai\lib\site-packages (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1) (75.8.2)
Collecting six>=1.12.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting termcolor>=1.1.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached termcolor-3.0.0-py3-none-any.whl.metadata (6.1 kB)
Collecting typing-extensions>=3.6.6 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached typing_extensions-4.13.0-py3-none-any.whl.metadata (3.0 kB)
Collecting wrapt<1.15,>=1.11.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached wrapt-1.14.1-cp311-cp311-win_amd64.whl.metadata (6.9 kB)
Collecting grpcio<2.0,>=1.24.3 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached grpcio-1.71.0-cp311-cp311-win_amd64.whl.metadata (4.0 kB)
Collecting tensorboard<2.15,>=2.14 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached tensorboard-2.14.1-py3-none-any.whl.metadata (1.7 kB)
Collecting tensorflow-estimator<2.15,>=2.14.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached tensorflow_estimator-2.14.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting keras<2.15,>=2.14.0 (from tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached keras-2.14.0-py3-none-any.whl.metadata (2.4 kB)
Collecting colorama (from click<9.0.0,>=8.1.8->drutai==0.0.1)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting python-dateutil>=2.8.2 (from pandas<3.0.0,>=2.2.3->drutai==0.0.1)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting pytz>=2020.1 (from pandas<3.0.0,>=2.2.3->drutai==0.0.1)
  Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
Collecting tzdata>=2022.7 (from pandas<3.0.0,>=2.2.3->drutai==0.0.1)
  Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting Pillow (from rdkit<2025.0.0,>=2024.9.6->drutai==0.0.1)
  Downloading pillow-11.2.0-cp311-cp311-win_amd64.whl.metadata (9.2 kB)
Requirement already satisfied: wheel<1.0,>=0.23.0 in d:\programming\anaconda3\envs\drutai\lib\site-packages (from astunparse>=1.6.0->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1) (0.45.1)
Collecting google-auth<3,>=1.6.3 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached google_auth-2.38.0-py2.py3-none-any.whl.metadata (4.8 kB)
Collecting google-auth-oauthlib<1.1,>=0.5 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached google_auth_oauthlib-1.0.0-py2.py3-none-any.whl.metadata (2.7 kB)
Collecting markdown>=2.6.8 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached Markdown-3.7-py3-none-any.whl.metadata (7.0 kB)
Collecting requests<3,>=2.21.0 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting cachetools<6.0,>=2.0.0 (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached cachetools-5.5.2-py3-none-any.whl.metadata (5.4 kB)
Collecting pyasn1-modules>=0.2.1 (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting rsa<5,>=3.1.4 (from google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached rsa-4.9-py3-none-any.whl.metadata (4.2 kB)
Collecting requests-oauthlib>=0.7.0 (from google-auth-oauthlib<1.1,>=0.5->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl.metadata (11 kB)
Collecting charset-normalizer<4,>=2 (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached charset_normalizer-3.4.1-cp311-cp311-win_amd64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached urllib3-2.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting certifi>=2017.4.17 (from requests<3,>=2.21.0->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached certifi-2025.1.31-py3-none-any.whl.metadata (2.5 kB)
Collecting MarkupSafe>=2.1.1 (from werkzeug>=1.0.1->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl.metadata (4.1 kB)
Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
Collecting oauthlib>=3.0.0 (from requests-oauthlib>=0.7.0->google-auth-oauthlib<1.1,>=0.5->tensorboard<2.15,>=2.14->tensorflow-intel==2.14.0->tensorflow==2.14->drutai==0.0.1)
  Using cached oauthlib-3.2.2-py3-none-any.whl.metadata (7.5 kB)
Using cached numpy-1.24.3-cp311-cp311-win_amd64.whl (14.8 MB)
Using cached tensorflow-2.14.0-cp311-cp311-win_amd64.whl (2.1 kB)
Using cached tensorflow_io_gcs_filesystem-0.31.0-cp311-cp311-win_amd64.whl (1.5 MB)
Using cached tensorflow_intel-2.14.0-cp311-cp311-win_amd64.whl (284.2 MB)
Using cached ml_dtypes-0.2.0-cp311-cp311-win_amd64.whl (938 kB)
Using cached biopython-1.85-cp311-cp311-win_amd64.whl (2.8 MB)
Using cached click-8.1.8-py3-none-any.whl (98 kB)
Using cached pandas-2.2.3-cp311-cp311-win_amd64.whl (11.6 MB)
Using cached pyfiglet-1.0.2-py3-none-any.whl (1.1 MB)
Using cached rdkit-2024.9.6-cp311-cp311-win_amd64.whl (22.5 MB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading pillow-11.2.0-cp311-cp311-win_amd64.whl (13.8 MB)
   ---------------------------------------- 13.8/13.8 MB 6.7 MB/s eta 0:00:00
Using cached absl_py-2.2.1-py3-none-any.whl (277 kB)
Using cached astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Using cached flatbuffers-25.2.10-py2.py3-none-any.whl (30 kB)
Using cached gast-0.6.0-py3-none-any.whl (21 kB)
Using cached google_pasta-0.2.0-py3-none-any.whl (57 kB)
Using cached grpcio-1.71.0-cp311-cp311-win_amd64.whl (4.3 MB)
Using cached h5py-3.13.0-cp311-cp311-win_amd64.whl (3.0 MB)
Using cached keras-2.14.0-py3-none-any.whl (1.7 MB)
Using cached libclang-18.1.1-py2.py3-none-win_amd64.whl (26.4 MB)
Using cached opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Using cached protobuf-4.25.6-cp310-abi3-win_amd64.whl (413 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached tensorboard-2.14.1-py3-none-any.whl (5.5 MB)
Using cached tensorflow_estimator-2.14.0-py2.py3-none-any.whl (440 kB)
Using cached termcolor-3.0.0-py3-none-any.whl (6.3 kB)
Using cached typing_extensions-4.13.0-py3-none-any.whl (45 kB)
Using cached wrapt-1.14.1-cp311-cp311-win_amd64.whl (35 kB)
Using cached packaging-24.2-py3-none-any.whl (65 kB)
Using cached google_auth-2.38.0-py2.py3-none-any.whl (210 kB)
Using cached google_auth_oauthlib-1.0.0-py2.py3-none-any.whl (18 kB)
Using cached Markdown-3.7-py3-none-any.whl (106 kB)
Using cached requests-2.32.3-py3-none-any.whl (64 kB)
Using cached tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached cachetools-5.5.2-py3-none-any.whl (10 kB)
Using cached certifi-2025.1.31-py3-none-any.whl (166 kB)
Using cached charset_normalizer-3.4.1-cp311-cp311-win_amd64.whl (102 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl (15 kB)
Using cached pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Using cached requests_oauthlib-2.0.0-py2.py3-none-any.whl (24 kB)
Using cached rsa-4.9-py3-none-any.whl (34 kB)
Using cached urllib3-2.3.0-py3-none-any.whl (128 kB)
Using cached oauthlib-3.2.2-py3-none-any.whl (151 kB)
Using cached pyasn1-0.6.1-py3-none-any.whl (83 kB)
Building wheels for collected packages: drutai
  Building wheel for drutai (pyproject.toml) ... done
  Created wheel for drutai: filename=drutai-0.0.1-py3-none-any.whl size=13322 sha256=ef3d75db741b264c3c881de0788864d19675f103b924e7c76a1bb745fa0850d0
  Stored in directory: C:\Users\jianf\AppData\Local\Temp\pip-ephem-wheel-cache-m77mbawc\wheels\24\5c\b0\c57fdbf40016befd2764ccfb990cb87fc11cd83c9e75571bd9
Successfully built drutai
Installing collected packages: pytz, libclang, flatbuffers, wrapt, urllib3, tzdata, typing-extensions, termcolor, tensorflow-io-gcs-filesystem, tensorflow-estimator, tensorboard-data-server, six, pyfiglet, pyasn1, protobuf, Pillow, packaging, opt-einsum, oauthlib, numpy, MarkupSafe, markdown, keras, idna, grpcio, gast, colorama, charset-normalizer, certifi, cachetools, absl-py, werkzeug, rsa, requests, rdkit, python-dateutil, pyasn1-modules, ml-dtypes, h5py, google-pasta, click, biopython, astunparse, requests-oauthlib, pandas, google-auth, google-auth-oauthlib, tensorboard, tensorflow-intel, tensorflow, drutai
Successfully installed MarkupSafe-3.0.2 Pillow-11.2.0 absl-py-2.2.1 astunparse-1.6.3 biopython-1.85 cachetools-5.5.2 certifi-2025.1.31 charset-normalizer-3.4.1 click-8.1.8 colorama-0.4.6 drutai-0.0.1 flatbuffers-25.2.10 gast-0.6.0 google-auth-2.38.0 google-auth-oauthlib-1.0.0 google-pasta-0.2.0 grpcio-1.71.0 h5py-3.13.0 idna-3.10 keras-2.14.0 libclang-18.1.1 markdown-3.7 ml-dtypes-0.2.0 numpy-1.24.3 oauthlib-3.2.2 opt-einsum-3.4.0 packaging-24.2 pandas-2.2.3 protobuf-4.25.6 pyasn1-0.6.1
pyasn1-modules-0.4.2 pyfiglet-1.0.2 python-dateutil-2.9.0.post0 pytz-2025.2 rdkit-2024.9.6 requests-2.32.3 requests-oauthlib-2.0.0 rsa-4.9 six-1.17.0 tensorboard-2.14.1 tensorboard-data-server-0.7.2 tensorflow-2.14.0 tensorflow-estimator-2.14.0 tensorflow-intel-2.14.0 tensorflow-io-gcs-filesystem-0.31.0 termcolor-3.0.0 typing-extensions-4.13.0 tzdata-2025.2 urllib3-2.3.0 werkzeug-3.1.3 wrapt-1.14.1
```
:::
::::

Everything should be all set before you run **Drutai**.
# Orange Chicken: Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation

This repository contains code and data for evaluating model performance in crosslinguistic low-resource settings, using morphological segmentation as the test case. For more information, we refer to the paper [Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00467/110437/Data-driven-Model-Generalizability-in).

```
@article{10.1162/tacl_a_00467,
    author = {Liu, Zoey and Prud’hommeaux, Emily},
    title = "{Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation}",
    journal = {Transactions of the Association for Computational Linguistics},
    volume = {10},
    pages = {393-413},
    year = {2022},
    month = {04},
    abstract = "{Common designs of model evaluation typically focus on monolingual settings, where different models are compared according to their performance on a single data set that is assumed to be representative of all possible data for the task at hand. While this may be reasonable for a large data set, this assumption is difficult to maintain in low-resource scenarios, where artifacts of the data collection can yield data sets that are outliers, potentially making conclusions about model performance coincidental. To address these concerns, we investigate model generalizability in crosslinguistic low-resource scenarios. Using morphological segmentation as the test case, we compare three broad classes of models with different parameterizations, taking data from 11 languages across 6 language families. In each experimental setting, we evaluate all models on a first data set, then examine their performance consistency when introducing new randomly sampled data sets with the same size and when applying the trained models to unseen test sets of varying sizes. The results demonstrate that the extent of model generalization depends on the characteristics of the data set, and does not necessarily rely heavily on the data set size. Among the characteristics that we studied, the ratio of morpheme overlap and that of the average number of morphemes per word between the training and test sets are the two most prominent factors. Our findings suggest that future work should adopt random sampling to construct data sets with different sizes in order to make more responsible claims about model evaluation.}",
    issn = {2307-387X},
    doi = {10.1162/tacl_a_00467},
    url = {https://doi.org/10.1162/tacl\_a\_00467},
    eprint = {https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl\_a\_00467/2006979/tacl\_a\_00467.pdf},
}

```

## Prerequisites

### Install the following:

(1) Python 3

(2) [Morfessor](https://morfessor.readthedocs.io/en/latest/)

(3) [CRFsuite](https://www.chokkan.org/software/crfsuite/)

(4) [OpenNMT](https://opennmt.net/)

## Code

The `code` directory contains the code applied to conduct the experiments.

## Collect initial data

Create a `resource ` folder. This folder is supposed to hold the initial data for each language invited to participate in the experiments. The experiments were performed at different stages, therefore the initial data of different languages have different subdirectories within `resource` (please excuse this).

### The data for three Mexican languages came from [this paper](https://aclanthology.org/N18-1005/). 

(1) download the data from the public repository

(2) for each language, combine all the data from the training, development, and test set; this applies to both the *src files and the *tgt files.

(3) rename the combined data file as, e.g., Yorem Nokki: `mayo_src`, `mayo_tgt`, Nahuatl: `nahuatl_src`, `nahuatl_tgt`.

(4) put the data files within `resource`

### The data for Persian came from [here](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3011).

(1) download the data from the public repository

(2) combine the training, development, and test set to one data file

(3) rename the combined data file as `persian`

(4) put the single data file within `resource`

### The data for German, Zulu and Indonesian came from [this paper](https://aclanthology.org/K15-1017/).

(1) download the data from the public repository

(2) put the downloaded `supplement` folder within `resource`

### The data for English, Russian, Turkish and Finnish came from [this repo](https://github.com/AlexeySorokin/NeuralMorphemeSegmentation).

(1) download the git repo

(2) put the downloaded `NeuralMorphemeSegmentation` folder within `resource`

### Summary of (alternative) Language codes and data directories for running experiments

Yorem Nokki: mayo ```resources/```

Nahuatl: nahuatl ```resources/```

Wixarika: wixarika ```resources/```

English: english/eng ```resources/NeuralMorphemeSegmentation/morphochal10data/```

German: german/ger ```resources/supplement/seg/ger```

Persian: persian ```resources/```

Russian: russian/ru ```resources/NeuralMorphemeSegmentation/data/```

Turkish: turkish/tur ```resources/NeuralMorphemeSegmentation/morphochal10data/```

Finnish: finnish/fin ```resources/NeuralMorphemeSegmentation/morphochal10data/```

Zulu: zulu/zul ```resources/supplement/seg/zul```

Indonesian: indonesian/ind ```resources/supplement/seg/ind```

##  Basic running of the code

### Create experiments folder and subfolders for each language; e.g., Zulu

```mkdir experiments```

```mkdir zulu```

### Generate data (an example)

#### with replacement, data size = 500

```python3 code/segmentation_data.py --input resources/supplement/seg/zul/ --output experiments/zulu/ --lang zul --r with --k 500```

#### without replacement, data size = 500

```python3 code/segmentation_data.py --input resources/supplement/seg/zul/ --output experiments/zulu/ --lang zul --r without --k 500```

### Training models: Morfessor 

#### Train morfessor models 

```python3 code/morfessor/morfessor.py --input experiments/zulu/500/with/ --lang zul```

```python3 code/morfessor/morfessor.py --input experiments/zulu/500/without/ --lang zul```

#### Generate evaluation scrips for morfessor model results

```python3 code/morf_shell.py --input experiments/zulu/500/ --lang zul```

#### Evaluate morfessor model results

```bash zulu_500_morf_eval.sh```

### Training models: CRF

#### Generate CRF shell script

e.g., generating 3-CRF shell script

```python3 code/crf_order.py --input experiments/zulu/500/ --lang zul --r with --order 3```

### Training models: Seq2seq

#### Generate configuration .yaml files

```python3 code/yaml.py --input experiments/zulu/500/ --lang zul --r with```

```python3 code/yaml.py --input experiments/zulu/500/ --lang zul --r without```

#### Generate pbs file (containing also the code to train Seq2seq model)

```python3 code/sirius.py --input experiments/zulu/500/ --lang zul --r with```

```python3 code/sirius.py --input experiments/zulu/500/ --lang zul --r without```

### Gather training results for a given language 

Again take Zulu as an example. Make sure that given a data set size (e.g, 500) and a sampling method (e.g., with replacement), there are three subfolders in the folder ```experiments/zulu/500/with```: 

(1) ```morfessor``` for all ```*eval*``` files from Morfessor; 

(2) ```higher_orders``` for all ```*eval*``` files from k-CRF;

(3) ```seq2seq``` for all ```*eval*``` files from Seq2seq

Then run:

```python3 code/gather.py --input experiments/zulu/ --lang zul --short zulu.txt --full zulu_full.txt --long zulu_details.txt```

### Testing

#### Testing the best CRF

e.g., 4-CRFs trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_crf.py --input experiments/zulu/500/ --data resources/supplement/seg/zul/ --lang zul --n 100 --order 4 --r with --k 50```

#### Testing the best Seq2seq

e.g., trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_seq2seq.py --input experiments/zulu/500/ --data resources/supplement/seg/zul/ --lang zul --n 100 --r with --k 50```

### Do the same for every language

### Generating alternative splits

#### Gather features of data sets, as well as generate heuristic/adversarial data splits

```python3 code/heuristics.py --input experiments/zulu/ --lang zul --output yayyy/ --split A --generate```

#### Gather features of new unseen test sets

```python3 code/new_test_heuristics.py --input experiments/zulu/ --output yayyy/ --lang zul```

## Yayyy: Full Results 

Get them [here](https://drive.google.com/file/d/11s_B9KsVS430VtzLzEaRABW4dpR9jWDj/view?usp=sharing)

## Running analyses and making plots

See ```code/plot.R``` for analysis and making fun plots 

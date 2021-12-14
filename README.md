# orange_chicken

Code and data for **Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation**, to appear in Transactions of the Association for Computational Linguistics

## (alternative) Language codes for running experiments

Yorem Nokki: mayo

Nahuatl: nahuatl

Wixarika: wixarika

English: english/eng

German: german/ger

Persian: persian

Russian: russian/ru

Turkish: turkish/tur

Finnish: finnish/fin

Zulu: zulu/zul

Indonesian: indonesian/ind

## Create experiments folder and subfolders for each language

```mkdir experiments```

```mkdir mayo```

## Generate data (an example)

### with replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r with --k 500```

### without replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r without --k 500```

## Morfessor 

### Train morfessor models 

```python3 code/morfessor/morfessor.py --input experiments/mayo/500/with/ --lang mayo```

```python3 code/morfessor/morfessor.py --input experiments/zulu/500/without/ --lang zul```

### Generate evaluation scrips for morfessor model results

```python3 code/morf_shell.py --input experiments/mayo/500/ --lang mayo```

### Evaluate morfessor model results

```bash mayo_500_morf_eval.sh```

## CRF

### Generate CRF shell script

e.g., generating 3-CRF shell script

```python3 code/crf_order.py --input experiments/mayo/500/ --lang mayo --r with --order 3```

### Seq2seq

### Generate configuration .yaml files

```python3 code/yaml.py --input experiments/mayo/500/ --lang mayo --r with```

```python3 code/yaml.py --input experiments/mayo/500/ --lang mayo --r without```


## Full Results 

Get them [here](https://drive.google.com/file/d/11s_B9KsVS430VtzLzEaRABW4dpR9jWDj/view?usp=sharing)

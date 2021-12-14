# orange_chicken

Code and data for **Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation**, to appear in Transactions of the Association for Computational Linguistics

## (alternative) Language codes and data directories for running experiments

Please see Section 4 in the paper for respective citations regarding the data source of these languages

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

## 1. Create experiments folder and subfolders for each language; take Yorem Nokki as an example

```mkdir experiments```

```mkdir mayo```

## 2. Generate data (an example)

### with replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r with --k 500```

### without replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r without --k 500```

## 3. Training models: Morfessor 

### Train morfessor models 

```python3 code/morfessor/morfessor.py --input experiments/mayo/500/with/ --lang mayo```

```python3 code/morfessor/morfessor.py --input experiments/zulu/500/without/ --lang zul```

### Generate evaluation scrips for morfessor model results

```python3 code/morf_shell.py --input experiments/mayo/500/ --lang mayo```

### Evaluate morfessor model results

```bash mayo_500_morf_eval.sh```

## 4. Training models: CRF

### Generate CRF shell script

e.g., generating 3-CRF shell script

```python3 code/crf_order.py --input experiments/mayo/500/ --lang mayo --r with --order 3```

## 5. Training models: Seq2seq

### Generate configuration .yaml files

```python3 code/yaml.py --input experiments/mayo/500/ --lang mayo --r with```

```python3 code/yaml.py --input experiments/mayo/500/ --lang mayo --r without```

## 6. Testing

### Testing the best CRF

e.g., 4-CRFs trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_crf.py --input experiments/mayo/500/ --data resources/ --lang mayo --n 100 --order 4 --r with --k 50```

### Testing the best Seq2seq

e.g., trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_seq2seq.py --input experiments/mayo/500/ --data resources/ --lang mayo --n 100 --r with --k 50```

## Full Results 

Get them [here](https://drive.google.com/file/d/11s_B9KsVS430VtzLzEaRABW4dpR9jWDj/view?usp=sharing)

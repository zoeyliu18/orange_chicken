# Orange Chicken: Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation

This repository contains code and data for evaluating model performance in crosslinguistic low-resource settings, using morphological segmentation as the test case. For more information, we refer to the paper Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation, to appear in Transactions of the Association for Computational Linguistics

## Resources

The `resource` directory holds the initial data for each language invited to participate in my experiments. The experiments were performed at different stages, therefore the initial data of different languages have different subdirectories within `resource` (please excuse this).

### (alternative) Language codes and data directories for running experiments

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

## 1. Create experiments folder and subfolders for each language; e.g., Yorem Nokki

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

### Generate pbs file (containing also the code to train Seq2seq model)

```python3 code/sirius.py --input experiments/mayo/500/ --lang mayo --r with```

```python3 code/sirius.py --input experiments/mayo/500/ --lang mayo --r without```

## 6. Gather training results for a given language 

Again take Yorem Nokki as an example. Make sure that given a data set size (e.g, 500) and a sampling method (e.g., with replacement), there are three subfolders in the folder ```experiments/mayo/500/with```: 

(1) ```morfessor``` for all ```*eval*``` files from Morfessor; 

(2) ```higher_orders``` for all ```*eval*``` files from k-CRF;

(3) ```seq2seq``` for all ```*eval*``` files from Seq2seq

Then run:

```python3 code/gather.py --input experiments/mayo/ --lang mayo --short mayo.txt --full mayo_full.txt --long mayo_details.txt```

## 7. Testing

### Testing the best CRF

e.g., 4-CRFs trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_crf.py --input experiments/zulu/500/ --data resources/ --lang zul --n 100 --order 4 --r with --k 50```

### Testing the best Seq2seq

e.g., trained from data sets sampled with replacement, for test sets of size 50

```python3 code/testing_seq2seq.py --input experiments/zulu/500/ --data resources/ --lang zul --n 100 --r with --k 50```

## 8. Do the same for every language

## Alternative splits

### Gather features of data sets, as well as generate heuristic/adversarial data splits

```python3 code/heuristics.py --input experiments/zulu/ --lang zul --output yayyy/ --split A --generate```

### Gather features of new unseen test sets

```python3 code/new_test_heuristics.py --input experiments/zulu/ --output yayyy/ --lang zul```

## Yayyy: Full Results 

Get them [here](https://drive.google.com/file/d/11s_B9KsVS430VtzLzEaRABW4dpR9jWDj/view?usp=sharing)

## See ```code/plot.R``` for analysis and making fun plots 

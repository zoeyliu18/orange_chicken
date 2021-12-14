# orange_chicken

Code and data for **Data-driven Model Generalizability in Crosslinguistic Low-resource Morphological Segmentation**, to appear in Transactions of the Association for Computational Linguistics

## (alternative) Language codes 

Yorem Nokki: mayo

Nahuatl: nahuatl

## Create experiments folder and subfolders for each language

```mkdir experiments```

```mkdir mayo```

## Generate data 

### with replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r with --k 500```

### without replacement, data size = 500

```python3 code/segmentation_data.py --input resources/ --output experiments/mayo/ --lang mayo --r without --k 500```

### Train morfessor models 

```python3 code/morfessor/morfessor.py --input experiments/mayo/1000/with/ --lang mayo

## Full Results 

Get them [here](https://drive.google.com/file/d/11s_B9KsVS430VtzLzEaRABW4dpR9jWDj/view?usp=sharing)

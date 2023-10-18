


## Quality Metrics for the Embeddings (Modality Prediction)
10-fold kNN Classification Accuracy and Balanced Accuracy. \
**Hyperparameters:** `k = 13, weights = distance, distance = cosine`.

| **Model**            | **Accuracy (%)** |      |      | **Balanced Accuracy (%)** |      |      |
|----------------------|------------------|------|------|--------------------------|------|------|
|                     | `[CLS]`             | `[SEP]` | `AVG`  | `[CLS]`                    | `[SEP]` | `AVG`  |
| BERT_base            | 54.3             | 57.7 | 61.3 | 38.6                     | 43.3 | 49.9 |
| SciBERT              | 58.2             | 56.4 | 63.6 | 43.9                     | 41.0 | 48.2 |
| BioBERT_base         | 53.2             | 65.2 | 61.1 | 36.0                     | 52.6 | 46.2 |
| PubMedBERT_base      | 57.7             | 74.5 | 64.3 | 42.9                     | 58.6 | 50.1 |
| CORD-19 BERT         | 56.4             | *52.9* | 60.2 | 43.0                     | *37.6* | 44.9 |
| CovidSciBERT         | 64.5             | 60.5 | 62.7 | 49.9                     | 47.9 | 50.6 |
| ClinicalCovidBERT    | 65.4             | 64.5 | 63.4 | 53.2                     | 50.8 | 49.6 |
| RadBERT              | 57.9             | 57.9 | *58.2* | 38.0                     | 38.0 | *39.7* |
| SPECTER 2            | **82.5**         | **83.8** | 68.8 | **75.3**                 | **76.7** | 57.8 |
| BERT_large           | *50.0*           | 58.8 | 60.2 | *34.7*                   | 43.4 | 44.8 |
| BioBERT_large        | 54.4             | 62.1 | 65.5 | 39.8                     | 47.2 | 51.3 |
| PubMedBERT_large     | 57.0             | 61.3 | 60.4 | 40.3                     | 44.2 | 45.3 |
| BioCovidBERT         | 69.5             | 64.8 | **69.6** | 53.8                  | 49.0 | **58.3** |
| Chance Level         |                  | 35.5 (±13) |      |                       | 24.8 (±9) |      |


<br>

## Quality Metrics for the Embeddings (Task Prediction)
10-fold kNN Classification Accuracy and Balanced Accuracy. <br>
**Hyperparameters:** `k = 6, weights = distance, distance = cosine`.

| **Model**           | **Accuracy (%)** |      |      | **Balanced Accuracy (%)** |      |      |
|---------------------|------------------|------|------|--------------------------|------|------|
|                     | `[CLS]`           | `[SEP]` | `AVG`  | `[CLS]`                    | `[SEP]` | `AVG`  |
| BERT_base           | *59.6*           | *58.2* | 64.8 | 27.0                     | 28.4 | 33.9 |
| SciBERT             | 62.7             | 63.0 | 68.6 | 33.3                     | 31.5 | 38.3 |
| BioBERT_base        | 63.9             | 70.2 | 69.6 | 28.6                     | 40.5 | 40.2 |
| PubMedBERT_base     | 66.8             | 70.7 | 67.5 | 34.7                     | 42.3 | 36.9 |
| CORD-19 BERT        | 65.0             | 60.7 | 65.9 | 33.7                     | *25.9* | 34.4 |
| CovidSciBERT        | 70.2             | 70.2 | 71.8 | 42.3                     | 42.4 | 45.1 |
| ClinicalCovid BERT  | 70.9             | 71.3 | 70.0 | 43.6                     | 46.7 | 40.9 |
| RadBERT             | 60.9             | 60.9 | *61.2* | 26.5                   | 26.5 | *26.4* |
| SPECTER 2           | **75.4**         | **74.5** | **74.1** | **56.6**           | **55.9** | **51.5** |
| BERT_large          | 60.0             | 64.1 | 66.6 | *26.2*                   | 34.0 | 38.5 |
| BioBERT_large       | 62.0             | 68.6 | 67.3 | 28.7                     | 37.7 | 36.0 |
| PubMedBERT_large    | 63.0             | 67.7 | 68.9 | 30.0                     | 36.1 | 38.4 |
| BioCovidBERT        | 66.6             | 68.2 | 70.9 | 37.0                     | 39.5 | 42.5 |
| Chance Level        |                  | 36.1 (±6)  |      |                          | 14.8 (±9)  |      |

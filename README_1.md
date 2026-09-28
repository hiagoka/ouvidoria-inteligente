# Ouvidoria Inteligente (Smart Ombudsman)

An NLP project on **citizen complaints sent to a municipal ombudsman office**. It includes a synthetic corpus and a **chunking** study of long texts, with semantic cohesion analysis and 2D visualization.

This repository contains **Deliverable 3** of the challenge.

## Contents

### `corpus_manifestacoes.py`

A synthetic corpus of **40 complaints** in Brazilian Portuguese, split into 5 categories: infrastructure, health, public safety, education and environment.

- About **15% semantic duplicates**: the same issue described in different words
- **5 long complaints** (over 500 characters), used in the chunking exercise
- Helper constants `DUPLICATAS_REAIS` (known duplicates) and `IDS_LONGAS_ESPERADAS` (IDs of the long complaints)

```bash
python corpus_manifestacoes.py   # prints a corpus summary
```

### `chunking_manifestacoes.ipynb`

A notebook that applies LangChain's `RecursiveCharacterTextSplitter` to the 5 long complaints and compares two configurations:

| Config | `chunk_size` | `chunk_overlap` |
|--------|--------------|-----------------|
| A | 200 | 20 (~10%) |
| B | 350 | 100 (~29%) |

The notebook answers three questions:

1. How does overlap affect **semantic cohesion** between consecutive chunks? Cohesion is measured with cosine similarity.
2. Which configuration **best preserves the meaning** of the complaints?
3. Do chunks from the same complaint stay **close together in 2D space**? The analysis uses PCA and tSNE.

**Conclusion:** Config B best preserves the meaning of each complaint, and chunks from the same complaint form visible clusters in the 2D projections.

> Embeddings use **TFIDF** instead of `sentence-transformers`, because the development environment had no access to Hugging Face. The notebook explains how to make the swap.

### `chunks_pca_tsne.png`

The chunks projected into 2D with PCA and tSNE, with one color per complaint.

## Getting started

```bash
pip install numpy pandas matplotlib scikit-learn langchain-text-splitters jupyter
jupyter notebook chunking_manifestacoes.ipynb
```

## Project structure

```
ouvidoria-inteligente/
├── corpus_manifestacoes.py         # Corpus of 40 complaints
├── chunking_manifestacoes.ipynb    # Deliverable 3: chunking and analysis
└── chunks_pca_tsne.png             # PCA and tSNE visualization
```

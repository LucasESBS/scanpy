import numpy as np
import scanpy.api as sc
from anndata import AnnData

def test_add_score():
    adata = AnnData(np.random.randint(0, 1000, 100000).reshape((100, 1000)))
    gene_names = np.array([''.join([chr(x) for x in np.random.randint(65, 90, 6)]) for n in range(2000)])
    adata.var_names = gene_names[:1000]
    sc.pp.normalize_per_cell(adata, counts_per_cell_after =1e4)
    sc.pp.log1p(adata)
    some_genes = np.concatenate([np.unique(gene_names[np.random.randint(0, 1000, 10)]), np.unique(gene_names[np.random.randint(1000, 2000, 3)])])
    sc.tl.add_score(adata, gene_list = some_genes, score_name = "Test")
    assert adata.obs['Test'].dtype == 'float32'





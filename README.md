# AIDS Antiviral Screen Data

## Introduction

This is a procedure for creating an AIDS Antiviral dataset to be used as a sample dataset for virtual screening.

See https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data

## Binary Classiication Labels

- CA - Confirmed active
- CM - Confirmed moderately active
- CI - Confirmed inactive

## Usage

```bash
bash run.sh
```

## Results

```
Finished conversion 41925 (errors 762)
{'CA': 421, 'CI': 40433, 'CM': 1066}
{0: 40433, 1: 1487}
          NSC Conclusion                                                smi  outcome
0          48         CI  CCC1=[O+][Cu-3]2([O+]=C(CC)C1)[O+]=C(CC)CC(CC)...        0
1          78         CI  C(=C/c1ccccc1)\C1=[O+][Cu-3]2([O+]=C(/C=C/c3cc...        0
2         128         CI                   CC(=O)N1c2ccccc2Sc2c1ccc1ccccc21        0
3         163         CI  Nc1ccc(/C=C/c2ccc(N)cc2S(=O)(=O)O)c(S(=O)(=O)O)c1        0
4         164         CI                             O=S(=O)(O)CCS(=O)(=O)O        0
...       ...        ...                                                ...      ...
41915  706739         CI  CCC1CCC2c3c([nH]c4ccc(C)cc34)C3C(=O)N(N(C)C)C(...        0
41916  706740         CI  Cc1ccc2[nH]c3c(c2c1)C1CCC(C(C)(C)C)CC1C1C(=O)N...        0
41917  706741         CI  Cc1ccc(N2C(=O)C3c4[nH]c5ccccc5c4C4CCC(C(C)(C)C...        0
41918  706742         CI  Cc1cccc(N2C(=O)C3c4[nH]c5ccccc5c4C4CCC(C(C)(C)...        0
41919  706805         CI  CCCCCC=C(c1cc(Cl)c(OC)c(-c2nc(C)no2)c1)c1cc(Cl...        0

[41920 rows x 4 columns]
```

## TODO

To append IC50 and EC50 values to dataset.

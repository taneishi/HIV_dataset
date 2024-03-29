# HIV Antiviral Screening Dataset

## Introduction

The *Developmental Therapeutics Program*, DTP of the *National Cancer Institute*, NCI released *AIDS Antiviral Screen Data* which had screened approximately 40,000 compounds for anti-HIV activity. Chemical structure data of the compounds that do not have a non-disclosure agreement are made publicly available. It is also accompanied by a 3D structure generated by *CORINA*. Here we described a procedure to create a sample dataset for virtual screening rom HIV Antiviral Screening Dataset.

## Binary Classiication Labels

The results of the screening test released in May 2004 placed each compound in one of three categories.

- CA - Confirmed Active
- CM - Confirmed Moderately Active
- CI - Confirmed Inactive

Each compound is assigned a Cancer Chemotherapy *National Service Center*, NSC number, NCI's internal ID, and one of the above categories is registered as a screening test result.

## EC50 and IC50

There is also data on the concentration needed to see the protective effect against infected cells, EC50, where EC50 is the base 10 logarithm of the concentration of the compound that protects 50% from infected cells. There are also data on the concentration needed to inhibit the growth of uninfected cells, IC50. IC50 is the concentration of the compound that inhibits the growth of uninfected cells by 50%. Resulting data are determined from individual dose-response curves and are synthesized by trained researchers; EC50 and IC50 data are computer-generated averages and do not necessarily reflect all considerations in making a determination.

## Results

```console
Converting MOL to SMILES: 41998 (errors 689)
Conversion finished.
{'CA': 421, 'CI': 40506, 'CM': 1066}
{0: 40506, 1: 1487}
          NSC Conclusion                                             smiles  interaction
0          48         CI  CCC1=[O+][Cu-3]2([O+]=C(CC)C1)[O+]=C(CC)CC(CC)...            0
1          78         CI  C(=C/c1ccccc1)\C1=[O+][Cu-3]2([O+]=C(/C=C/c3cc...            0
2         128         CI                   CC(=O)N1c2ccccc2Sc2c1ccc1ccccc21            0
3         163         CI  Nc1ccc(/C=C/c2ccc(N)cc2S(=O)(=O)O)c(S(=O)(=O)O)c1            0
4         164         CI                             O=S(=O)(O)CCS(=O)(=O)O            0
...       ...        ...                                                ...          ...
41988  706739         CI  CC[C@@H]1CC[C@H]2c3c([nH]c4ccc(C)cc34)[C@H]3C(...            0
41989  706740         CI  Cc1ccc2[nH]c3c(c2c1)[C@@H]1CC[C@@H](C(C)(C)C)C...            0
41990  706741         CI  Cc1ccc(N2C(=O)[C@@H]3[C@@H]4C[C@H](C(C)(C)C)CC...            0
41991  706742         CI  Cc1cccc(N2C(=O)[C@@H]3[C@@H]4C[C@H](C(C)(C)C)C...            0
41992  706805         CI  CCCCCC=C(c1cc(Cl)c(OC)c(-c2nc(C)no2)c1)c1cc(Cl...            0
```

## Reference

- [AIDS Antiviral Screen Data - NCI DTP Data](https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data)

## TODO

- IC50 and EC50 values.

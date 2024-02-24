import pandas as pd
from rdkit import Chem, RDLogger

RDLogger.DisableLog('rdApp.*')

def main():
    smiles = []
    errors = 0
    for mol in Chem.SDMolSupplier('data/AIDO99SD.SDF'):
        try:
            smi = Chem.MolToSmiles(mol)
            nsc = int(mol.GetProp('NSC').strip())
            smiles.append([nsc, smi])
            print('\rConverting MOL to SMILES: %5d (errors %3d)' % (len(smiles), errors), end='')
        except Exception as e:
            errors += 1

    print('\nConversion finished.')
    
    smiles = pd.DataFrame(smiles, columns=['NSC', 'smi'])

    df = pd.read_csv('data/aids_conc_may04.txt', sep=',')

    df.columns = df.columns.str.strip()
    df['Conclusion'] = df['Conclusion'].str.strip()

    df = pd.merge(df, smiles, on='NSC')

    df['interaction'] = (df['Conclusion'] != 'CI').astype(int)

    print(df.groupby('Conclusion').size().to_dict())
    print(df.groupby('interaction').size().to_dict())

    df.to_csv('data/hiv_antiviral.tsv', sep='\t', index=False)
    print(df)

if __name__ == '__main__':
    main()

import pandas as pd
from rdkit import Chem, RDLogger

RDLogger.DisableLog('rdApp.*')

def main():
    smiles = []
    errors = 0
    for mol in Chem.SDMolSupplier('data/structures.sdf'):
        try:
            smi = Chem.MolToSmiles(mol)
            nsc = int(mol.GetProp('NSC').strip())
            smiles.append([nsc, smi])
            print(f'\rConverting MOL to SMILES: {len(smiles):5d} (errors {errors:3d})', end='')
        except Exception as e:
            errors += 1

    print('\nConversion finished.')
    
    smiles = pd.DataFrame(smiles, columns=['NSC', 'smiles'])

    df = pd.read_csv('data/conclusions.csv')

    df.columns = df.columns.str.strip()
    df['Conclusion'] = df['Conclusion'].str.strip()

    df = pd.merge(df, smiles, on='NSC')

    df['interaction'] = (df['Conclusion'] != 'CI').astype(int)

    print(df.groupby('Conclusion').size().to_dict())
    print(df.groupby('interaction').size().to_dict())

    df.to_csv('data/hiv.tsv', sep='\t', index=False)
    print(df)

if __name__ == '__main__':
    main()

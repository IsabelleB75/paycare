import pytest
import pandas as pd
import os
from etl import extract_data, transform_data, load_data

# Test extraction
def test_extract_data():
    data = extract_data('data/input_data.csv')
    assert data is not None
    assert len(data) == 6
    assert 'salary' in data.columns

# Test transformation
def test_transform_data():
    data = pd.DataFrame({
        'id': [1, 2],
        'name': ['Alice', 'Bob'],
        'age': [30, None],
        'salary': [100000, 50000]
    })
    result = transform_data(data)
    
    # Verifie que la ligne avec NaN est supprimee
    assert len(result) == 1
    
    # Verifie le calcul de la taxe (10%)
    assert result.iloc[0]['tax'] == 10000
    
    # Verifie le calcul du salaire net
    assert result.iloc[0]['net_salary'] == 90000

# Test chargement
def test_load_data():
    data = pd.DataFrame({
        'id': [1],
        'name': ['Test'],
        'salary': [50000],
        'tax': [5000],
        'net_salary': [45000]
    })
    output_path = 'data/test_output.csv'
    load_data(data, output_path)
    
    # Verifie que le fichier existe
    assert os.path.exists(output_path)
    
    # Nettoyage
    os.remove(output_path)

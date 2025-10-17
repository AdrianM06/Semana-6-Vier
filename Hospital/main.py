import functions as f


def main():
    patients = []

    pathologies_data = {
        "Respiratory system": [
            {"id": 1, "name": "Cystic Fibrosis", "price": 300},
            {"id": 2, "name": "Emphysema", "price": 500},
            {"id": 3, "name": "Tuberculosis", "price": 450}
        ],
        "Nervous system": [
            {"id": 4, "name": "Parkinson", "price": 800},
            {"id": 5, "name": "Epilepsy", "price": 600}
        ],
        "Endocrine system": [
            {"id": 6, "name": "Diabetes", "price": 350},
            {"id": 7, "name": "Acromegaly", "price": 700},
            {"id": 8, "name": "Hashimoto's thyroiditis", "price": 900}
        ]
    }

    pathologies = f.create_patohlogies(pathologies_data)
    
    for data in pathologies.values():
        for pat in data:
            print(pat.show_attr())


main()
from pathology import Pathology


def create_patohlogies(pathologies_data):
    pathologies = {}

    for system, data in pathologies.items():
        pathologies[system] = []
        for pathology in data:
            pat = Pathology(pathology["id"], pathology["name"], pathology["price"])
            pathologies[system].append(pat)
    
    return pathologies
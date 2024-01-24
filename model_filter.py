from typing import List, Dict


def filter_by_bounding_box(
    target_model: Dict,
    attempted_models: List[Dict]
) -> List[Dict]:
    """Filters attempted models by bounding box rounded to 3 decimal places"""
    filtered_models = []
    incorrect_models = []

    for model in attempted_models:
        if (
            (
                round(model["bbMin"][0], 3) == round(target_model["bbMin"][0], 3)
                and round(model["bbMax"][0], 3) == round(target_model["bbMax"][0], 3)
            )
            and (
                round(model["bbMin"][1], 3) == round(target_model["bbMin"][1], 3)
                and round(model["bbMax"][1], 3) == round(target_model["bbMax"][1], 3)
            )
            and (
                round(model["bbMin"][2], 3) == round(target_model["bbMin"][2], 3)
                and round(model["bbMax"][2], 3) == round(target_model["bbMax"][2], 3)
            )
        ):
            filtered_models.append(model)
        else:
            incorrect_models.append(model)
    print(
        "After filtering by bounding box, the following models matches with the target model: ",
        [filtered_model["file_name"] for filtered_model in filtered_models]
    )
    print(
        "After filtering by bounding box, the following models does not match with the target model: ",
        [incorrect_model["file_name"] for incorrect_model in incorrect_models]
    )
    return filtered_models, incorrect_models

def filter_by_volume(target_model: Dict, attempted_models: List[Dict], incorrect_models: List[Dict]) -> List[Dict]:
    """Filters attempted models by volume rounded to 3 decimal places"""
    filtered_models = []
    for model in attempted_models:
        if round(model["volume"], 3) == round(target_model["volume"], 3):
            filtered_models.append(model)
        else:
            incorrect_models.append(model)
    print(
        "After filtering by volume, the following models matches with the target model: ",
        [filtered_model["file_name"] for filtered_model in filtered_models]
    )
    print(
        "After filtering by volume, the following models does not match with the target model: ",
        [incorrect_model["file_name"] for incorrect_model in incorrect_models]
    )
    return filtered_models, incorrect_models

def filter_by_faces(target_model: Dict, attempted_models: List[Dict], incorrect_models: List[Dict]) -> List[Dict]:
    """Filters attempted models by the number of faces"""
    filtered_models = []
    for model in attempted_models:
        if len(model["faces"]) == len(target_model["faces"]):
            filtered_models.append(model)
        else:
            incorrect_models.append(model)
    print(
        "After filtering by faces, the following models matches with the target model: ",
        [filtered_model["file_name"] for filtered_model in filtered_models]
    )
    print(
        "After filtering by faces, the following models does not match with the target model: ",
        [incorrect_model["file_name"] for incorrect_model in incorrect_models]
    )
    return filtered_models, incorrect_models
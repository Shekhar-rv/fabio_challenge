from json import load, JSONDecodeError
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Dict


def get_data(file_name: str) -> Dict:
    """Converts json file to dict"""
    with open(f"data/{file_name}", "r", encoding="utf-8") as f:
        try:
            data = load(f)
            data["file_name"] = file_name
        except JSONDecodeError as e:
            print(e)
            data = {}
    return data

def get_dict_stats(data: Dict) -> Dict:
    """Counts the number of each face in the data"""
    dict_stats = {}
    dict_stats["file_name"] = data["file_name"]
    dict_stats["volume"] = round(data["volume"], 3)
    dict_stats["faces_count"] = len(data["faces"])
    print(f"Stats for {data['file_name']}: {dict_stats}")
    return dict_stats

def area_data_checker(target_model: Dict, attempted_model: Dict, stats_dict: Dict) -> Dict:
    """
    This function is used to check the data points (rounded to 4 decimal places) in each attempted models and comparing it with the target model.
    """
    check_list = [round(face["area"], 4) for face in target_model["faces"]]
    target_model_volume = round(target_model["volume"], 4)
    target_model_faces_count = len(target_model["faces"])
    data_counter = 0
    for face in attempted_model["faces"]:
        if round(face["area"], 4) in check_list:
            data_counter += 1
    stats_dict["faces_area_count"] = data_counter
    percentage_difference = abs(target_model_faces_count - data_counter) / target_model_faces_count
    stats_dict["faces_score"] = round(max(0, 1 - percentage_difference), 3)
    percentage_difference = abs(target_model_volume - stats_dict["volume"]) / target_model_volume
    stats_dict["volume_score"] = round(max(0, 1 - percentage_difference), 3)
    return stats_dict

def score_calc(stats_dict: Dict) -> Dict:
    """Calculates the score for each model"""
    volume_score = stats_dict["volume_score"] * 5
    faces_score = stats_dict["faces_score"] * 5
    stats_dict["overall_score"] = round(volume_score + faces_score, 1)
    return stats_dict
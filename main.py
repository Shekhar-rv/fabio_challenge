from typing import List
from model_filter import filter_by_bounding_box, filter_by_volume
from utils import get_data, get_dict_stats, plot_face



if __name__ == "__main__":
    # Get the data and compare the stats
    attempt1 = get_data(file_name="attempt1.json")
    attempt1_count = get_dict_stats(data=attempt1)
    attempt2 = get_data(file_name="attempt2.json")
    attempt2_count = get_dict_stats(data=attempt2)
    attempt3 = get_data(file_name="attempt3.json")
    attempt3_count = get_dict_stats(data=attempt3)
    attempt4 = get_data(file_name="attempt4.json")
    attempt4_count = get_dict_stats(data=attempt4)
    target = get_data(file_name="target.json")
    target_count = get_dict_stats(data=target)



    # Trying out the filtering
    filtered_models, incorrect_models = filter_by_bounding_box(
        target_model=target, attempted_models=[attempt1, attempt2, attempt3, attempt4]
    )
    filtered_models, incorrect_models = filter_by_volume(target_model=target, attempted_models=filtered_models, incorrect_models=incorrect_models)

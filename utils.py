from json import load, JSONDecodeError
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def get_data(file_name: str) -> dict:
    """Converts json file to dict"""
    with open(f"data/{file_name}", "r", encoding="utf-8") as f:
        try:
            data = load(f)
            data["file_name"] = file_name
        except JSONDecodeError as e:
            print(e)
            data = {}
    return data


def get_dict_stats(data: dict) -> dict:
    """Counts the number of each face in the data"""
    dict_stats = {}
    dict_stats["file_name"] = data["file_name"]
    dict_stats["volume"] = round(data["volume"], 3)

    for face in data["faces"]:
        for i in face:
            if i in dict_stats:
                dict_stats[i] += 1
            else:
                dict_stats[i] = 1
    print(f"Stats for {data['file_name']}: {dict_stats}")
    return dict_stats

def plot_face(ax, bbMin, bbMax, centroid, area):
    x = [bbMin[0], bbMax[0]]
    y = [bbMin[1], bbMax[1]]
    z = [bbMin[2], bbMax[2]]

    ax.plot(x, y, z, color="blue", alpha=0.5)

    # Plot the centroid
    ax.scatter(centroid[0], centroid[1], centroid[2], color="red", marker="o")

    # Annotate the face with its area
    ax.text(
        centroid[0],
        centroid[1],
        centroid[2],
        f"Area: {area:.5f}",
        color="black",
        fontsize=8,
    )

def plot_3d(data: dict):
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each face
    for face_data in data["faces"]:
        plot_face(ax, face_data['bbMin'], face_data['bbMax'], face_data['centroid'], face_data['area'])

    # Set labels for the axes
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # Show the plot
    plt.show()
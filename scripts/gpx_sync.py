"""
If you do not want bind any account
Only the gpx files in GPX_OUT sync
"""

from config import GPX_FOLDER, JSON_FILE, SQL_FILE
from utils import make_activities_file
import os
import gpxpy

if __name__ == "__main__":
    print("only sync gpx files in GPX_OUT")

    for filename in os.listdir(GPX_FOLDER):
        if filename.endswith(".gpx"):
            gpx_file = open(os.path.join(GPX_FOLDER, filename), 'r')
            gpx = gpxpy.parse(gpx_file)
            gpx_file.close()

            if gpx.length_2d() < 4000: #这里设置呈现的最小公里数
                os.remove(os.path.join(GPX_FOLDER, filename))
                print(f"Removed {filename} due to distance < 4km")

    make_activities_file(SQL_FILE, GPX_FOLDER, JSON_FILE)

"""
If you do not want bind any account
Only the gpx files in GPX_OUT sync
"""

# 导入所需的模块和文件
from config import GPX_FOLDER, JSON_FILE, SQL_FILE
from utils import make_activities_file
import os
import gpxpy

# 主函数：只同步 GPX_OUT 文件夹下的 GPX 文件
if __name__ == "__main__":
    print("only sync gpx files in GPX_OUT")

    # 遍历 GPX_FOLDER 文件夹下所有文件
    for filename in os.listdir(GPX_FOLDER):
        # 如果文件是 .gpx 格式
        if filename.endswith(".gpx"):
            # 打开 GPX 文件，解析文件内容，并关闭文件
            gpx_file = open(os.path.join(GPX_FOLDER, filename), 'r')
            gpx = gpxpy.parse(gpx_file)
            gpx_file.close()

            # 如果 GPX 文件的距离小于 4 公里
            if gpx.length_2d() < 4000:
                # 删除该文件
                os.remove(os.path.join(GPX_FOLDER, filename))
                # 在控制台打印提示信息
                print(f"Removed {filename} due to distance < 4km")

    # 在指定的 SQL_FILE 和 JSON_FILE 中生成活动文件
    make_activities_file(SQL_FILE, GPX_FOLDER, JSON_FILE)

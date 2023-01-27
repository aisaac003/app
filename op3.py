import numpy as np
import pandas as pd
import cv2 as cv
import open3d as o3d 

carpeta = "D:\Ingeniería Mecánica Eléctrica\Ciclo VII - 2023\Sistemas Automáticos y Control (SAC)\Proyecto_semestral\Programación\app\fragment.ply"

pcd = o3d.visualization.draw_geometries(carpeta)
print (pcd)
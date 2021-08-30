import homcloud.interface as hc  # HomCloudのインターフェス
import homcloud.paraview_interface as pv  # 3次元可視化用
import numpy as np
import matplotlib.pyplot as plt

pointcloud = np.loadtxt("test.txt")

pointcloud.shape
np.min(pointcloud, axis=0), np.max(pointcloud, axis=0)
#pv.show([pv.PointCloud.from_array(pointcloud)])

PHI = 0.52500

L1 = ((500*np.pi)/PHI)**(1/3)

hc.PDList.from_alpha_filtration(pointcloud, 
                                 save_to="pointcloud-periodic-test.pdgm",
                                periodicity=[(0, L1), (0, L1), (0, L1)],
                                no_squared=True,
                                save_boundary_map=True)


pdlist = hc.PDList("pointcloud-periodic-test.pdgm")

pd2 = pdlist.dth_diagram(2)
#pd2.histogram((0, 1.4)).plot(colorbar={"type": "log"})
plt.hist(pd2.deaths - pd2.births, bins=100); 

plt.savefig("pointcloud-periodic-test.png")
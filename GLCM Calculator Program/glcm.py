from matplotlib import pyplot as plt
import numpy as np

# load an image
img_rgb = plt.imread("gsimg.jpg")

# get img greyscale
finl_img = np.average(img_rgb,axis=2).astype(np.uint8)

# choose a positional operator
pos_op = [1,0]

# init glcm array
glcm = np.zeros([256,256])

# iterate over image and complete glcm
for i in range(finl_img.shape[0]): # row
    for j in range(finl_img.shape[1]): # col
        init_val = finl_img[i,j]
        try:
            target = finl_img[i+pos_op[0],j+pos_op[1]]
        except IndexError:
        	continue # out of img bounds
        glcm[init_val,target]+=1

glcm = glcm/np.sum(glcm)

plt.imshow(np.log(glcm+1e-6))
plt.show()

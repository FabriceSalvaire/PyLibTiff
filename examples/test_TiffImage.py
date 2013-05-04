####################################################################################################
# 
# pylibtiff - A Python binding to libtiff 
# Copyright (C) Salvaire Fabrice 2013 
# 
####################################################################################################

####################################################################################################

from Image import Image
from TiffImage import write_from_image, load_to_image

####################################################################################################

file_name = 'image_gray8.tiff'
image = Image(format='gray8', width=100, height=100, is_planar=True)
image.buffer[50,:] = 255
image.buffer[:,50] = 255
write_from_image(image, file_name, compression=False)

file_name = 'image_gray16.tiff'
image = Image(format='gray16', width=100, height=100, is_planar=True)
image.buffer[50,:] = 2**15
image.buffer[:,50] = 2**16 -1
write_from_image(image, file_name, compression=False)

image = load_to_image(file_name)
print image.buffer[48:53,48:53]

file_name = 'image_rgb8.tiff'
image = Image(format='rgb8', width=100, height=100, is_planar=False)
image.buffer[50,:,0] = 255
image.buffer[:,50,1] = 255
image.buffer[:,:,2] = 128
write_from_image(image, file_name, compression=False)

####################################################################################################
#
# End
#
####################################################################################################

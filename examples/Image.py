####################################################################################################
# 
# pylibtiff - A Python binding to libtiff 
# Copyright (C) Salvaire Fabrice 2013 
# 
####################################################################################################

####################################################################################################

import numpy as np

####################################################################################################

class Image(object):
       
    #######################################
    
    def __init__(self, format, width, height, is_planar=True):

        if not (width and height):
            raise ValueError('Wrong image size %i x %i' % (width, height))
        self.height = height
        self.width = width
       
        dtype = self._init_from_format(format, is_planar)

        self.size = self._compute_size()

        self.buffer = np.zeros(self.size, dtype=dtype)
        self.size_byte = self.buffer.nbytes
        self.reshape()

    #######################################
    
    def _init_from_format(self, format, is_planar):

        self.format = format
        self.is_planar = is_planar

        if format == 'gray8':
            dtype = np.uint8
            self.bits_per_pixel = 8
            self.samples_per_pixel = 1
            # interleaved makes no sense
            self.is_planar = True

        elif format == 'gray16':
            dtype = np.uint16
            self.bits_per_pixel = 16
            self.samples_per_pixel = 1
            # interleaved makes no sense
            self.is_planar = True

        elif format == 'rgb8':
            dtype = np.uint8
            self.bits_per_pixel = 8
            self.samples_per_pixel = 3

        elif format == 'rgb16':
            dtype = np.uint16
            self.bits_per_pixel = 16
            self.samples_per_pixel = 3

        else:
            raise NameError('Image format %s is not supported' % (format))

        return dtype

    #######################################

    def _compute_size(self):

        """ Return the size in pixels. """

        return self.width * self.height * self.samples_per_pixel

    #######################################

    def reshape_to_linear(self):

        """ Reshape the buffer to a linear shape. """

        self.buffer.shape = self.size
    
    #######################################

    def planar_shape(self, array):

        """ Reshape the buffer to a planar 3D shape [*samples_per_pixel*, *height*, *width*]. If
        *samples_per_pixel* is equal to one then this dimension is omitted.
        """

        if self.samples_per_pixel > 1:
            array.shape = self.samples_per_pixel, self.height, self.width
        else:
            array.shape = self.height, self.width

    #######################################

    def interleaved_shape(self, array):

        """ Reshape the buffer to an interleaved 3D shape [*height*, *width*, *samples_per_pixel*].
        """

        if self.samples_per_pixel > 1:
            array.shape = self.height, self.width, self.samples_per_pixel
        else:
            array.shape = self.height, self.width

    #######################################

    def reshape(self):

        """ Reshape the buffer to its normal (3D) shape. """

        if self.is_planar:
            self.planar_shape(self.buffer)
        else:
            self.interleaved_shape(self.buffer)

####################################################################################################
#
# End
#
####################################################################################################

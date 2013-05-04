####################################################################################################
# 
# pylibtiff - A Python binding to libtiff 
# Copyright (C) Salvaire Fabrice 2013 
# 
####################################################################################################

####################################################################################################

from Image import Image
import LibTiff as Tiff

####################################################################################################

class TiffImage(object):

    ##############################################
    
    def __init__(self, file_name, mode='r'):
        
        """ Open a Tiff file with *mode* set to read "r" or write "w". """

        self.file_name = file_name

        self.tif = Tiff.TIFFOpen(str(file_name), mode)
        if self.tif is None:
            raise NameError("Can't open Tiff file %s" % (file_name))

    ##############################################
    
    def __del__(self):

        Tiff.TIFFClose(self.tif)

    ##############################################
    
    def load(self):

        """ Load the image and return an :class:`Image` instance. """

        bits_per_pixel = self.get_bits_per_sample()
        height = self.get_image_length()
        samples_per_pixel = self.get_sample_per_pixel()
        width = self.get_image_width()
        photometric = self.get_photometric()
        planar_config = self.get_planar_config()
    
        is_planar = planar_config == Tiff.PLANARCONFIG_SEPARATE
        # Tiff.PLANARCONFIG_CONTIG   = 1 = Chunky format
        # Tiff.PLANARCONFIG_SEPARATE = 2 = Planar format
        
        if samples_per_pixel == 1 and bits_per_pixel == 16 and photometric == Tiff.PHOTOMETRIC_MINISBLACK:
            format_ = 'gray16'
        elif samples_per_pixel == 3 and bits_per_pixel == 8 and photometric == Tiff.PHOTOMETRIC_RGB:
            format_ = 'rgb8'
        else:
            raise NameError('Image format of %s is not supported' % (self.file_name))
    
        image = Image(format_, width, height, is_planar)
    
        image.reshape_to_linear()
        if format_ == 'gray16':
            Tiff.read_scanline_gray16(self.tif, image.buffer)
        elif format_ == 'rgb8':
            Tiff.read_scanline_rgb8(self.tif, image.buffer)
        else:
            raise NotImplementedError
        image.reshape()
    
        return image

    ##############################################
    
    def write(self, image, compression=False):

        """ Write *image* to the Tiff file. """
    
        if image.samples_per_pixel == 1 or not image.is_planar: # cf. TIFF p38 
            planar_config = Tiff.PLANARCONFIG_CONTIG
        else:
            planar_config = Tiff.PLANARCONFIG_SEPARATE
    
        if image.format in ('gray8', 'gray16'):
            photometric = Tiff.PHOTOMETRIC_MINISBLACK
        elif image.format in ('rgb8', 'rgb16'): # Fixme: is_rgb
            photometric = Tiff.PHOTOMETRIC_RGB
        else:
            raise NotImplementedError

        self.set_bits_per_sample(image.bits_per_pixel)
        self.set_image_length(int(image.height))
        self.set_image_width(int(image.width))
        self.set_photometric(photometric)
        self.set_sample_per_pixel(image.samples_per_pixel)
        self.set_planar_config(planar_config)
        self.set_orientation(Tiff.ORIENTATION_BOTLEFT) # TOPLEFT
    
        self.set_row_per_strip(Tiff.TIFFDefaultStripSize(self.tif, 0))
    
        if compression:
            self.set_compression(Tiff.COMPRESSION_LZW)
    
        image.reshape_to_linear()
        if image.format == 'gray8':
            Tiff.write_scanline_gray8(self.tif, image.buffer)
        elif image.format == 'gray16':
            Tiff.write_scanline_gray16(self.tif, image.buffer)
        elif image.format == 'rgb8':
            Tiff.write_scanline_rgb8(self.tif, image.buffer)
        elif image.format == 'rgb16':
            Tiff.write_scanline_rgb16(self.tif, image.buffer)
        else:
            raise NotImplementedError
        image.reshape()

    ##############################################

    # Fixme: getattr?
    
    def get_date_time(self):

        return Tiff.TIFFGetField_TIFFTAG_DATETIME(self.tif)

    ##############################################
    
    def get_image_description(self):

        return Tiff.TIFFGetField_TIFFTAG_IMAGEDESCRIPTION(self.tif)

    ##############################################
    
    def get_software(self):

        return Tiff.TIFFGetField_TIFFTAG_SOFTWARE(self.tif)

    ##############################################
    
    def get_bits_per_sample(self):

        return Tiff.TIFFGetField_TIFFTAG_BITSPERSAMPLE(self.tif)

    ##############################################
    
    def get_image_length(self):

        return Tiff.TIFFGetField_TIFFTAG_IMAGELENGTH(self.tif)

    ##############################################
    
    def get_sample_per_pixel(self):

        return Tiff.TIFFGetField_TIFFTAG_SAMPLESPERPIXEL(self.tif)

    ##############################################
    
    def get_image_width(self):

        return Tiff.TIFFGetField_TIFFTAG_IMAGEWIDTH(self.tif)

    ##############################################
    
    def get_photometric(self):

        return Tiff.TIFFGetField_TIFFTAG_PHOTOMETRIC(self.tif)

    ##############################################
    
    def get_planar_config(self):

        return Tiff.TIFFGetField_TIFFTAG_PLANARCONFIG(self.tif)

    ##############################################
    
    def get_orientation(self):

        return Tiff.TIFFGetField_TIFFTAG_ORIENTATION(self.tif)

    ##############################################
    
#   def set_date_time(self, value):
#
#       return Tiff.TIFFSetField_TIFFTAG_DATETIME(self.tif)

    ##############################################
    
#   def set_image_description(self, value):
#
#       return Tiff.TIFFSetField_TIFFTAG_IMAGEDESCRIPTION(self.tif)

    ##############################################
    
    def set_software(self, value):

        return Tiff.TIFFSetField_TIFFTAG_SOFTWARE(self.tif, value)

    ##############################################
    
    def set_bits_per_sample(self, value):

        return Tiff.TIFFSetField_TIFFTAG_BITSPERSAMPLE(self.tif, value)

    ##############################################
    
    def set_image_length(self, value):

        return Tiff.TIFFSetField_TIFFTAG_IMAGELENGTH(self.tif, value)

    ##############################################
    
    def set_sample_per_pixel(self, value):

        return Tiff.TIFFSetField_TIFFTAG_SAMPLESPERPIXEL(self.tif, value)

    ##############################################
    
    def set_image_width(self, value):

        return Tiff.TIFFSetField_TIFFTAG_IMAGEWIDTH(self.tif, value)

    ##############################################
    
    def set_photometric(self, value):

        return Tiff.TIFFSetField_TIFFTAG_PHOTOMETRIC(self.tif, value)

    ##############################################
    
    def set_planar_config(self, value):

        return Tiff.TIFFSetField_TIFFTAG_PLANARCONFIG(self.tif, value)

    ##############################################
    
    def set_orientation(self, value):

        return Tiff.TIFFSetField_TIFFTAG_ORIENTATION(self.tif, value)

    ##############################################
    
    def set_row_per_strip(self, value):

        return Tiff.TIFFSetField_TIFFTAG_ROWSPERSTRIP(self.tif, value)

    ##############################################
    
    def set_compression(self, value):

        return Tiff.TIFFSetField_TIFFTAG_COMPRESSION(self.tif, value)

    ##############################################
    
    def change_directory(self, directory):

        return Tiff.TIFFSetDirectory(self.tif, directory)

    ##############################################
    
    def change_to_next_directory(self):

        return Tiff.TIFFReadDirectory(self.tif)

####################################################################################################

def load_to_image(file_name, directory=None):

    """ Create an :class:`Image` instance from a Tiff file.
    """

    tiff_image = TiffImage(file_name)

    if directory is None:
        images = []
        while True:
            images.append(tiff_image.load())
            if not tiff_image.change_to_next_directory():
                break
    
        # compatibility
        if len(images) > 1:
            return images
        else:
            return images[0]

    else:
        if tiff_image.change_directory(directory):
            return tiff_image.load()
        else:
            raise IndexError("Can't change to directory %u" % directory)

####################################################################################################

def write_from_image(image, file_name, compression=True):

    """ Write a Tiff file from an *image* instance. """

    tiff_image = TiffImage(file_name, mode='w')
    tiff_image.write(image, compression)
    
####################################################################################################
#
# End
#
####################################################################################################

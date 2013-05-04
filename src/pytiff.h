/* *********************************************************************************************** *
 * 
 * pylibtiff - A Python binding to libtiff 
 * Copyright (C) Salvaire Fabrice 2013 
 *
 * *********************************************************************************************** */

/* *********************************************************************************************** */

#ifndef __PYTIFF_H__
#define __PYTIFF_H__

/* *********************************************************************************************** */

#include <tiff.h>
#include <tiffio.h>

/* *********************************************************************************************** */

// fixme
int  read_scanline_gray8 (TIFF *tif, uint8 *buffer, tsize_t size);
int write_scanline_gray8 (TIFF *tif, uint8 *buffer, tsize_t size);

int  read_scanline_gray16 (TIFF *tif, uint16 *buffer, tsize_t size);
int write_scanline_gray16 (TIFF *tif, uint16 *buffer, tsize_t size);

int  read_scanline_rgb8 (TIFF *tif, uint8 *buffer, tsize_t size);
int write_scanline_rgb8 (TIFF *tif, uint8 *buffer, tsize_t size);

int  read_scanline_rgb16 (TIFF *tif, uint16 *buffer, tsize_t size);
int write_scanline_rgb16 (TIFF *tif, uint16 *buffer, tsize_t size);

/* *********************************************************************************************** */

#endif /* __PYTIFF_H__ */

/************************************************************************************************* *
 *
 * End
 *
 ************************************************************************************************* */

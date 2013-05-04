/* *********************************************************************************************** *
 * 
 * pylibtiff - A Python binding to libtiff 
 * Copyright (C) Salvaire Fabrice 2013 
 *
 * *********************************************************************************************** */

/* *********************************************************************************************** */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "pytiff.h"

/* *********************************************************************************************** */

/* #define DEBUG 1 */

/* *********************************************************************************************** */

int
read_scanline (TIFF *tif, tdata_t buffer)
{
  uint32 length;
  tsize_t number_of_samples, planar_config;

  TIFFGetField (tif, TIFFTAG_IMAGELENGTH,  &length);
  TIFFGetField (tif, TIFFTAG_PLANARCONFIG, &planar_config);

  if (planar_config == PLANARCONFIG_CONTIG)
    number_of_samples = 1;
  else // PLANARCONFIG_SEPARATE
    TIFFGetField (tif, TIFFTAG_SAMPLESPERPIXEL, &number_of_samples);

  tsize_t scan_line_size = TIFFScanlineSize (tif);
  
#ifdef DEBUG
  printf("Debug read_scanline\n");
  printf("  length %u\n", length);
  printf("  planar_config %u\n", planar_config);
  printf("  number_of_samples %u\n", number_of_samples);
  printf("  scan_line_size %u\n", scan_line_size);
#endif

  // pointer arithmetic
  char *pbuffer = (char *) buffer;
  tsize_t sample, row;
  for (sample = 0; sample < number_of_samples; sample++)
    for (row = 0; row < length; row++)
      {
	if (TIFFReadScanline (tif, (tdata_t) pbuffer, row, sample) < 0)
	  return -1;
	
	pbuffer += scan_line_size * sizeof (char);
      }

  return 0;
}

int
read_scanline_gray8 (TIFF *tif, uint8 *buffer, tsize_t size)
{
  return read_scanline (tif, (tdata_t) buffer);
}

int
read_scanline_gray16 (TIFF *tif, uint16 *buffer, tsize_t size)
{
  return read_scanline (tif, (tdata_t) buffer);
}

int
read_scanline_rgb8 (TIFF *tif, uint8 *buffer, tsize_t size)
{
  return read_scanline (tif, (tdata_t) buffer);
}

int
read_scanline_rgb16 (TIFF *tif, uint16 *buffer, tsize_t size)
{
  return read_scanline (tif, (tdata_t) buffer);
}

/* *********************************************************************************************** */

int
write_scanline (TIFF *tif, tdata_t buffer)
{
  uint32 length;
  tsize_t number_of_samples, planar_config;

  TIFFGetField (tif, TIFFTAG_IMAGELENGTH,  &length);
  TIFFGetField (tif, TIFFTAG_PLANARCONFIG, &planar_config);

  if (planar_config == PLANARCONFIG_CONTIG)
    number_of_samples = 1;
  else // PLANARCONFIG_SEPARATE
    TIFFGetField (tif, TIFFTAG_SAMPLESPERPIXEL, &number_of_samples);

  tsize_t scan_line_size = TIFFScanlineSize (tif);

#ifdef DEBUG
  printf("Debug write_scanline\n");
  printf("  length %u\n", length);
  printf("  planar_config %u\n", planar_config);
  printf("  number_of_samples %u\n", number_of_samples);
  printf("  scan_line_size %u\n", scan_line_size);
#endif
  
  char *pbuffer = (char *) buffer;
  tsize_t sample, row;
  for (sample = 0; sample < number_of_samples; sample++)
    for (row = 0; row < length; row++)
      {
	if (TIFFWriteScanline (tif, (tdata_t) pbuffer, row, sample) < 0)
	  return -1;
	
	pbuffer += scan_line_size * sizeof (char);
      }
  
  return 0;
}

int
write_scanline_gray8 (TIFF *tif, uint8 *buffer, tsize_t size)
{
  return write_scanline (tif, (tdata_t) buffer);
}

int
write_scanline_gray16 (TIFF *tif, uint16 *buffer, tsize_t size)
{
  return write_scanline (tif, (tdata_t) buffer);
}

int
write_scanline_rgb8 (TIFF *tif, uint8 *buffer, tsize_t size)
{
  return write_scanline (tif, (tdata_t) buffer);
}

int
write_scanline_rgb16 (TIFF *tif, uint16 *buffer, tsize_t size)
{
  return write_scanline (tif, (tdata_t) buffer);
}

/************************************************************************************************* *
 *
 * End
 *
 ************************************************************************************************* */

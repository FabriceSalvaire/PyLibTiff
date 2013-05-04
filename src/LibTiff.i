// -*- C++ -*-

/* *********************************************************************************************** *
 * 
 * pylibtiff - A Python binding to libtiff 
 * Copyright (C) Salvaire Fabrice 2013 
 *
 * *********************************************************************************************** */

/* *********************************************************************************************** */

// Warning : there is a mess with uintxx type check pytiffinfo output

/* *********************************************************************************************** */

%module LibTiff

/* *********************************************************************************************** */

%{
#include <stdio.h>

#include <tiff.h>
#include <tiffvers.h>
#include <tiffio.h>

#include "vararg.c"

#include "pytiff.h"
%}

/* *********************************************************************************************** */

%include "std_typedef.i"

// for va_list
%ignore TIFFVGetField;
%ignore TIFFVGetFieldDefaulted;
%ignore TIFFVSetField;

%include <tiff.h>
// %include <tiffconf.h>
%include <tiffconf-64.h>
%include <tiffvers.h>
%include <tiffio.h>

%include "vararg.h"

/* *********************************************************************************************** */
/*
 * Numpy interface
 *
 */

%{
#define SWIG_FILE_WITH_INIT
%}

%include "numpy.i"

%init %{
import_array();
%}

// fixme: uint8
%apply (unsigned char* IN_ARRAY1, int DIM1) {(uint8* buffer, tsize_t size)};
%apply (unsigned char* IN_ARRAY1, int DIM1) {(uint8* dst_buffer, tsize_t dst_size)};

// fixme: uint16
%apply (unsigned short* IN_ARRAY1, int DIM1) {(uint16* buffer, tsize_t size)};
%apply (unsigned short* IN_ARRAY1, int DIM1) {(uint16* src_buffer, tsize_t src_size)};

// fixme: uint8
%apply (unsigned char* IN_ARRAY2, int DIM1, int DIM2) {(uint8* buffer,
							tsize_t number_of_rows, tsize_t number_of_columns)};

// fixme: uint16
%apply (unsigned short* IN_ARRAY2, int DIM1, int DIM2) {(uint16* buffer,
							 tsize_t number_of_rows, tsize_t number_of_columns)};

%include "pytiff.h"

/************************************************************************************************* *
 *
 * End
 *
 ************************************************************************************************* */

####################################################################################################

project(pylibtiff)

set(PYLIBTIFF_VERSION_MAJOR 0)
set(PYLIBTIFF_VERSION_MINOR 1)
set(PYLIBTIFF_VERSION_PATCH 0)

set(PYLIBTIFF_VERSION ${PYLIBTIFF_VERSION_MAJOR}.${PYLIBTIFF_VERSION_MINOR}.${PYLIBTIFF_VERSION_PATCH})

####################################################################################################

# check cmake version
cmake_minimum_required(VERSION 2.8)

if(COMMAND cmake_policy)
  cmake_policy(SET CMP0003 NEW)
endif(COMMAND cmake_policy)

####################################################################################################

if(CMAKE_SYSTEM_NAME MATCHES "Linux")
  set(CMAKE_SWIG_FLAGS ${CMAKE_SWIG_FLAGS_COMMON} -DSystemLinux)
endif(CMAKE_SYSTEM_NAME MATCHES "Linux")

if(CMAKE_SYSTEM_NAME MATCHES "Windows")
  set(CMAKE_SWIG_FLAGS ${CMAKE_SWIG_FLAGS_COMMON} -DSystemWindows)
endif(CMAKE_SYSTEM_NAME MATCHES "Windows")

####################################################################################################
#
# Find Libraries
#

include(FindTIFF)

####################################################################################################
#
# Python
#

include(FindPythonLibs)

##################################################
#
# Numpy
#

find_path(NUMPY_INCLUDE_PATH
  NAMES "numpy/arrayobject.h"
  PATHS "${PYTHON_PREFIX}/lib/python${PYTHON_VERSION}/site-packages/numpy/core/include"
)
mark_as_advanced(NUMPY_INCLUDE_PATH)
include_directories(${NUMPY_INCLUDE_PATH})

####################################################################################################
#
# Swig
#

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
include_directories(${PYTHON_INCLUDE_PATH})
set(CMAKE_SWIG_FLAGS_COMMON "-Wall")

####################################################################################################
#
# Sub directories
#

add_subdirectory(src)

####################################################################################################
#
# End
#
####################################################################################################

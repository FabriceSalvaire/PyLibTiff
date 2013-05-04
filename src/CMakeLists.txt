####################################################################################################
# 
# pylibtiff - A Python binding to libtiff 
# Copyright (C) Salvaire Fabrice 2013 
# 
####################################################################################################

####################################################################################################
#
# tiff.h
#

# Expand tiff.h with C Pre-Processor to tiff.local.h
execute_process(
  COMMAND cpp ${TIFF_INCLUDE_DIR}/tiff.h
  OUTPUT_FILE ${CMAKE_CURRENT_BINARY_DIR}/tiff.local.h)

####################################################################################################
#
# Include directories
#

include_directories(${CMAKE_CURRENT_SOURCE_DIR})

####################################################################################################
#
# SWIG Module
#

# set_source_files_properties(LibTiff.i PROPERTIES CPLUSPLUS ON)
set_source_files_properties(LibTiff.i PROPERTIES SWIG_FLAGS "-cpperraswarn")
SET(SWIG_MODULE_LibTiff_EXTRA_DEPS pytiff.h vararg.h vararg.c)
swig_add_module(LibTiff python LibTiff.i pytiff.c)
swig_link_libraries(LibTiff ${PYTHON_LIBRARIES} ${TIFF_LIBRARIES})

if(CMAKE_SYSTEM_NAME MATCHES "Windows")
  SET_TARGET_PROPERTIES(
    ${SWIG_MODULE_LibTiff_REAL_NAME}
    PROPERTIES SUFFIX .pyd)
endif(CMAKE_SYSTEM_NAME MATCHES "Windows")

####################################################################################################
#
# Install
#

install(TARGETS ${SWIG_MODULE_LibTiff_REAL_NAME}
  LIBRARY DESTINATION lib/python${PYTHON_VERSION})

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/LibTiff.py
  DESTINATION lib/python${PYTHON_VERSION})

####################################################################################################
#
# Clean
#

set_directory_properties(PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES "LibTiff.pyc")

####################################################################################################
#
# End
#
####################################################################################################

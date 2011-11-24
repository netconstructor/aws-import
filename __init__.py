"""
/***************************************************************************
Name			 	 : AWS Import
Description          : Download and import AWS Data from various automated sources
Date                 : 24/Nov/11 
copyright            : (C) 2011 by Arunmozhi
email                : aruntheguy@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "AWS Import" 
def description():
  return "Download and import AWS Data from various automated sources"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load awsimport class from file awsimport
  from awsimport import awsimport 
  return awsimport(iface)

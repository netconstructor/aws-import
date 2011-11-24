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
"""
from PyQt4 import QtCore, QtGui 
from Ui_awsimport import Ui_awsimport
# create the dialog for awsimport
class awsimportDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_awsimport ()
    self.ui.setupUi(self)
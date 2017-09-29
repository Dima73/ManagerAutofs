#
#  Manager Autofs
#
#  $Id$
#
#  Coded by ims (c) 2017
#  Support: openpli.org
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#

# for localized messages
from . import _

from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigSubsection, ConfigYesNo

config.plugins.mautofs = ConfigSubsection()
config.plugins.mautofs.extended_menu = ConfigYesNo(default = False)

def main(session, **kwargs):
	import ui
	session.open(ui.ManagerAutofsMasterSelection)

def Plugins(**kwargs):
	name = _("Manager Autofs")
	descr = _("Manage autofs files and conection")
	list = [PluginDescriptor(name=name, description=descr, where = PluginDescriptor.WHERE_PLUGINMENU, icon = 'plugin.png', fnc = main)]
	if config.plugins.mautofs.extended_menu.value:
		list.append(PluginDescriptor(name=name, description=descr, where = PluginDescriptor.WHERE_EXTENSIONSMENU, icon = 'plugin.png', fnc = main))
	return list

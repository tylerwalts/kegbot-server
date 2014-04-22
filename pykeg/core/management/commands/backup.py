# Copyright 2014 Bevbot LLC, All Rights Reserved
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.

import os

from django.core.files.storage import get_storage_class
from django.core.management.base import NoArgsCommand
from pykeg.core import backup

class Command(NoArgsCommand):
    help = u'Creates a zipfile backup of the current Kegbot system.'

    def handle(self, **options):
        location = backup.backup()
        storage = get_storage_class()()
        if hasattr(storage, 'location'):
            location = os.path.join(storage.location, location)
        print 'Backup complete! Backup file:\n  {}'.format(location)

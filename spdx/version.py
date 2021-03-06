# Copyright 2014 Ahmed H. Ismail

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import re


class Version(object):

    """Version number composed of major and minor.
       Fields:
       major: Major number, int.
       minor: Minor number, int.
    """
    VERS_STR_REGEX = re.compile(r'(\d+)\.(\d+)')

    def __init__(self, major=1, minor=2):
        super(Version, self).__init__()
        self.major = major
        self.minor = minor

    @classmethod
    def from_str(cls, value):
        """Constructs a Version from a string.
        Returns None if string not in N.N form where N represents a 
        number.
        """
        m = cls.VERS_STR_REGEX.match(value)
        if m is not None:
            return cls(int(m.group(1)), int(m.group(2)))
        else:
            return None

    def __cmp__(self, other):
        if self.major == other.major:
            return self.minor - other.minor
        elif self.major < other.major:
            return -1
        else:
            return 1

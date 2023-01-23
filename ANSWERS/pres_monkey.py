#!/usr/bin/python

from president import President


def fn(self):
    return '%s %s' % (self.first_name, self.last_name)


setattr(President, 'get_full_name', fn)
# or just
# President.getFullName = fn

abe = President(16)
print(abe.get_full_name())

millard = President(13)
print(millard.get_full_name())

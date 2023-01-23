#!/usr/bin/python

from president import President


@property
def fn(self):
    return '%s %s' % (self.first_name, self.last_name)


setattr(President, 'full_name', fn)
# or just
# President.getFullName = fn

abe = President(16)
print(abe.full_name)

millard = President(13)
print(millard.full_name)

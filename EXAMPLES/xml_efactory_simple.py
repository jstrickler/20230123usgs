#
import lxml.etree as ET
from lxml.builder import E  # import E object

xml = (
    E.animals(  # use E to create nested tags
        E.animal('wombat', species="Vombatus ursinus"),
        E.animal('bushbaby', species="Galago senegalensis")
    )
)

print(ET.tostring(xml, pretty_print=True).decode())

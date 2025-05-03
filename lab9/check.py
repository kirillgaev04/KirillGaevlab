from lxml import etree

try:
    xml_file = 'library.xml'
    xsd_file = 'library.xsd'

    with open(xml_file, 'rb') as f:
        xml_doc = etree.parse(f)

    with open(xsd_file, 'rb') as f:
        schema_root = etree.parse(f)
        schema = etree.XMLSchema(schema_root)

    schema.assertValid(xml_doc)
    print("XML документ валиден!")

except etree.DocumentInvalid as e:
    print("Ошибка валидации:", e)
except Exception as e:
    print("Ошибка:", e)

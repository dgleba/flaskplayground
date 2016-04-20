from sqlalchemy.orm import class_mapper
import collections

# structure returned by get_metadata function.
MetaDataTuple = collections.namedtuple("MetaDataTuple", 
        "coltype, colname, default, m2m, nullable, uselist, collection")


def get_metadata_iterator(class_):
    for prop in class_mapper(class_).iterate_properties:
        name = prop.key
        if name.startswith("_") or name == "id" or name.endswith("_id"):
            continue
        md = _get_column_metadata(prop)
        if md is None:
            continue
        yield md


def get_column_metadata(class_, colname):
    prop = class_mapper(class_).get_property(colname)
    md = _get_column_metadata(prop)
    if md is None:
        raise ValueError("Not a column name: %r." % (colname,))
    return md


def _get_column_metadata(prop):
    name = prop.key
    m2m = False
    default = None
    nullable = None
    uselist = False
    collection = None
    proptype = type(prop)
    if proptype is ColumnProperty:
        coltype = type(prop.columns[0].type).__name__
        try:
            default = prop.columns[0].default
        except AttributeError:
            default = None
        else:
            if default is not None:
                default = default.arg(None)
        nullable = prop.columns[0].nullable
    elif proptype is RelationshipProperty:
        coltype = RelationshipProperty.__name__
        m2m = prop.secondary is not None
        nullable = prop.local_side[0].nullable
        uselist = prop.uselist
        if prop.collection_class is not None:
            collection = type(prop.collection_class()).__name__
        else:
            collection = "list"
    else:
        return None
    return MetaDataTuple(coltype, str(name), default, m2m, nullable, uselist, collection)
    
import pandas
import pyarrow

def to_arrow(source):
    if source == None:
        return None

    if isinstance(source, pyarrow.Table):
        return source

    if isinstance(source, pandas.DataFrame):
        return pyarrow.Table.from_pandas(source)

    raise Exception('unsupported data source type: %s' % type(source))

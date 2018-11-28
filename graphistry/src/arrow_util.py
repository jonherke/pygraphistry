import pyarrow as arrow

# Consider where to move to_buffer
def table_to_buffer(table: arrow.Table) -> arrow.Buffer:
    sink = arrow.BufferOutputStream()
    writer = arrow.RecordBatchStreamWriter(sink, table.schema)
    writer.write_table(table)
    return sink.getvalue()
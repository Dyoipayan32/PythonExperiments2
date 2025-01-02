def test_table_data(table_cursor):
    table_cursor.execute('select id, name from items')
    fetched_data = table_cursor.fetchall()
    assert fetched_data == [(1, "books")]

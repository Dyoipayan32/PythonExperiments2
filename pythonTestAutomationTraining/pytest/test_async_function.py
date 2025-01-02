import asyncio
import pytest
# Imports aiomysql, an asynchronous library for accessing MySQL databases.
# It provides a non-blocking way to interact with MySQL databases using asyncio.
import aiomysql


@pytest.fixture
async def db():
    '''
    Defines an asynchronous function db.
    This function will asynchronously set up a database connection and cleanup after tests.
    :return: connection object when the connection is established
    '''
    # The await keyword is used to pause the function's execution until the connection is established.

    conn = await aiomysql.connect(host='localhost', port=3306,
                                  user='user', password='password', db='test_db')
    # After setting up the connection, it yields the connection object conn.
    # This makes the connection available to the tests that use this fixture.
    # This line effectively splits the fixture into setup and teardown phases.
    yield conn

    conn.close()


@pytest.mark.asyncio
# A decorator that marks the function as an async test,
# enabling pytest to treat it as an asyncio-based coroutine.
# This allows the test to be run within an event loop.
async def test_db_query(db):
    '''
    Defines an asynchronous test function that takes a db parameter,
    which is the database connection provided by the db fixture.
    :param db:
    :return:
    '''
    # Below line asynchronously manages a database cursor.
    # This line retrieves a cursor object from
    # the connection db and ensures proper acquisition and release of the cursor resource.
    async with db.cursor() as cursor:
        await cursor.execute("SELECT 42;")
        result = await cursor.fetchone()
        assert result == (42,)

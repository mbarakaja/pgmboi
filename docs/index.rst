Welcome to pgmboi
=================

Dump a PostgreSQL database schema for easy versioning.

Installation
------------

1.  Clone the repository
2.  Run the next command in a virtual or main python interpreter, as you
    prefer::

      $ pip install --editable .

The ``pgmboi`` command should be accesible now from the **terminal**.


Usage
-----

You have two ways to start a successfull connection to the database running
``pgmboi`` application in the terminal; passing all basic parameters
in the command line or creating a ``config.json`` file with all values
needed.

If you are going to pass the arguments through the command line, provide at least 
a ``--database`` and ``--password`` arguments and then pass the command
(**dump** or **restore**) that you want to run like following::

    $ pgmboi --database mydb --password 123 dump

To see all arguments available run in the terminal `pgmboi --help`::

    $ pgmboi --help
    Usage: pgmboi [OPTIONS] COMMAND [ARGS]...
    
      Dump a PostgreSQL database schema for easy revision control.
    
    Options:
      --host TEXT      database server host, default: localhost
      --port TEXT      connection port number, default: 5432
      --database TEXT  the name of the database
      --user TEXT      user name, default: postgres
      --password TEXT  password
      --help           Show this message and exit.
    
    Commands:
      dump
      restore


Otherwise, you can create a ``config.json`` file, containing at minimun
the values for ``database`` and ``password`` parameters. host, port
and user have default values, so you can ommit if you want.::

    {
      "database": "mydb",
      "password": "123"
    }

**pgmboi** will look for the file in the current working directory and
use all the values inside it. So you can run the application without arguments::

    $ pgmboi dump

If you pass an connection argument in the command line and pgmboi find
a ``config.json`` in the working directory, pgmboi will use the values
passed in the command line over the ``config.json`` file values


The dump command
----------------

Pass this command after all parameters to dump the specified database to
the filesystem. 

The application will being to create a file called **__header__.sql**, that will
contain all the global definitions. 

Then, for instance, if your database has five schemas, pgmboi will create one
folder per schema with the name of the schema.

Finally, inside of each folder (schema) the aplication proceeds to dump the
functions in a **__functions__.sql** file, the tables in their own files named
with the table name and a **relations.json** file that register dependencies
between tables.

The final result will look like::

    __header__.sql
    schema_name1/
        relations.json
        __functions__.sql
        table1.sql
        table2.sql
    schema_name2/
        relations.json
        __functions__.sql
        table1.sql
        table2.sql
    schema_name3/
        relations.json
        __functions__.sql
        table1.sql
        table2.sql


The restore command
-------------------

Run this command in the directory where you dump your database, where the
**__header__.sql** is located. Pass all the parameters for the database
connection or place a **config.json** with the necessary parameters.::

    $ pgmboi --database mydb --password 123 restore


.. warning:: Don't restore on an existing database. Create a new empty database and restore on it.


Modules in package
------------------

.. toctree::
   :maxdepth: 4

   pgmboi




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


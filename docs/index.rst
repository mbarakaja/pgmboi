Welcome to pgmboi
=================

Dump a PostgreSQL database schema for easy revision control.

Usage
-----

You have two ways to start a sucefull connection to the database running
``pgmboi`` application in the terminal; passing all basic parameters
in the command line or creating a ``config.json`` file with all values
needed.

If you will pass the arguments through the command line, provide at least 
a ``--database`` and ``--password`` arguments and then pass the task that 
you want to start like following::

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


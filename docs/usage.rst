========
Usage
========

There are two ways to use Jetstream: either to perform some tasks on your data
using the 'jet' command-line tool provided by Jetstream, or as a part of your
own application.

In either case, Jetstream must first be configured, using YAML_. The
configuration tells Jetstream what components to instantiate and how, and how to
combine them into one or more pipes runnable by Jetstream.

Configuring Jetstream
-----------------------

The YAML_ configuration consists of two or more sections declaring the
components to be used (at least an :term:`Input` and :term:`Output`) and a
section declaring the :term:`pipes`.

Configuring components
~~~~~~~~~~~~~~~~~~~~~~~

Each :term:`component` is configured under a component type section which is
either 'inputs', 'introspectors', 'transformers', or 'outputs'. Under the type
section, each component is listed as:

.. code-block:: yaml

  <component title>: &<component_id>
    description: <some description here>
    use: <a fully-qualified Python dotted name of the factory>

The description field is optional but recommended. Also note that the
`component_id` can not include spaces.

An example configuration of an :term:`Input` :term:`component`:

.. code-block:: yaml

   inputs:
     my MySQL data source: &sqlsource
       description: an example MySQL data source
       use: mypackage.mymodule.get_my_sql_source


Configuring pipes
~~~~~~~~~~~~~~~~~~~

Each :term:`pipe` is configured under 'pipes' section, and is of the form:

.. code-block:: yaml

  <pipe title>: &<pipe_id>
    description: <some description here>
    use: <a fully-qualified Python dotted name of the factory>

An example configuration of a :term:`pipe` with two components:

.. code-block:: yaml

   pipes:
      example pipe:
         - *sqlsource
         - *csvoutput


Full example
~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the full configuration file from Jetstream tests:

.. literalinclude:: ../tests/config.yaml

Using the Jetstream cli
------------------------

.. todo:: write the cli & docs

Embedding Jetstream
--------------------------

To use Jetstream in your own project::

	import jetstream

.. todo:: explain how to embed Jetstream


.. _YAML: http://en.wikipedia.org/wiki/YAML
Extending Jetstream
===============================

The primary way of extending Jetstream is by adding new components, which is
relatively easy. If you're not sure what kind of component to develop, take a
look at :doc:`cases`.

Architecture overview
-------------------------

There are four types of components: :term:`Input`, :term:`Inspector`,
:term:`Transformer` and :term:`Output`. The following diagram illustrates how
they fit into the the overall architecture.

.. figure:: images/overview.png

Note that any number of components can be freely arranged into a pipe, as long
as it is started by an :term:`Input`, and ends in an :term:`Output`.

For more on using components, see :doc:`cases`.

To create a component, Jetstream needs to be able to call a component factory,
passing it two parameters:

 1. configuration settings (a mapping)
 2. the data :term:`streamer` (an iterable)

It is the responsibility of the factory to return the component; all that is
required of the component that it implements the iterator protocol, producing
the :term:`data stream`.

So in practice, **a simple Python generator function accepting two parameters
is all that is needed to implement a component**.

Plugin registration API
------------------------------

Jetstream uses the standard setuptools entry points API for pluggable component
registrations. Each entry point is expected to resolve to a component factory
that is a callable accepting two parameters:

 1. configuration settings (a mapping)
 2. the data :term:`streamer` (an iterable)

The entry points to register under are as follows, one for each component type:

 - jetstream.input
 - jetstream.inspector
 - jetstream.transformer
 - jetstrem.output

Here is an example entry point declaration to go into your package's `setup.py`:

.. code-block:: python

    entry_points = {
        'jetstream.input': [
            'NoSQLInput = jetstream.nosqlinput.component:get_component'
        ]
    },

This would register the `get_component` function found in module
`jetstream.nosqlinput.component` as the factory for an Input component called
"NoSQLInput".

Implementing components
--------------------------

Component basics
~~~~~~~~~~~~~~~~~~~

Components can be any callables that return an iterator; it is suggested a
generator be used for that.

.. _developing-inputs:

Input components
~~~~~~~~~~~~~~~~~~~

The component should be able to handle the data stream regardless of how many
records it provides. It should also handle any problems in network connectivity
or errors originating from the data source.

since the number of records that can be read may be limited
in many ways; for example by the data source:

 - data may contain a fixed number of records by nature
 - there may be usage limits to data volume or time of day
 - there is an error at data source

... or by user context:

 - data may be limited by authentication > authorization
 - only a subset of available data is requested by query terms
 - user may want a smaller number of records than what is available

It is of course also possible that data is available ad infinitum.

.. todo:: capability declarations related to stream reading abilities

.. _developing-inspectors:

Inspector components
~~~~~~~~~~~~~~~~~~~~~~

.. _developing-transformers:

Transformer components
~~~~~~~~~~~~~~~~~~~~~~

.. _developing-outputs:

Output components
~~~~~~~~~~~~~~~~~~~~~~

and an Output is
allowed to return an exhausted iterator.




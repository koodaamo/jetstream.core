===============================
Jetstream
===============================

.. image:: https://badge.fury.io/py/jetstream.png
    :target: http://badge.fury.io/py/jetstream

.. image:: https://travis-ci.org/koodaamo/jetstream.png?branch=master
        :target: https://travis-ci.org/koodaamo/jetstream

.. image:: https://pypip.in/d/jetstream/badge.png
        :target: https://crate.io/packages/jetstream?version=latest

Jetstream provides a data batch processing tool and simple, convenient framework
for data integration applications. It is driven by a small core, Python plugins
and YAML configuration, which together provide the glue to hook incoming and
outgoing data streams into any Python application and process the data in
various ways.

It does not enforce a particular event loop, http server or client library,
SQL library, ORM or such. Instead, Jetstream can be extended by following kinds
of data processing components:

 - inputs for reading data from various sources
 - inspectors for e.g. checking data conformity
 - transformers for modifying data and/or creating stuff from it
 - outputs for receiving data and possibly writing it somewhere else

Some common built-in components are included and it's easy to write more.

To hook components together into a data processing sequence, Jetstream provides
a pipeline construct and facilities for running the pipeline to actually process
some data.

Both the components and the pipelines are configured using YAML. **No
programming is required to process data using Jetstream**. To make most of it,
you may want to extend Jetstream and incorporate it into your own app, though.

* Free software: GPL3 licensed
* Documentation: http://jetstream.rtfd.org.

Features
--------

* TODO

===============================
Overview
===============================

.. image:: https://badge.fury.io/py/jetstream.png
    :target: http://badge.fury.io/py/jetstream

.. image:: https://travis-ci.org/koodaamo/jetstream.png?branch=master
        :target: https://travis-ci.org/koodaamo/jetstream

.. image:: https://pypip.in/d/jetstream/badge.png
        :target: https://crate.io/packages/jetstream?version=latest

Jetstream provides a configurable data batch processing tool and a framework
for data integration applications, ie. hooking incoming and
outgoing data streams into any Python application and processing the data in
various ways.

It does not enforce a particular event loop, http server or client library,
SQL library, ORM or such. Those are all outside its scope. Instead, Jetstream
can be extended by following kinds of data processing components:

- inputs for reading data from various sources
- inspectors for e.g. checking data conformity
- transformers for modifying data and/or creating stuff from it
- outputs for receiving data and possibly writing it somewhere else

Some common built-in components are included and it's easy to write more.
Jetstream then provides facilities for running data processing pipelines
composed of the components, by the configuration.

Both the components and the pipelines are configured using YAML. **No
programming is required to process data using Jetstream**. On the other hand,
Jetstream is easy to extend and/or incorporate into your own app.

* Free software: GPL3 licensed
* Documentation: http://jetstream.rtfd.org.


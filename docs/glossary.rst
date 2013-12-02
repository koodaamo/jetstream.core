.. _glossary:

Glossary
========

.. glossary::

   data stream
      collection of data records produced and consumed by
      :term:`data components`

   data source
   data destination
   data endpoint
      where you get data from or write to: SQL database, CSV file, REST api ...

   data components
   data component
   component
      Components are the basic building blocks of Jetstream :term:`pipes`. There
      are four types of (data) components: :term:`Input`, :term:`Inspector`,
      :term:`Transformer` or :term:`Output` components.

   data pipe
   pipes
   pipe
      a "master" component composed of several :term:`data components` piped
      together and run in order by a Jetstream :term:`Streamer`

   streamer
        Part of Jetstream framework that:

        #. composes a :term:`pipe` from two or more :term:`components`
        #. adds instrumentation in between every 'slot' or 'connection' between
           two components
        #. runs the pipe, indexing received records, performing logging and
           producing a report of the run

   Input
      a :term:`component` reading data from an :term:`data source`, for example
      from an SQL database

   Inspector
      a :term:`component` that analyses the data stream and performs actions
      depending on data content; for example a validating Introspector can
      raise an error upon seeing incomplete data

   Transformer
      a :term:`component` that modifies a :term:`data stream`

   Output
      a :term:`component` writing to a :term:`data source`, for example to a CSV
      file


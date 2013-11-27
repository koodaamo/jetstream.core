Data component use cases
==============================

Each component type has clearly defined roles with responsibilities and
constraints that should be followed in order to fully benefit from functionality
offered by Jetstream.

Here are some notes on how to choose the right component type for each
use case, and how to combine components to achieve desired result when it's not
possible to get that from a single component.

Input components
-----------------

An :term:`Input` **connects to a data source and produces a data
stream**. It does nothing else. Given that, an input component is typically set
as the first component of the pipe. In that case, there is no :term:`data pipe`
passed to it as an input parameter.

However, if a pipe is configured so that the input component is not the first
one, it receives a data pipe, and can then be used to implement following
actions on received data:

* append = add more records to the end of :term:`data stream`
* mix = add records interleaved with existing records

An input MAY add records that differ in format from those passed to it; those
records can later be separated, if needed, using the input id associated with
each data item.

.. todo:: add reference to retrieving and using input id label

An input MAY NOT modify the structure or content of data passed to it. To modify
data in any way, always use a transformer.

For developing inputs, see :ref:`developing-inputs`.

Inspector components
---------------------

An :term:`Inspector` **reads the data but does not touch (or output) it**.
However it has **control over the processing** of the :term:`data stream`,
and may include parts of data within its own non-data output. An inspector can
thus perform for example one or more of the following actions:

* validate data
* flag it
* log events
* alert user
* summarize data
* analyze it

For developing inspectors, see :ref:`developing-inspectors`.

Transformer components
-----------------------

:term:`Transformer` modifies data and passes it on, and may also drop records.
Thus a transformer can be naturally used to:

- rearrange fields
- filter out data records
- convert data from a type to another
- modify data labels and/or values

A transformer may also add to the data. It is however limited to using the data
it has received as input, including any information available within the
Jetstream system, such as configuration information passed to the transformer.
It may not fetch data on its own from any other, external data source.

For developing Transformers, see :ref:`developing-transformers`.

Output components
------------------

An :term:`Output` **connects to a :term:`data destination` and writes data to
it**. So the end of the pipe always has some sort of Output configured, even if
it is simply some code that reads and prints out the data, for example.

When not configured as pipe end, an output component can be used to:

* copy data to another destination

.. todo:: add loop-back data source/destination functionality to Jetstream

For developing Outputs, see :ref:`developing-outputs`.

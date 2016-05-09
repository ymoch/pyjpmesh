Pyjpmesh
========

Japan grid square code (JIS X 0410) utility for Python.

.. image:: https://travis-ci.org/ymoch/pyjpmesh.svg?branch=master
    :target: https://travis-ci.org/ymoch/pyjpmesh
.. image:: https://coveralls.io/repos/github/ymoch/pyjpmesh/badge.svg?branch=master
    :target: https://coveralls.io/github/ymoch/pyjpmesh?branch=master


Features
--------

- Supports the meshes below.
    - 1st mesh (*jpmesh.FirstMesh* class, about 80 km square).
    - 2nd mesh (*jpmesh.SecondMesh* class, about 10 km square).
    - 3rd mesh (*jpmesh.ThirdMesh* class, about 1 km square).
    - 1/2 mesh (*jpmesh.HalfMesh* class, about 500 m square).
    - 1/4 mesh (*jpmesh.QuarterMesh* class, about 250 m square).
    - 1/8 mesh (*jpmesh.OneEighthMesh* class, about 125 m square).
- Supports the calculations below.
    - Mesh border coordinates from mesh codes.
    - Mesh codes from coordinates.
- Consisted of only one file and depends on no other libraries,
  which enable you to use it portably.


Installation
------------

Choose one from the following.

- Run ``pip install pyjpmesh``.
- Put *jpmesh.py* on your project.


Tutorial
--------

Here is an example to get the 1st mesh (about 8 km square) code
that a given point belongs to.

.. code-block:: python

  from jpmesh import Angle, Coordinate, FirstMesh

  coordinate = Coordinate(
      lon=Angle.from_degree(140.0), lat=Angle.from_degree(35.0))
  mesh = FirstMesh.from_coordinate(coordinate)
  print mesh.code # '5240'

Here is another example to get the center point of the given mesh.

.. code-block:: python

  from jpmesh import parse_mesh_code

  mesh = parse_mesh_code('5339')
  mesh_center = mesh.south_west + (mesh.size / 2.0)
  print mesh_center.lon.degree, mesh_center.lat.degree # 139.5 35.667

To use other mesh classes (SecondMesh, ThirdMesh, etc.),
use those classes instead of FirstMesh.

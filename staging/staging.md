---
title: Staging
layout: default
nav_order: 5
---

This is a place to stage tutorials/examples/etc while platform is being built.


## Table of Contents

1. TOC
{:toc}


# How-To

## Time series

### Series difference

Given a time series of observations, calculate the differences between observations at a regular step. Similar to: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html

*Author: Gennadii Donchyts*

https://code.earthengine.google.com/35f681f9b77978866d02b24f32aa912d

TODO: could be simplifed for brevity. 



## Landsat

### Correction

**Minnaert terrain correction**

Implementation where Minnaert constant k is calculated per pixel as a function of slope.

TODO: Sun azimuth and zenith angles are taken from image metadata, so represent nadir position and are held constant. Could adjust for every pixel.

[GEE JS](https://code.earthengine.google.com/1fcc034eb3014d7606eec467241dc1da){: .btn }

**Landsat7 SLC-off gap filling**

[GEE JS](https://code.earthengine.google.com/078556a80eee46a8330b2079cd4c9dca){: .btn .btn-outline }



TODO: 


## Feature Collection

**Generate regular grid intersecting a geometry**

*Author: Gennadii Donchyts*

https://code.earthengine.google.com/ff50a3e4745b1e732b1b7ac8a12623b6

Also implemented in `users/gena/packages:grid` library

```js
var g = require('users/gena/packages:grid')
var dx = 0.45
var dy = 0.45
var grid = g.generateGridForGeometry(region.bounds(), dx, dy)
```

Example of its use in dividing an image for export

*Author: marortpab*

https://code.earthengine.google.com/3a413327f67acc350bec59ba5ce1cb3c

TODO: make reproducable - calls user asset(s)


## Charts

### Scatterplot

**3-band**

*Author: Gennadii Donchyts*

https://code.earthengine.google.com/252fda4ed0340c3e926096b01668576b

**2-band with color for group**

*Author: barbosaale*

https://code.earthengine.google.com/41f4c83698112405fcaf591ed9145a25

TODO: make reproducable - calls user asset(s)


## UI

### ui.Label

**Adjust the position of a label within a panel using `textAlign` style property**

https://code.earthengine.google.com/b4c03edade9ab3509d0e8a9b5a4e09b1

# Apps

## Forest Change



## Atmosphere









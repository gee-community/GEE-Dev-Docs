---
title: Topic 2
layout: default
parent: Specific
grand_parent: Method
nav_order: 2
tags: [cloud masking, palette]
---

This is specific methods sub-sub topics

1. TOC
{:toc}

### Example 1

This is a test of labels - use these for search tags

Landsat 
{: .label }

Cloud masking 
{: .label } 

Image collection building 
{: .label }

Here is some code using Jekyll’s built-in syntax highlighting with Rouge

```js
// Load some raster data: CONUS mean daily max temperature for January 2010
var tmax = ee.Image('OREGONSTATE/PRISM/AN81m/201001').select('tmax');

// Get a palette: a list of hex strings
var palettes = require('users/gena/packages:palettes');
var palette = palettes.misc.tol_rainbow[7];
 
// Display max temp with defined palette stretched between selected min and max
Map.addLayer(tmax, {min: -11, max: 25, palette: palette}, 'tmax');
```
[Try live](https://code.earthengine.google.com/){: .btn }

<a href="{{ site.github.repository_url }}/tree/master/{{ page.path }}">Edit this</a>

### Example 2

### Example 3

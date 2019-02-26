---
title: Date Ranges
layout: default
parent: API
nav_order: 1
---

# Date Ranges
{: .no_toc }

A dateRange is an Earth Engine parameter object that represents the span of time from the beginning of “start” date onward 
until (but not including) the beginning of an “end” date. DateRanges can be processed by using operations of the types 
listed below, which vary according to the nature of that processing. Each operation name is linked to a separate 
page describing that operation.

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

<!------------------------------------------------------------------------------------------------------------------------------>
<!---Creating DateRanges-------------------------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------------------------------------------------>


## Creating DateRanges


### ee.DateRange
- Creates a DateRange object extending from a specified starting date to a specified stopping date and including both of those dates.

**Syntax**

*Javascript*

```
newDateRange = ee.DateRange( startingDate, stoppingDate, timeZone )
```

- *newDateRange* is The new DateRange.

**Example**

*Javascript*

```javascript
var TheDATERANGE = ee.DateRange( '1950-12-25', '1990-07-16' );
print( TheDATERANGE );
```


<!------------------------------------------------------------------------------------------------------------------------------>


### dateRange.isUnbounded 
- Creates a new Boolean set to true (only) if a specified dateRange contains all possible dates.

**Syntax**

*Javascript*

```
newBoolean = oldDateRange.isUnbounded( )
```

- *newBoolean* is the new Boolean.
- *oldDateRange.isUnbounded( )* is the specified dateRange.

**Example**

*Javascript*

```javascript
var TheDATERANGE = ee.DateRange.unbounded( );
print( TheDATERANGE );
```


<!------------------------------------------------------------------------------------------------------------------------------>
<!---Transforming DateRanges---------------------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------------------------------------------------>


## Transforming DateRanges


#### dateRange.union
- Creates a new dateRange encompassing the union of two specified dateRanges.

**Syntax**

*Javascript*

```
newDateRange = 1stDateRange.union( 2ndDateRange )
```

- *newDateRange* is The new DateRange.
- *1stDateRange.union* is the first specified dateRange.
- *2ndDateRange* is the first specified dateRange.

**Example**

*Javascript*

```javascript
var MozartDATERANGE     = ee.DateRange( '1756-1-27', '1791-12-5' );
var BeethovenDATERANGE  = ee.DateRange( '1770-12-17', '1827-3-26' );
var TheirTotalDATERANGE = MozartDATERANGE.union( BeethovenDATERANGE );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'DateRange for Beethoven', BeethovenDATERANGE );
print( 'DateRange when Either Was Alive', TheirTotalDATERANGE );
```


<!------------------------------------------------------------------------------------------------------------------------------>


#### dateRange.intersection
- Creates a new dateRange encompassing the intersection of two specified dateRanges.

**Syntax**

*Javascript*

```
newDateRange = 1stDateRange.intersection( 2ndDateRange )
```

- *newDateRange* is The new DateRange.
- *1stDateRange.intersection* is the first specified dateRange
- *2ndDateRange* is the second specified dateRange.

**Example**

*Javascript*

```javascript
var MozartDATERANGE      = ee.DateRange( '1756-1-27', '1791-12-5' );
var BeethovenDATERANGE   = ee.DateRange( '1770-12-17', '1827-3-26' );
var TheirSharedDATERANGE = MozartDATERANGE.intersection( BeethovenDATERANGE );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'DateRange for Beethoven', BeethovenDATERANGE );
print( 'DateRange when Both Were Alive', TheirSharedDATERANGE );
```


<!------------------------------------------------------------------------------------------------------------------------------>
<!---Querying DateRanges-------------------------------------------------------------------------------------------------------->
<!------------------------------------------------------------------------------------------------------------------------------>


## Querying DateRanges


### dateRange.start
- Creates a new date set to the (inclusive) start of a specified dateRange.

**Syntax**

*Javascript*

```
newDate = oldDateRange.start( )
```

- *newDate* is The new Date.
- *oldDateRange.start( )* is the specified dateRange.

**Example**

*Javascript*

```javascript
var MozartDATERANGE = ee.DateRange( '1756-1-27', '1791-12-5' );
var MozartBirthDATE = MozartDATERANGE.start( );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'So he was born on the following date.', MozartBirthDATE );
```


<!------------------------------------------------------------------------------------------------------------------------------>


### dateRange.end
- Creates a new date set to the (exclusive) end of a specified dateRange.

**Syntax**

*Javascript*

```
newDate = oldDateRange.end( )
```

- *newDate* is the new Date.
- *oldDateRange.end( )* is the specified dateRange.
**Example**

*Javascript*

```javascript
var MozartDATERANGE = ee.DateRange( '1756-1-27', '1791-12-5' );
var MozartDeathDATE = MozartDATERANGE.end( );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'So he died on the following date.', MozartDeathDATE );
```


<!------------------------------------------------------------------------------------------------------------------------------>
<!---Describing DateRanges------------------------------------------------------------------------------------------------------>
<!------------------------------------------------------------------------------------------------------------------------------>


## Describing DateRanges


### dateRange.intersects
- Creates a new Boolean set to true (only) if one specified dateRange overlaps at all with another specified dateRange.

**Syntax**

*Javascript*

```
newBoolean = 1stDateRange.intersects( 2ndDateRange )
```

- *newBoolean* is the new Boolean.
- *1stDateRange.intersects* is the first specified dateRange.
- *2ndDateRange* is the second specified dateRange.

**Example**

*Javascript*

```javascript
var MozartDATERANGE    = ee.DateRange( '1756-1-27', '1791-12-5' );
var BeethovenDATERANGE = ee.DateRange( '1770-12-17', '1827-3-26' );
var TheBOOLEAN         = MozartDATERANGE.intersects( BeethovenDATERANGE );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'DateRange for Beethoven', BeethovenDATERANGE );
print( 'Is it true that Mozart’s lifespan overlaps Beethoven’s?', TheBOOLEAN );
```


<!------------------------------------------------------------------------------------------------------------------------------>


### dateRange.contains
- Creates a new Boolean set to true (only) if a specified dateRange contains another specified date or dateRange.

**Syntax**

*Javascript*

```
newBoolean = oldDateRange.contains( anotherDateOrDateRange )
```

- *newBoolean* is the new Boolean
- *oldDateRange.contains* is the specified “container” dateRange
- *anotherDateOrDateRange* is the specified “containee” date or dateRange

**Example**

*Javascript*

```javascript
var MozartDATERANGE    = ee.DateRange( '1756-1-27', '1791-12-5' );
var BeethovenDATERANGE = ee.DateRange( '1770-12-17', '1827-3-26' );
var TheBOOLEAN         = MozartDATERANGE.contains( BeethovenDATERANGE );
print( 'DateRange for Mozart', MozartDATERANGE );
print( 'DateRange for Beethoven', BeethovenDATERANGE );
print( 'Is it true that Mozart’s lifespan contain Beethoven’s?', TheBOOLEAN );
```


<!------------------------------------------------------------------------------------------------------------------------------>


### dateRange.isEmpty
- Creates a new Boolean set to true (only) if a specified dateRange contains no dates (because its ending date precedes 

**Syntax**

*Javascript*

```
newBoolean = oldDateRange.isEmpty( )
```

- *newBoolean* is the new Boolean.
- *oldDateRange.isEmpty( )* is the specified dateRange.

**Example**

*Javascript*

```javascript
var TheDATERANGE = ee.DateRange( '1990-07-16', '1950-12-25');
var TheBOOLEAN   = TheDATERANGE.isEmpty( );
print( TheDATERANGE );
print( 'Is it true that this dateRange is empty?', TheBOOLEAN );
```


<!------------------------------------------------------------------------------------------------------------------------------>


### dateRange.isUnbounded
- Creates a new Boolean set to true (only) if a specified dateRange contains all possible dates.

**Syntax**

*Javascript*

```
newBoolean = oldDateRange.isUnbounded( )
```

- *newBoolean* is the new Boolean.
- *oldDateRange.isUnbounded* is the specified dateRange.

**Example**

*Javascript*

```javascript
var TheDATERANGE = ee.DateRange.unbounded( );
print( TheDATERANGE );
```

(Note: the following article is uneditied -- Proceed with caution).

Pandas' documentation explains the similarities between their API
and SQL for querying tabular data. A SQL query with a compound `WHERE` clause,
 for instance, can be expressed as follows:

```
-- tips of more than $5.00 at Dinner meals
SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;
```

The equivalent Pandas syntax is as such:
```
# tips of more than $5.00 at Dinner meals
>>> In [11]: tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)]
     total_bill    tip     sex smoker  day    time  size
23        39.42   7.58    Male     No  Sat  Dinner     4
44        30.40   5.60    Male     No  Sun  Dinner     4
47        32.40   6.00    Male     No  Sun  Dinner     4
52        34.81   5.20  Female     No  Sun  Dinner     4
59        48.27   6.73    Male     No  Sat  Dinner     4
116       29.93   5.07    Male     No  Sun  Dinner     4
155       29.85   5.14  Female     No  Sun  Dinner     5
170       50.81  10.00    Male    Yes  Sat  Dinner     3
172        7.25   5.15    Male    Yes  Sun  Dinner     2
181       23.33   5.65    Male    Yes  Sun  Dinner     2
183       23.17   6.50    Male    Yes  Sun  Dinner     4
211       25.89   5.16    Male    Yes  Sat  Dinner     4
212       48.33   9.00    Male     No  Sat  Dinner     4
214       28.17   6.50  Female    Yes  Sat  Dinner     3
239       29.03   5.92    Male     No  Sat  Dinner     3
```

[(source)](https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#where)

This example got me thinking, how can we generalize querying data from dataframes?
What if we wanted to filter the rows of a table with an arbitrary number of
conditions?

Using the standard Pandas syntax, it would look something like this:

```
>>> tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00) &
...      (tips['sex'] == 'Female')  & (tips['smoker'] == 'No')]
     total_bill   tip     sex smoker  day    time  size
52        34.81  5.20  Female     No  Sun  Dinner     4
155       29.85  5.14  Female     No  Sun  Dinner     5
```

This does not seem ideal. Quickly as we add more filtering logic, the line of code gets
longer and less maintainable. Furthermore, a lot of logic is repeated -- namely, we keep referring
to the `tips` dataframe over and over.

What if we want to take the same filtering operations (e.g. query by a `time` and `tip` field) on another
dataframe with a different name? We would need to re-write the whole line substituting one variable name for the
other -- or worse, swap the data each variable refers to.

How can we provide a more succinct interface for querying data? How can we make sure that
it is flexible, general, and correct?

Let's break down what's going on in the above query:

```
>>> is_dinner_time = (tips['time'] == 'Dinner')
>>> is_dinner_time.head()
0    True
1    True
2    True
3    True
4    True
Name: time, dtype: bool
>>> is_dinner_time.value_counts()
True     176
False     68
Name: time, dtype: int64
>>> is_tip_above_five = (tips['tip'] > 5.00)
>>> is_tip_above_five.head()
0    False
1    False
2    False
3    False
4    False
Name: tip, dtype: bool
>>> is_tip_above_five.value_counts()
False    226
True      18
Name: tip, dtype: int64
>>> # etc...
```

Ah! So what's actually going on is we are taking advantage of dataframes capacity for [boolean indexing](https://pandas.pydata.org/pandas-docs/stable/10min.html#boolean-indexing).

What if we could take advantage of this to abstract away which dataframe we are acting on?
Certainly, we'd prefer only to focus on the filtering logic rather than housekeeping.
Plus, we might like to reuse the query on different dataframes.

Let's try this:

```
>>> is_dinner_time = lambda df: df['time'] == 'Dinner'
>>> is_tip_above_five = lambda df: df['tip'] > 5.00
>>> tips[is_dinner_time(tips) & is_tip_above_five(tips)]
     total_bill    tip     sex smoker  day    time  size
23        39.42   7.58    Male     No  Sat  Dinner     4
44        30.40   5.60    Male     No  Sun  Dinner     4
47        32.40   6.00    Male     No  Sun  Dinner     4
52        34.81   5.20  Female     No  Sun  Dinner     4
59        48.27   6.73    Male     No  Sat  Dinner     4
116       29.93   5.07    Male     No  Sun  Dinner     4
155       29.85   5.14  Female     No  Sun  Dinner     5
170       50.81  10.00    Male    Yes  Sat  Dinner     3
172        7.25   5.15    Male    Yes  Sun  Dinner     2
181       23.33   5.65    Male    Yes  Sun  Dinner     2
183       23.17   6.50    Male    Yes  Sun  Dinner     4
211       25.89   5.16    Male    Yes  Sat  Dinner     4
212       48.33   9.00    Male     No  Sat  Dinner     4
214       28.17   6.50  Female    Yes  Sat  Dinner     3
239       29.03   5.92    Male     No  Sat  Dinner     3

```

Great. I now have two functions `is_dinner_time` and `is_tip_above_five` which I could use on any other dataframe.
However, I still am repeating the reference to `tips` as many times as I did before.
How can I get rid of this grunt work? Ideally, I would like to refer to a dataframe once, mixing in the filter
operations and I see fit.

Why not use a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)? Functions are first class citizens in python, after all. Let's abstract away
the rote work of calling these filter functions with respect to a particular dataframe.

```
>>> import functools
>>> def intersection(df, *filters):
...    mapped_boolean_dfs = [f(df) for f in filters if callable(f)]
...    accumulated_boolean_df = functools.reduce(lambda acc, d: acc & d, mapped_boolean_dfs)
...    return df[accumulated_boolean_df]
>>> intersection(tips, is_dinner_time, is_tip_above_five)
     total_bill    tip     sex smoker  day    time  size
23        39.42   7.58    Male     No  Sat  Dinner     4
44        30.40   5.60    Male     No  Sun  Dinner     4
47        32.40   6.00    Male     No  Sun  Dinner     4
52        34.81   5.20  Female     No  Sun  Dinner     4
59        48.27   6.73    Male     No  Sat  Dinner     4
116       29.93   5.07    Male     No  Sun  Dinner     4
155       29.85   5.14  Female     No  Sun  Dinner     5
170       50.81  10.00    Male    Yes  Sat  Dinner     3
172        7.25   5.15    Male    Yes  Sun  Dinner     2
181       23.33   5.65    Male    Yes  Sun  Dinner     2
183       23.17   6.50    Male    Yes  Sun  Dinner     4
211       25.89   5.16    Male    Yes  Sat  Dinner     4
212       48.33   9.00    Male     No  Sat  Dinner     4
214       28.17   6.50  Female    Yes  Sat  Dinner     3
239       29.03   5.92    Male     No  Sat  Dinner     3
```

Much better. Now, should we want to add additional fields in the table to filter on, we merely define more
filter functions -- which, again, can be used for any table.

Please note that the filter functions can be as complicated as we want, as long as they return a dataframe of
booleans the same size of the input.

For example, if we are querying string data that is messy, we could write a filter like
the following:

```
>>> def is_dinner_fuzzy(df):
...    return df['time'].apply(lambda x: fuzz.ratio(x, 'dinner')) >= 90
>>> intersection(tips, is_dinner_fuzzy, is_tip_above_five)
     total_bill    tip     sex smoker  day    time  size
23        39.42   7.58    Male     No  Sat  Dinner     4
44        30.40   5.60    Male     No  Sun  Dinner     4
47        32.40   6.00    Male     No  Sun  Dinner     4
52        34.81   5.20  Female     No  Sun  Dinner     4
59        48.27   6.73    Male     No  Sat  Dinner     4
116       29.93   5.07    Male     No  Sun  Dinner     4
155       29.85   5.14  Female     No  Sun  Dinner     5
170       50.81  10.00    Male    Yes  Sat  Dinner     3
172        7.25   5.15    Male    Yes  Sun  Dinner     2
181       23.33   5.65    Male    Yes  Sun  Dinner     2
183       23.17   6.50    Male    Yes  Sun  Dinner     4
211       25.89   5.16    Male    Yes  Sat  Dinner     4
212       48.33   9.00    Male     No  Sat  Dinner     4
214       28.17   6.50  Female    Yes  Sat  Dinner     3
239       29.03   5.92    Male     No  Sat  Dinner     3

```

(Note: `fuzz.ratio()` returns an integer representing the [levinstine distance](https://en.wikipedia.org/wiki/Levenshtein_distance) from one string to another)

Is our intersection general enough? What if we wanted to query our data but instead of using a SQL-like `AND` operation,
we wanted an `OR` operation?

Let's generalize further:

```
>>> def filter_reduce(df, *filters, reducer=lambda acc, x: acc & x):
...    mapped_dfs = [f(df) for f in filters if callable(f)]
...    accumulated_df = functools.reduce(reducer, mapped_dfs)
...    return df[accumulated_df]
>>> def intersection(df, *filters):
...    return filter_reduce(df, *filters, reducer=lambda acc, x: acc & x)
>>> def union(df, *filters):
...    return filter_reduce(df, *filters, reducer=lambda acc, x: acc | x)

```

Then we can represent the following SQL query (from the Pandas documentation) like so:
```
SELECT *
FROM tips
WHERE size >= 5 OR total_bill > 45;
```
```
>>> is_total_bill_large = lambda df: df['total_bill'] > 45
>>> is_party_gte_five = lambda df: df['size'] >= 5
>>> union(tips, is_party_gte_five, is_total_bill_large)
     total_bill    tip     sex smoker   day    time  size
59        48.27   6.73    Male     No   Sat  Dinner     4
125       29.80   4.20  Female     No  Thur   Lunch     6
141       34.30   6.70    Male     No  Thur   Lunch     6
142       41.19   5.00    Male     No  Thur   Lunch     5
143       27.05   5.00  Female     No  Thur   Lunch     6
155       29.85   5.14  Female     No   Sun  Dinner     5
156       48.17   5.00    Male     No   Sun  Dinner     6
170       50.81  10.00    Male    Yes   Sat  Dinner     3
182       45.35   3.50    Male    Yes   Sun  Dinner     3
185       20.69   5.00    Male     No   Sun  Dinner     5
187       30.46   2.00    Male    Yes   Sun  Dinner     5
212       48.33   9.00    Male     No   Sat  Dinner     4
216       28.15   3.00    Male    Yes   Sat  Dinner     5
```

Sure, we could have implemented the `union` and `intersection` cases by themselves, but the
function `filter_reduce` offers us the luxury of adaptability later on.
---
layout: post
title: "Higher Order Functions on Pandas Dataframes"
date: 2018-07-06
---

(Note: the following article is uneditied -- Proceed with caution).

(Last updated: 2018-07-31)

## Motivation

I wrote this article to capture a perspective on dataframes that I think most Python developers -- especially data 
scientists -- overlook. 

Working closely with data often lends itself to tight coupling to the structure of that data. With this comes messy, brittle code.

I advocate that there is a better way; a way that promotes modular, flexible, and testable code; a method
where we can automate away the boring parts and think clearly about the problem at hand.

The core idea is to promote re-use of logic through composition. To this end, we treat functions as data. We must also try
as much as possible to abstract away the unessential details of each operation.

I'm getting ahead of myself. It's better to *show* rather than *tell*. 
Let's explore the thought process of refactoring the standard process for querying data in Pandas.

## The Conventional Way 

The Pandas documentation explains the similarities between their API
and SQL for querying tabular data. A SQL query with a compound `WHERE` clause,
 for instance, can be expressed as follows:

{% highlight SQL %}
-- tips of more than $5.00 at Dinner meals
SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;
{% endhighlight %}

The equivalent Pandas syntax is as such:

{% highlight python %}
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
{% endhighlight %}

[(source)](https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#where)

What if we wanted to extend our query with an arbitrary number of conditions?

Using the standard Pandas syntax, it would look something like this:

{% highlight python %}
>>> tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00) &
...      (tips['sex'] == 'Female')  & (tips['smoker'] == 'No')]
     total_bill   tip     sex smoker  day    time  size
52        34.81  5.20  Female     No  Sun  Dinner     4
155       29.85  5.14  Female     No  Sun  Dinner     5
{% endhighlight %}

This does not seem ideal. Our line of code quickly gets longer as we add more filtering logic. This can't be 
maintainable. A lot of logic is repeated -- namely, we keep referring to the `tips` dataframe over and over. What if the 
dataframe name changed? Or we wanted to apply the same query to another, similar table? 

This would double our work: We would need to re-write the whole line substituting one variable name for the
other. Or worse, we could swap the data each variable refers to.

How can we provide a more succinct interface for querying data? How can we make sure that
it is intuitive, general, and correct?

## Breaking down the problem 

Let's break down what's going on in the above query:

{% highlight python %}
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
{% endhighlight %}

Ah! So what's actually going on is we are taking advantage of dataframe's capacity for [boolean indexing](https://pandas.pydata.org/pandas-docs/stable/10min.html#boolean-indexing).

What if we could use this to abstract away which dataframe we are acting on?
Certainly, we'd prefer to only focus on the filtering logic rather than housekeeping.
Plus, we might like to reuse the query on different dataframes.

Let's try this:

{% highlight python %}
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

{% endhighlight %}

Great. I now have two functions `is_dinner_time` and `is_tip_above_five` which I could use on any other dataframe.
However, I still am repeating the reference to `tips` as many times as I did before.
How can I get rid of this grunt work? Ideally, I would like to refer to a dataframe once, mixing in the filter
operations and I see fit.

## Towards generalization 

Why not use a [higher-order function](https://en.wikipedia.org/wiki/Higher-order_function)? Functions are first class citizens in python, after all. Let's abstract away
the rote work of calling these filter functions with respect to a particular dataframe.

{% highlight python %}
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

{% endhighlight %}

Much better. Now, should we want to add additional fields in the table to filter on, we merely define more
filter functions -- which, again, can be used for any table.

Please note that each functions can be as complicated as we want, as long as they return a dataframe of
booleans the same size of the input.

For example, if we are querying string data that is messy, we could write a filter like
the following:

{% highlight python %}
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

{% endhighlight %}

(Note: `fuzz.ratio()` returns an integer representing the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) from one string to another)


## How general can we go?

Is our intersection general enough? What if we wanted to query our data but instead of using a SQL-like `AND` operation,
we wanted an `OR` operation?

Let's generalize further:

{% highlight python %}
>>> def filter_reduce(df, *filters, reducer=lambda acc, x: acc & x):
...    mapped_dfs = [f(df) for f in filters if callable(f)]
...    accumulated_df = functools.reduce(reducer, mapped_dfs)
...    return df[accumulated_df]
>>> def intersection(df, *filters):
...    return filter_reduce(df, *filters, reducer=lambda acc, x: acc & x)
>>> def union(df, *filters):
...    return filter_reduce(df, *filters, reducer=lambda acc, x: acc | x)

{% endhighlight %}

Then we can represent the following SQL query (from the Pandas documentation) like so:

{% highlight SQL %}
SELECT *
FROM tips
WHERE size >= 5 OR total_bill > 45;
{% endhighlight %}

{% highlight python %}
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

{% endhighlight %}

Sure, we could have implemented the `union` and `intersection` cases by themselves, but the
function `filter_reduce` offers us the luxury of adaptability later on.


## Beyond querying
Can this perspective help with other problems besides querying?

Often, we need to mutate dataframes: a new column of derived values has to be added, or we want to change the type of a 
column. Mutability comes with several challenges:
What if we make a mistake when mutating the dataframe, and we would like to revert to the previous form? What if we 
wanted to know what the original data looked like?

In Pandas, we can simulate immutability by creating mapping functions that first perform a shallow copy of the input 
dataframe and return a new result.

{% highlight python %}
>>> def add_subtotal(df):
...     cp = pd.DataFrame(df, copy=True)
...     cp['subtotal'] = cp['total_bill'] - cp['tip']
...     return cp
>>> tips1 = add_subtotal(tips)
>>> tips1.head()
   total_bill   tip     sex smoker  day    time  size  subtotal
0       16.99  1.01  Female     No  Sun  Dinner     2     15.98
1       10.34  1.66    Male     No  Sun  Dinner     3      8.68
2       21.01  3.50    Male     No  Sun  Dinner     3     17.51
3       23.68  3.31    Male     No  Sun  Dinner     2     20.37
4       24.59  3.61  Female     No  Sun  Dinner     4     20.98
>>> def add_avg_bill(df): 
...     cp = pd.DataFrame(df, copy=True)
...     cp['price_per_person'] = cp['subtotal'] / cp['size']
...     return cp
>>> tips2 = add_avg_bill(tips1)
>>> tips2.head()
   total_bill   tip     sex smoker  day    time  size  subtotal  \
0       16.99  1.01  Female     No  Sun  Dinner     2     15.98   
1       10.34  1.66    Male     No  Sun  Dinner     3      8.68   
2       21.01  3.50    Male     No  Sun  Dinner     3     17.51   
3       23.68  3.31    Male     No  Sun  Dinner     2     20.37   
4       24.59  3.61  Female     No  Sun  Dinner     4     20.98   
   price_per_person  
0          7.990000  
1          2.893333  
2          5.836667  
3         10.185000  
4          5.245000  
>>> def yesno_to_bool(df, column='smoker'):
...     cp = pd.DataFrame(df, copy=True)
...     cp[column] = cp[column].apply(lambda x: x == 'Yes')
...     return cp
>>> tips3 = yesno_to_bool(tips2, 'smoker')
>>> tips3.head()
Out[52]: 
   total_bill   tip     sex  smoker  day    time  size  subtotal  \
0       16.99  1.01  Female   False  Sun  Dinner     2     15.98   
1       10.34  1.66    Male   False  Sun  Dinner     3      8.68   
2       21.01  3.50    Male   False  Sun  Dinner     3     17.51   
3       23.68  3.31    Male   False  Sun  Dinner     2     20.37   
4       24.59  3.61  Female   False  Sun  Dinner     4     20.98   
   price_per_person  
0          7.990000  
1          2.893333  
2          5.836667  
3         10.185000  
4          5.245000  

{% endhighlight %}

...

We can combine all of these -- and arbitrarily more operations -- through a higher order function called `compose`:

{% highlight python %}
>>> import functools
>>> def compose(df, *mappers):
...     return functools.reduce(lambda acc, x: x(acc), mappers, df)
>>> tips_all = compose(tips, add_subtotal, add_avg_bill, lambda x: yesno_to_bool(x, 'smoker'))
>>> tips_all.head()
   total_bill   tip     sex  smoker  day    time  size  subtotal  \
0       16.99  1.01  Female   False  Sun  Dinner     2     15.98   
1       10.34  1.66    Male   False  Sun  Dinner     3      8.68   
2       21.01  3.50    Male   False  Sun  Dinner     3     17.51   
3       23.68  3.31    Male   False  Sun  Dinner     2     20.37   
4       24.59  3.61  Female   False  Sun  Dinner     4     20.98   
   price_per_person  
0          7.990000  
1          2.893333  
2          5.836667  
3         10.185000  
4          5.245000  

{% endhighlight %}

One advantage of this approach is that mutating dataframes can be lazily evaluated: We can wait to modify the data only
until it's needed (i.e. until we call `compose`).

Another advantage is that we preserver all the intermediate states of the data. Further, we have complete flexibility 
as to what mappings get applied. Decide that we want to keep the `smokers` column as strings again? Just remove the
`yesno_to_bool` function. Decide that you'd rather map it to `int`s? Just swap out the function. Just like the filter
functions, the mapper functions can be applied to any dataframe, provided it has the correct columns. 

You may be wondering if copying all of the data is inefficient? Surely, you don't want to duplicate your data all over
the place, especially if your data is large.

Pandas is actually very clever when it comes to copying data. The copied dataframes store 
references to the original values. Only when the data gets mutated does it decide to allocate new memory. 
Only the *differences* from one dataframe to another are stored. Thus, representing transformations with copies remains
efficient while promoting many other benefits. 

Don't take my word for it! Let's prove that this is the case:

{% highlight python %}
>>> tips_ref_original = tips.applymap(id)
>>> tips_ref_copied = tips_all.applymap(id)
>>> tips_ref_original.head()
    total_bill              tip              sex           smoker  \
0  139919566582840  139919566583392  139919566677192  139919567009976   
1  139919566584736  139919566583416  139919567011768  139919567009976   
2  139919566584760  139919566583440  139919567011768  139919567009976   
3  139919566584808  139919566583464  139919567011768  139919567009976   
4  139919566584832  139919566583488  139919566677192  139919567009976   
               day             time            size  
0  139919567011600  139919567008184  94289170979360  
1  139919567011600  139919567008184  94289170979392  
2  139919567011600  139919567008184  94289170979392  
3  139919567011600  139919567008184  94289170979360  
4  139919567011600  139919567008184  94289170979424  
>>> tips_ref_copied.head()
        total_bill              tip              sex          smoker  \
0  139919450679696  139919450735360  139919566677192  94289170711232   
1  139919450679720  139919450735336  139919567011768  94289170711232   
2  139919450679744  139919450735312  139919567011768  94289170711232   
3  139919450679768  139919450735288  139919567011768  94289170711232   
4  139919450679792  139919450735264  139919566677192  94289170711232   
               day             time            size         subtotal  \
0  139919567011600  139919567008184  94289170979360  139919450679696   
1  139919567011600  139919567008184  94289170979392  139919450679720   
2  139919567011600  139919567008184  94289170979392  139919450679744   
3  139919567011600  139919567008184  94289170979360  139919450679768   
4  139919567011600  139919567008184  94289170979424  139919450679792   
   price_per_person  
0   139919450735360  
1   139919450735336  
2   139919450735312  
3   139919450735288  
4   139919450735264  
>>> tips_xor = tips_ref_original ^ tips_ref_copied
>>> tips_xor.head()
   day  price_per_person  sex  size          smoker  subtotal  time  \
0    0               NaN    0     0  46733414398584       NaN     0   
1    0               NaN    0     0  46733414398584       NaN     0   
2    0               NaN    0     0  46733414398584       NaN     0   
3    0               NaN    0     0  46733414398584       NaN     0   
4    0               NaN    0     0  46733414398584       NaN     0   
         tip  total_bill  
0  423146848   423075240  
1  423146640   423072264  
2  423146560   423072376  
3  423146512   423072304  
4  423146592   423073264  

{% endhighlight %}

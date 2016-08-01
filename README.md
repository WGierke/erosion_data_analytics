# Erosion Data Analytics

Our task was to analyze given erosion data in order to find possible relations, how the erosion rate correlates with the rock type, the basin slope, the climate zone etc.
This is an important research topic in geology since the measurement of a erosion sample costs approxmately 800$.
Thus, it's desired to be able to predict the erosion rate using already known features.

[The world map](https://github.com/WGierke/erosion_data_analytics/blob/master/World%20Map.ipynb) gives an overview of where the given samples were taken from.  
[Overview](https://github.com/WGierke/erosion_data_analytics/blob/master/Overview.ipynb) summarizes properties of the given samples.  
[Statistics](https://github.com/WGierke/erosion_data_analytics/blob/master/Statistics.ipynb) performs some simple statistical analysis on the data.  
[Correlation](https://github.com/WGierke/erosion_data_analytics/blob/master/Correlation.ipynb) uses the Pearson coefficient to find correlations between the erosion rate and the features.

We found out that the *mean annual temperature* and the *vegetation zone* features correlate negatively with the erosion rate.
On the other hand, the *mean basin slope* has the largest positive correlation.
Unfortunately, since the sample data is very small, we can't be certain that our results are equal on bigger sample sizes.

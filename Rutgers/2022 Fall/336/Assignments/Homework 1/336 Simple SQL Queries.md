---
title: Simple SQL Queries
course: CS_336
released: 2022-09-22
due: 2022-10-03
tags: 
- Assignments
- CS_336
---
<center><h1>Simple SQL Queries</h1></center>
<center><h3>CS 210 - Principles of Information and Data Management</h3></center>

Return SQL code as text file plus results which workbench gave you (you can include them in the same txt file). Query + answer. As long as it is readable by a grader, it is fine - text, word, screenshot....but text is easiest.   

### 1.  Find all distinct drinkers whose phone numbers come from area code 917 and who like Budweiser or Bud (synonym!)
**Interpretation**: All unique drinkers whose phone numbers start with 917 and like Bud / Budweiser.

```sql
SELECT DISTINCT drinker  
FROM Likes l, Drinkers d  
WHERE  
(l.beer='Budweiser' OR l.beer='Bud') AND  
d.phone LIKE '917%' AND  
d.name = l.drinker
```

	# drinker


### 2. What beers does Mike like?
**Interpretation**: Beers liked by Mike
```sql
SELECT DISTINCT beer FROM Likes WHERE drinker='Mike'
```

	# beer
	
	Blue Moon  
	Bud  
	Budweiser  
	Creamy Dark  
	Hefeweizen  
	Michelob Golden Draft Light  
	Original Premium Lager  
	Original Premium Lager Dog  
	Killian's

### 3. Which town has the most drinkers?
**Interpretation:** Return a single town that has no other towns with more drinkers
```sql
SELECT city  
FROM Drinkers  
GROUP BY city  
ORDER BY count(*) DESC  
LIMIT 1;
```

	# city
	Edison

### 4. What bars are frequented by drinkers from that town (3)?
**Interpretation:** As written in question

```sql
SELECT DISTINCT bar  
FROM Frequents f, Drinkers d  
WHERE d.name = f.drinker AND  
d.city = 'Edison';
```

	# bar
	'Gecko Grill'
	'Cabana'
	'Blue Angel'
	'Seven Bamboo'

### 5. Provide all bars which serve beers that Mike likes
**Interpretation:** As written in question
```sql
SELECT DISTINCT s.bar  
FROM Sells s, (SELECT beer FROM Likes WHERE drinker='Mike') AS b  
WHERE s.beer = b.beer;
```

	# bar
	
	A.P. Stump's  
	Blue Angel  
	Blue Tattoo  
	Britannia Arms  
	Cabana  
	Caravan  
	Club 175  
	Coconut Willie's Cocktail Lounge  
	Gecko Grill  
	Giza Hookah Lounge  
	Hedley Club  
	Seven Bamboo  
	The Backbeat  
	The Blank Club  
	The Shark and Rose


### 6. Who likes at least one same beer that Joe or Mike like?
**Interpretation:** Return all drinkers that like at least one beer that is also liked by Joe or Mike.
```sql
SELECT DISTINCT l.drinker  
FROM Likes l, Likes l1, Likes l2  
WHERE  
(l.beer = l1.beer OR l.beer = l2.beer)  
AND l.drinker != 'Joe' AND l.drinker != 'Mike';
```

	# drinker
	'John'
	'Justin'
	'Devarsh'
	'Yuhan'
	'Vince'
	'Gunjan'
	'Sahil'
	'Jesse'

### 7.  All bars which sell at least one beer which is liked by at least one drinker who frequents these bars
**Interpretation:** Return bars that sell a beer that is liked by someone who frequents their bar.

```sql
SELECT DISTINCT s.bar  
FROM Sells s, Frequents f, Likes l  
WHERE f.bar = s.bar AND  
s.beer = l.beer AND  
f.drinker = l.drinker;
```

	# bar
	'The Shark and Rose'
	'Seven Bamboo'
	'Gecko Grill'
	'Caravan'
	'Cabana'
	'Blue Angel'
	'A.P. Stump\'s'



### 8. Drinkers who like some beers sold by Caravan bar
**Interpretation:** Drinkers who like some (two or more) beers sold by Caravan bar
```sql
SELECT DISTINCT l.drinker  
FROM Likes l, Sells s  
WHERE l.beer = s.beer AND s.bar = 'Caravan'  
GROUP BY l.drinker HAVING count(*) >= 1;
```

	# drinker
	'John'
	'Mike'
	'Vince'
	'Gunjan'
	'Yuhan'
<div style="page-break-after: always;"></div>

### 9. Bars which sell Budweiser and are frequented by some drinkers who like Budweiser
**Interpretation:** As written in title
```sql
SELECT DISTINCT b.bar
FROM 
(SELECT DISTINCT bar FROM Sells WHERE Sells.beer = 'Budweiser') as b,
Frequents f,
Likes l
WHERE
f.drinker = l.drinker
AND l.beer = 'Budweiser'
AND f.bar = b.bar
```
	
	# bar
	'Cabana'
	'Caravan'
	'Gecko Grill'
	'Seven Bamboo'
	'The Shark and Rose'

### 10.  Bars which are frequented by Mike and Steve
**Interpretation:** As written in title
```sql
SELECT DISTINCT f1.bar
FROM Frequents f1, Frequents f2
WHERE
f1.bar = f2.bar
AND f1.drinker='Mike' AND f2.drinker='Steve'
```

	# bar
	null

### 11. Drinker who like at least two beers that Mike likes
**Interpretation:** As written in title
```sql
SELECT COUNT(*), drinker
FROM Likes l1
WHERE beer in (
SELECT beer
FROM Likes l
WHERE
l.drinker = 'Mike'
AND l1.drinker!=l.drinker
)
GROUP BY l1.drinker
HAVING COUNT(*)>1
```
	# COUNT(*), drinker
	'5', 'John'
	'2', 'Justin'
	'2', 'Gunjan'
	'3', 'Yuhan'



### 12. Bars which sell at least 3 beers that Mike likes (do not use COUNT)
**Interpretation:** As written in title

```sql
SELECT DISTINCT s1.bar
FROM 
Sells s1, Sells s2, Sells s3
WHERE
s1.bar = s2.bar AND s2.bar = s3.bar
AND s1.beer IN (SELECT l.beer FROM Likes l WHERE l.drinker="Mike")
AND s2.beer IN (SELECT l.beer FROM Likes l WHERE l.drinker="Mike")
AND s3.beer IN (SELECT l.beer FROM Likes l WHERE l.drinker="Mike")
AND s1.beer != s2.beer AND s2.beer != s3.beer AND s3.beer != s1.beer;
```

	# bar
	'Caravan'

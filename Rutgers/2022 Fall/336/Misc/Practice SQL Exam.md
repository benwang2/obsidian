1. Bars which sell at least one beer liked by a resident of Edison
```sql
SELECT DISTINCT s.bar
FROM
	Sells s,
    (SELECT beer FROM Drinkers d, Likes l WHERE d.city = 'Edison') as b
WHERE
	s.beer = b.beer;
```
	Caravan
	Britannia Arms
	Cabana
	Club 175
	Coconut Willie's Cocktail Lounge
	Gecko Grill
	Giza Hookah Lounge
	Seven Bamboo
	The Blank Club
	The Shark and Rose
	A.P. Stump's
	Hedley Club
	Blue Tattoo
	The Backbeat
	Blue Angel

2. Beers which are liked by Mike and by Devarsh
   ```sql
SELECT DISTINCT l.beer
FROM
	Likes l,
    Likes l1
WHERE
	l.drinker = 'Mike' AND 
    l1.drinker = 'Devarsh' AND 
    l.beer = l1.beer
```
	Blue Moon

3. Drinkers who do not frequent Caravan bar
```sql
SELECT DISTINCT d.name
FROM Drinkers d
WHERE d.name NOT IN (
		SELECT f.drinker
        FROM Frequents f
        WHERE f.bar = 'Caravan'
);
```
	Ahmed
	Ajla
	Bob
	Boshen
	Devarsh
	Erik
	Gunjan
	Harshal
	Herb
	Jeanie
	Jesse
	Kayla
	Laura
	Mike
	Rebecca
	Sahil
	Tatiana
	Vedant
	Vince
	Vishal
	Yuchen
	Yuhan

4. Bars which sell most beers under $6 (include ties)
```sql
SELECT bar
FROM Sells
WHERE price < 6
GROUP BY bar
HAVING COUNT(*) = (
	SELECT COUNT(*)
	FROM Sells
	WHERE price < 6
	GROUP BY bar 
	ORDER BY COUNT(*) DESC
	LIMIT 1
);
```
	The Shark and Rose
5. Bars which sell all beers
```sql
SELECT DISTINCT s.bar
FROM Sells s
WHERE NOT EXISTS(
	SELECT name
	FROM Beers b
	WHERE name NOT IN (SELECT beer FROM Sells WHERE bar=s.bar)
);
```
	None

6. Use left join to find Drinkers who do not frequent Caravan bar
```sql
SELECT DISTINCT name
FROM Drinkers d
LEFT JOIN Frequents as f
ON d.name = f.drinker
WHERE f.bar != 'Caravan' OR f.bar IS NULL;
```
	Ahmed
	Ajla
	Bob
	Boshen
	Devarsh
	Erik
	Gunjan
	Harshal
	Herb
	Jeanie
	Jesse
	Joe
	John
	Justin
	Kayla
	Laura
	Mike
	Rebecca
	Sahil
	Tatiana
	Tom
	Vedant
	Vince
	Vishal
	Yuchen
	Yuhan
7. Use Case statement to add new attribute to Sells table with two values:  "Expensive" and "Regular". Expensive are beers sold above $8, The remaining beers are "Regular".
```sql
SELECT *, CASE
	WHEN price > 8 THEN 'Expensive'
    ELSE 'Regular'
END
FROM Sells;
```

| bar                                 | beer                         | price   | case            |
| ----------------------------------- | ---------------------------- | ------- | ----------- |
| 'A.P. Stump\'s'                     | 'Hefeweizen'                 | '6.00'  | 'Regular'   |
| 'Blue Angel'                        | 'Hefeweizen Doppelbock'      | '5.80'  | 'Regular'   |
| 'Blue Angel'                        | 'Original Premium Lager Dog' | '6.55'  | 'Regular'   |
| 'Blue Tattoo'                       | 'Killian\'s'                 | '6.00'  | 'Regular'   |
| 'Britannia Arms'                    | 'Budweiser'                  | '6.80'  | 'Regular'   |
| 'Cabana'                            | 'Budweiser'                  | '3.84'  | 'Regular'   |
| 'Caravan'                           | 'Budweiser'                  | '10.80' | 'Expensive' |
| 'Caravan'                           | 'Original Premium Lager Dog' | '8.80'  | 'Expensive' |
| 'Club 175'                          | 'Budweiser'                  | '4.50'  | 'Regular'   |
| 'Coconut Willie\'s Cocktail Lounge' | 'Budweiser'                  | '3.55'  | 'Regular'   |
| 'Eulipia'                           | 'Hefeweizen Doppelbock'      | '4.50'  | 'Regular'   |
| 'Gecko Grill'                       | 'Budweiser'                  | '3.00'  | 'Regular'   |
| 'Giza Hookah Lounge'                | 'Budweiser'                  | '3.25'  | 'Regular'   |
| 'Giza Hookah Lounge'                | 'Stolichnaya Citrona'        | '6.00'  | 'Regular'   |
| 'Hedley Club'                       | 'Hefeweizen'                 | '8.00'  | 'Regular'   |
| 'Hedley Club'                       | 'Hefeweizen Doppelbock'      | '5.50'  | 'Regular'   |
| 'Seven Bamboo'                      | 'Budweiser'                  | '2.50'  | 'Regular'   |
| 'The B-Hive'                        | 'Michelob Amber Bock'        | '5.00'  | 'Regular'   |
| 'The Backbeat'                      | 'Killian\'s'                 | '3.50'  | 'Regular'   |
| 'The Blank Club'                    | 'Budweiser'                  | '5.50'  | 'Regular'   |
| 'The Shark and Rose'                | 'Budweiser'                  | '4.50'  | 'Regular'   |
| 'The Shark and Rose'                | 'Original Premium Lager Dog' | '5.50'  | 'Regular'   |
| 'Gecko Grill'                       | 'Hefeweizen'                 | '6.00'  | 'Regular'   |
| 'Caravan'                           | 'Bud'                        | NULL    | 'Regular'   |
| 'Caravan'                           | 'Bud'                        | NULL    | 'Regular'   |
| 'Caravan'                           | 'Bud'                        | NULL    | 'Regular'   |
| 'Caravan'                           | 'Bud'                        | '10.30' | 'Expensive' |
| 'Caravan'                           | 'Zywiec'                     | '10.30' | 'Expensive' |
| 'Caravan'                           | 'Zywiec'                     | '10.30' | 'Expensive' |
| 'Caravan'                           | 'Zywiec'                     | '10.30' | 'Expensive' |
| 'Caravan'                           | 'Zywiec'                     | '10.30' | 'Expensive' |
| 'Caravan'                           | 'Zywiec'                     | '10.30' | 'Expensive' |
| 'Bosman'                            | 'Zywiec'                     | '6.00'  | 'Regular'   |
| 'Bosman'                            | 'Okocim'                     | '5.00'  | 'Regular'   |


8. Which precinct(s) had the highest totalvotes at the end of voting?
```sql
FROM Penna p
WHERE
	p.Timestamp = (
		SELECT p1.Timestamp
		FROM Penna p1
		WHERE p1.precinct = p.precinct
		ORDER BY p1.Timestamp DESC
		LIMIT 1
	)
    AND p.totalvotes = (
		SELECT totalvotes
        FROM Penna
        ORDER BY totalvotes
        DESC LIMIT 1
	);
```
9. Extract domain name from www.cs.rutgers.edu/~rmartin
```sql
SELECT SUBSTRING_INDEX(SUBSTRING_INDEX('www.cs.rutgers.edu', 'www.', -1), '/', 1) as res;
```
10. How many votes did Biden get by the end of the day of November 6, 2020?

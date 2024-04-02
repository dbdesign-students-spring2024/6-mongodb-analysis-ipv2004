# AirBnB MongoDB Analysis
## Ishar Varma
### Data set details:
1. This data set is from the Inside Airbnb website, and it details the airbnb data for specific cities around the world, giving a comprehensive list of basically every aspect of the property posted on airBnB, which is great if i wanted to find somewhere with very specific parameters. I chose the city of Porto in Portugal because I've always wanted to go there.
[Porto data](https://insideairbnb.com/porto/)
[Inside Airbnb](http://insideairbnb.com/get-the-data/)
2. The data was originally in a csv.gz data format, which was later decompressed to a normal .csv file in the i6 database
3. **Original Data**

| id                  | name                                                      | host_id   | host_name     | neighbourhood_cleansed              | latitude           | longitude          | property_type              | room_type          | price | minimum_nights | maximum_nights |
|---------------------|-----------------------------------------------------------|-----------|---------------|-------------------------------------|--------------------|--------------------|-----------------------------|--------------------|-------|----------------|----------------|
| 1047129969789053982 | Home in Porto · ★New · 1 bedroom · 2 beds · 1 bath        | 37066714  | Diogo         | Lordelo do Ouro e Massarelos        | 41.15591959420874  | -8.649161788997706 | Entire home                | Entire home/apt    | $35.00| 1              | 1125           |
| 1047098537943911534 | Rental unit in Porto · ★New · 2 bedrooms · 4 beds · 1 bath| 74632957  | Maria Amélia  | Cedofeita, Ildefonso, Sé, Miragaia.. | 41.14893270282833  | -8.61613330428188  | Entire rental unit         | Entire home/apt    | $30.00| 2              | 50             |
| 1047095823178760491 | Rental unit in Porto · ★New · 1 bedroom · 1 bed · 1 bath  | 521069984 | Holidu        | Cedofeita, Ildefonso, Sé, Miragaia.. | 41.14702608374129  | -8.616599320237727 | Entire rental unit         | Entire home/apt    | $115.00| 1             | 365            |
| 1047093215736505702 | Rental unit in Porto · ★New · 1 bedroom · 1 bed · 2 baths | 521069984 | Holidu        | Cedofeita, Ildefonso, Sé, Miragaia.. | 41.1470584         | -8.6166476         | Entire rental unit         | Entire home/apt    | $115.00| 1             | 365            |
| 1047092758660013660 | Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath| 542228046 | Ricardo       | Cedofeita, Ildefonso, Sé, Miragaia.. | 41.1519460953842   | -8.611383315319532 | Entire rental unit         | Entire home/apt    | $85.00| 1             | 365            |
| 1047042712259867835 | Rental unit in Matosinhos · ★New · 1 bedroom · 1 bed · 1 bath | 551102753 | Hezi | Matosinhos e Leça da Palmeira | 41.1793 | -8.68685 | Entire rental unit | Entire home/apt | $90.00 | 1 | 1125 |
| 1046919773146082304 | Rental unit in Vila Nova de Gaia · ★New · 1 bedroom · 2 beds · 1 bath | 549399740 | Alexandra | Santa Marinha e São Pedro da Afurada | 41.13524 | -8.61055 | Entire rental unit | Entire home/apt | $55.00 | 3 | 365 |
| 1046504324811801951 | Bed and breakfast in Vila do Conde · ★New · 1 bedroom · 6 beds · 3.5 shared baths | 505353144 | Cachinnans Hostel | Vila do Conde | 41.3611625 | -8.757869 | Shared room in bed and breakfast | Shared room | $16.00 | 1 | 31 |
| 1046447180098227323 | Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath | 37066714 | Diogo | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.15396 | -8.6171 | Entire rental unit | Entire home/apt | $61.00 | 1 | 1125 |
| 1046353439303737070 | Rental unit in Matosinhos · ★New · 1 bedroom · 2 beds · 1 bath | 550970342 | GuestReady | Matosinhos e Leça da Palmeira | 41.17988005898072 | -8.685176210668939 | Entire rental unit | Entire home/apt | $90.00 | 1 | 1125 |
| 1046345736581286273 | Rental unit in Porto · ★New · Studio · 1 bed · 1 bath | 368252613 | Trent | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.16035320561446 | -8.620059475713948 | Entire rental unit | Entire home/apt | $31.00 | 2 | 270 |
| 1046338176948816995 | Home in Porto · ★New · Studio · 1 bed · 1 bath | 368252613 | Trent | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.159979720460285 | -8.621359296869604 | Entire home | Entire home/apt | $31.00 | 2 | 270 |
| 1046310506182063350 | Rental unit in Porto · ★New · 7 bedrooms · 7 beds · 6 baths | 12730028 | Host | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.14722 | -8.61696 | Entire rental unit | Entire home/apt | $359.00 | 1 | 365 |
| 1046302544171485150 | Rental unit in Porto · ★New · 1 bedroom · 1 bed · 1 bath | 550960414 | Vanessa | Bonfim | 41.15102468559961 | -8.600858721675461 | Entire rental unit | Entire home/apt | $41.00 | 2 | 270 |
| 1046205107572647577 | Rental unit in Porto · ★New · 3 bedrooms · 4 beds · 3 baths | 12730028 | Host | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.147030989023506 | -8.61687445861954 | Entire rental unit | Entire home/apt | $168.00 | 1 | 365 |
| 1046198693629096721 | Rental unit in Porto · ★New · 3 bedrooms · 4 beds · 3 baths | 12730028 | Host | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.145035721783735 | -8.615419389522197 | Entire rental unit | Entire home/apt | $178.00 | 1 | 365 |
| 1046158581683598224 | Rental unit in Porto · ★New · 2 bedrooms · 3 beds · 1 bath | 550932241 | Frederico | Campanhã | 41.15055083482842 | -8.589043271504533 | Entire rental unit | Entire home/apt | $74.00 | 2 | 270 |
| 1046147200330770785 | Home in Porto · ★New · Studio · 2 beds · 1 bath | 492711799 | Rachel | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.15902105517569 | -8.614493741373769 | Entire home | Entire home/apt | $50.00 | 2 | 60 |
| 1046032278569119632 | Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath | 118420008 | João Maria Teresa | Cedofeita, Ildefonso, Sé, Miragaia, Nicolau, Vitória | 41.143815042587576 | -8.617255514433014 | Entire rental unit | Entire home/apt | $80.00 | 1 | 1125 |

4. **Munging:**
I created a python program that takes the file "listings.csv" and saves only the columns labelled id, host_id, host_is_superhost, name, price, neighbourhood, host_name, beds, neighbourhood_group_cleansed, neighborhood, review_scores_rating, as these are the only columns relevent to the data analysis I am going to perform below (ie saves space in the server). Only problems i encountered were the fact that a lot of columns didnt have reviews



### Data analysis in mongoDB
1. **show exactly two documents from the listings collection in any order**
```shell
db.listings.find().limit(2)
[
  {
    _id: ObjectId('660c339cb6515eb20574d589'),
    id: Long('1047129969789053982'),
    host_id: 37066714,
    host_is_superhost: 'f',
    name: 'Home in Porto · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$35.00',
    neighbourhood: '',
    host_name: 'Diogo',
    beds: 2,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58a'),
    id: Long('1047095823178760491'),
    host_id: 521069984,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 1 bed · 1 bath',
    price: '$115.00',
    neighbourhood: '',
    host_name: 'Holidu',
    beds: 1,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  }
]
```

2. **show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.**
```shell
db.listings.find().limit(10).pretty()
[
  {
    _id: ObjectId('660c339cb6515eb20574d589'),
    id: Long('1047129969789053982'),
    host_id: 37066714,
    host_is_superhost: 'f',
    name: 'Home in Porto · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$35.00',
    neighbourhood: '',
    host_name: 'Diogo',
    beds: 2,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58a'),
    id: Long('1047095823178760491'),
    host_id: 521069984,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 1 bed · 1 bath',
    price: '$115.00',
    neighbourhood: '',
    host_name: 'Holidu',
    beds: 1,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58b'),
    id: Long('1047042712259867835'),
    host_id: 551102753,
    host_is_superhost: 'f',
    name: 'Rental unit in Matosinhos · ★New · 1 bedroom · 1 bed · 1 bath',
    price: '$90.00',
    neighbourhood: 'Matosinhos, Porto, Portugal',
    host_name: 'Hezi',
    beds: 1,
    neighbourhood_group_cleansed: 'MATOSINHOS',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58c'),
    id: Long('1047098537943911534'),
    host_id: 74632957,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 4 beds · 1 bath',
    price: '$30.00',
    neighbourhood: '',
    host_name: 'Maria Amélia',
    beds: 4,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58d'),
    id: Long('1047093215736505702'),
    host_id: 521069984,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 1 bed · 2 baths',
    price: '$115.00',
    neighbourhood: '',
    host_name: 'Holidu',
    beds: 1,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58e'),
    id: Long('1046504324811801951'),
    host_id: 505353144,
    host_is_superhost: 't',
    name: 'Bed and breakfast in Vila do Conde · ★New · 1 bedroom · 6 beds · 3.5 shared baths',
    price: '$16.00',
    neighbourhood: 'Vila do Conde, Porto, Portugal',
    host_name: 'Cachinnans Hostel',
    beds: 6,
    neighbourhood_group_cleansed: 'VILA DO CONDE',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d58f'),
    id: Long('1046447180098227323'),
    host_id: 37066714,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath',
    price: '$61.00',
    neighbourhood: '',
    host_name: 'Diogo',
    beds: 2,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d590'),
    id: Long('1046353439303737070'),
    host_id: 550970342,
    host_is_superhost: 'f',
    name: 'Rental unit in Matosinhos · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$90.00',
    neighbourhood: 'Matosinhos, Porto, Portugal',
    host_name: 'GuestReady',
    beds: 2,
    neighbourhood_group_cleansed: 'MATOSINHOS',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d591'),
    id: Long('1047092758660013660'),
    host_id: 542228046,
    host_is_superhost: 'f',
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath',
    price: '$85.00',
    neighbourhood: '',
    host_name: 'Ricardo',
    beds: 2,
    neighbourhood_group_cleansed: 'PORTO',
    review_scores_rating: ''
  },
  {
    _id: ObjectId('660c339cb6515eb20574d592'),
    id: Long('1046919773146082304'),
    host_id: 549399740,
    host_is_superhost: 'f',
    name: 'Rental unit in Vila Nova de Gaia · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$55.00',
    neighbourhood: 'Vila Nova de Gaia, Porto, Portugal',
    host_name: 'Alexandra',
    beds: 2,
    neighbourhood_group_cleansed: 'VILA NOVA DE GAIA',
    review_scores_rating: ''
  }
```

3. **choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts**
```shell
ipv2004> db.listings.find( { $or: [ { host_id: 2228036, host_is_superhost: 't' }, { host_id: 456999607, host_is_superhost: 't' }] }, { _id: 0, name: 1, price: 1, neighbourhood: 1, host_name: 1, host_is_superhost: 1 } ).pretty()
[
  {
    host_is_superhost: 't',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 3 beds · 1 bath',
    price: '$71.00',
    neighbourhood: '',
    host_name: 'Rui'
  },
  {
    host_is_superhost: 't',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$71.00',
    neighbourhood: '',
    host_name: 'Rui'
  },
  {
    host_is_superhost: 't',
    name: 'Rental unit in Porto · ★New · 1 bedroom · 3 beds · 1 bath',
    price: '$71.00',
    neighbourhood: '',
    host_name: 'Rui'
  },
  {
    host_is_superhost: 't',
    name: 'Rental unit in Porto · ★New · 5 bedrooms · 8 beds · 5 baths',
    price: '$430.00',
    neighbourhood: '',
    host_name: 'Rui'
  },
```
Significance, superhosts own a lot of different properties, and it seems like the price of these properties can very significantly, but superhosts may imply more experience, ie more trustworthy
4. **find all the unique host_name values**
```shell
db.listings.distinct("host_name")
[
  57,
  '(Joe)  American Club Granja',
  '24 Agosto',
  "3M'S - City & Country Rentals",
  '4 City',
  '5 Outubro',
  'A Cor De Cá',
  'A Window',
  'A.',
  'A. Teixeira Da Cunha',
```
(etc)
Lots of unique hosts means lots of options, also a lot of corporations

5. **find all of the places that have more than 2 beds in a neighborhood of your choice**
```shell
db.listings.find( { "neighbourhood_group_cleansed": "PORTO", "beds": 2, "review_scores_rating": { $ne: null } , { _id: 0, name: 1, beds: 1, review_scores_rating: 1, price: 1 } ).sort({ review_scores_rating: -1 })

  {
    name: 'Home in Porto · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$35.00',
    beds: 2,
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath',
    price: '$61.00',
    beds: 2,
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath',
    price: '$85.00',
    beds: 2,
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Porto · ★New · 2 bedrooms · 2 beds · 1 bath',
    price: '$76.00',
    beds: 2,
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Porto · ★New · 1 bedroom · 2 beds · 1 bath',
    price: '$50.00',
    beds: 2,
    review_scores_rating: ''
  },
```
I tried a couple other neighborhoods that weren't as popular, however they didnt have nearly as many search results, and often had no reviews I could analyze
6. **show the number of listings per host**
```shell
db.listings.aggregate([
...   {
...     $group: {
...       _id: "$host_id", // Group by host_id
...       numberOfListings: { $sum: 1 } 
    }
  },
  {
...     }
...   {
...     $sort: { numberOfListings: -1 }
...   }
... ])
  { _id: 12730028, numberOfListings: 260 },
  { _id: 364783572, numberOfListings: 175 },
  { _id: 30907275, numberOfListings: 128 },
  { _id: 2228036, numberOfListings: 94 },
  { _id: 3953109, numberOfListings: 93 },
  { _id: 16922131, numberOfListings: 92 },
```
A small number of hosts hold a significant amount of the Airbnb market in Porto, these are most likely the "superhosts" and the ones under a corporation, basically a hotel chain
7. **find the average review_scores_rating per neighborhood, and only show those that are 4 or above, sorted in descending order of rating**
```shell
ipv2004> db.listings.aggregate([
...   {
...     $group: {
...       _id: "$neighbourhood", // Group by neighbourhood
...       averageRating: { $avg: "$review_scores_rating" } // Calculate the average rating
...     }
...   },
...   {
...     $match: {
...       averageRating: { $gte: 4 } // Filter groups with an average rating of 4 or above
...     }
...   },
...   {
...     $sort: { averageRating: -1 } // Sort by averageRating in descending order
...   }
... ])
[
  { _id: 'muro, Porto, Portugal', averageRating: 5 },
  { _id: 'Gião, Porto, Portugal', averageRating: 5 },
  { _id: 'Rio Tinto, Porto District, Portugal', averageRating: 5 },
  { _id: 'Rio Mau, Porto, Portugal', averageRating: 5 },
  { _id: 'Agua Longa, Portugal', averageRating: 5 },
  { _id: 'Perafita, Po, Portugal', averageRating: 5 },
  { _id: 'Agrela, Santo Tirso, Porto, Portugal', averageRating: 5 },
  ```
  There are a whole lot of really nice neighbourhoods in Porto, this is why I want to go:)

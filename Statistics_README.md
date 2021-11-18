# Statistics_ReadMe
ReadMe file to learn about Statistics how to apply it into the Python Code

## Outlier
- Values that doesn't match the right data of the `graph`
- Values could be `extremly big` or `extremly small`

## Missing Value
- Values that doesn't exist or the status of values are `null`

## Variance
- Get the middle-values by using `Average` number and subtract or plus the number between 
Origin-Data and `Averaged Number`

```
Numbers --> 100 90 80 60
Sum ------> 330
Average --> 82.5

Variance -> (100 - 82.5)^2 (90 - 82.5)^2 (80 - 82.5)^2 (60 - 82.5)^2
             (17.5 + 7.5 + (-2.5) + (-17.5))
        --> (306.25 + 56.25 + 6.25 + 306.25) / 4 = 168.75
```

## Standard Deviation
- Variance covered by Root

```
Standard Deviation -> √168.75 = 12.99
```

## Covariance and Correlation-Coefficient

### Covariance
- Compare Original values and get the `Averaged Number`, and then plus its together
- Multiply several `Variance` Number

### Correlation-Coefficient
- `Covariance` Value / (`A` Standard Deviation) * (`B` Standard Deviation)

### Correlation-Coefficient
- 

## Detail Information (Korean)

### Blog Post
- (`Handle Outlier`)[https://m.blog.naver.com/lingua/221909198917]
- (`Delete Outlier`)[https://m.blog.naver.com/syw0729/221543078133]
- (`Standard-Deviation, Covariance, and Correlation-Coefficient`)[https://todays-review.tistory.com/81]

### Wiki-Doc
- (`Handle Missing-Value`)[https://wikidocs.net/33923]
- (`Print Outlier value`)[https://wikidocs.net/33920]

INSERT INTO continuous_example 
(ORIGIN_ID, TOTAL_BILL, TIP, SEX, SMOKER, DAY, TIME, SIZE)
VALUES
(0, 16.99, 1.01, "Female", "No", "Sun", "Dinner", 2),
(1, 10.34, 1.66, "  Male", "No", "Sun", "Dinner", 3),
(2, 21.01, 3.50, "  Male", "No", "Sun", "Dinner", 3),
(3, 23.68, 3.31, "  Male", "No", "Sun", "Dinner", 2),
(4, 24.59, 3.61, "Female", "No", "Sun", "Dinner", 4);

SELECT * FROM continuous_example;

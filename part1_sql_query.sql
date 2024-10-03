SELECT
	c.customer_id as customer,
	c.age,
	i.item_name as item,
	CAST(SUM(CASE WHEN o.quantity is null THEN 0 else o.quantity END) as INT) as quantity
FROM customers c
INNER JOIN sales s
	ON s.customer_id = c.customer_id
INNER JOIN orders o
	ON o.sales_id = s.sales_id
INNER JOIN items i
	ON i.item_id = o.item_id
WHERE c.age BETWEEN 18 and 35
GROUP BY c.customer_id, c.age, i.item_name
HAVING SUM(CASE WHEN o.quantity is null THEN 0 else o.quantity END) > 0
ORDER BY c.customer_id, c.age, i.item_name

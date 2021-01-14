Respostas 

-- 1

select count(*) from ( select SalesOrderID, count(*) from sales_order_detail group by SalesOrderID having count(*) > 2 ) as sls;


-- 2

select p.DaysToManufacture, p.name, ssod.OrderQty
  from product p
  inner join ( select distinct(ProductID) from special_offer_product sop ) ssop ON ssop.ProductID = p.ProductID
  inner join ( select ProductID, sum(OrderQty) OrderQty from sales_order_detail sod group by ProductID) as ssod ON ssod.ProductID = p.ProductID
order by ssod.OrderQty desc

-- 3

select CONCAT(FirstName,' ',MiddleName,' ',LastName) customer_name, PersonID, BusinessEntityID, ssoh.orders_qty
from person p
inner join customer c on c.PersonID = p.BusinessEntityID
left join (select CustomerID, count(*) orders_qty from sales_order_header group by CustomerID) ssoh ON ssoh.CustomerID = c.CustomerID

-- 4 

select sub.ProductID, sub.OrderDate, sum(sub.OrderQty) order_total_qty
from (SELECT soh.SalesOrderID,soh.OrderDate, sod.OrderQty, sod.ProductID
	FROM sales_order_header soh
	inner join sales_order_detail sod on sod.SalesOrderID = soh.SalesOrderID) as sub
GROUP BY sub.ProductID, sub.OrderDate

-- 5

SELECT SalesOrderID, OrderDate, TotalDue
  FROM teste.sales_order_header
  WHERE substr(OrderDate,1,7) = '2011-09' and TotalDue > 1000
  order by TotalDue desc

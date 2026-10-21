use('ecommerce')


// db.sales.insertMany([
// { _id: 1, item: "Apple",  price: 10, quantity: 5, category: "Fruit" },
// { _id: 2, item: "Banana", price: 5,  quantity: 10, category: "Fruit" },
// { _id: 3, item: "Carrot", price: 8,  quantity: 6, category: "Vegetable" },
// { _id: 4, item: "Tomato", price: 6,  quantity: 8, category: "Vegetable" },
// ])



// db.sales.aggregate([
// { $match: { category: "Fruit" } }
// ]);


// db.sales.aggregate([
// { $project: { _id: 0, item: 1, price: 1 } }
// ]);


db.sales.aggregate([
{
    $group: {
      _id: "$category",
      totalSales: { $sum: { $multiply: ["$price", "$quantity"] } }
        }
    }
])

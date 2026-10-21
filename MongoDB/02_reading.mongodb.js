use('ecommerce')

'For all Data'
// db.products.find()

'For Pretty data'
// db.products.find().pretty()


'For particular Data'
// db.products.find({"name": 'Wireless Mouse'})
// db.products.find({category: 'Electronics'})

'Comparison Opertor'
// db.products.find({ price: { $gt: 1000 } }) 
// db.products.find({price: { $lte:1000, $gte:800 }})
// db.products.find({ price: { $gte: 1000, $lte: 50000 } })

'logical Operator'

'OR'
// db.products.find({ $or: [ {category: "Electronics" }, {stock: { $lt: 50 }} ] })
'AND'
// db.products.find({category: 'Electronics',stock: { $lt: 500 }})

'Select specific fields'
'1 for show , 0 for not show'
// db.products.find({}, { name: 1, price: 1})
// db.products.find({}, { name: 1, price: 1, _id: 0 })


'Sorting and limiting'
'-1 Means Decreasing'

// db.products.find().sort({ price: -1 }).limit(2)
// db.products.find().sort({ price: -1 }).skip(1).limit(2)
// db.products.find().skip(0).limit(10)
// db.products.find().skip(1).limit(2)


// db.products.find({},{name:1})
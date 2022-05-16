### Link
- [chap01. Domain Model Unit Test Example](https://github.com/cosmicpython/code/tree/chapter_01_domain_model_exercise)
- [chap01. Domain Model Unit Test](https://github.com/cosmicpython/code/tree/chapter_01_domain_model)

```mermaid
classDiagram
	direction LR
	class Batch {
		int reference
		str sku
		date eta
		int _purchased_quantity
		OrderLine _allocations
	}

	class OrderLine {
		str orderid
		str sku
		int qty
	}

	Batch *-- OrderLine
```
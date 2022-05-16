### Link
- [chap04. Service Layer](https://github.com/cosmicpython/code/tree/chapter_04_service_layer)
- [chap04. Service Layer Exercise](https://github.com/cosmicpython/code/tree/chapter_04_service_layer_exercise)

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